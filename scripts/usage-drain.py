#!/usr/bin/env python3
"""
usage-drain.py — Consume Claude subscription capacity before it resets.

The problem: claude.ai subscription windows reset on a rolling basis.
Unused capacity in a window is wasted — it doesn't roll over.
This script calculates the optimal burn time and generates useful
Life-playbook content to consume near-expiring capacity.

Usage:
  python3 usage-drain.py --check
  python3 usage-drain.py --set-window --duration 240 --remaining 72 --resets-in 95
  python3 usage-drain.py --schedule
  python3 usage-drain.py --burn 30
  python3 usage-drain.py --watch
"""

import argparse
import json
import math
import os
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

# ─── Config ───────────────────────────────────────────────────────────────────

CONFIG_PATH = Path(__file__).parent / "usage-drain.config.json"
LOG_PATH = Path.home() / ".usage-drain.log"

DEFAULT_CONFIG = {
    "windows": {
        "short": {
            "duration_minutes": 240,       # 4-hour block
            "remaining_pct": None,         # set via --set-window
            "reset_at": None,              # ISO datetime string
            "last_updated": None
        },
        "weekly": {
            "duration_minutes": 10080,     # 7 days
            "remaining_pct": None,
            "reset_at": None,
            "last_updated": None
        }
    },
    "settings": {
        "burn_threshold_pct": 15,          # only burn if >15% will go to waste
        "safe_buffer_minutes": 12,         # start burn this many minutes before reset
        "watch_interval_minutes": 10,      # how often --watch polls
        "min_burn_pct": 10                 # minimum burn size (avoid tiny sessions)
    },
    "anthropic": {
        "api_key_env": "ANTHROPIC_API_KEY",
        "model": "claude-haiku-4-5-20251001",
        "playbook_repo": str(Path(__file__).parent.parent)
    },
    "burn_history": []
}

PLAYBOOK_TOPICS = [
    ("energy-management.md", "energy management and ultradian rhythms, peak performance windows, recovery cycles, and the science of managing energy rather than time"),
    ("identity-design.md", "deliberately designing your identity — the concept that identity precedes behavior, how to choose and reinforce who you are, and techniques for identity-level change"),
    ("communication-mastery.md", "communication at the highest level — written precision, spoken clarity under pressure, listening as a competitive advantage, and difficult conversations"),
    ("resilience-protocols.md", "mental and emotional resilience — the difference between resilience and toughness, recovery from failure, post-traumatic growth, and the neuroscience of bouncing back"),
    ("wealth-philosophy.md", "a deep philosophy of wealth — what it actually is (time, options, freedom), how to build it without losing yourself, and the relationship between money and meaning"),
    ("social-dynamics.md", "deep social dynamics — status hierarchies, dominance vs. prestige, how groups really work, and how to navigate social environments with precision"),
    ("the-body-as-instrument.md", "the body as primary instrument — martial arts philosophy applied to daily movement, proprioception, ground, and treating the body as a tool to be mastered"),
    ("mental-health-protocols.md", "a rigorous, non-clinical approach to mental health — emotional regulation, nervous system regulation, processing difficulty, and building psychological strength"),
    ("time-philosophy.md", "a complete philosophy of time — deep work, time blocking, the 4Ds, Eisenhower matrix, and the radical idea that most urgency is manufactured"),
    ("the-dark-night.md", "navigating the dark night of the soul — the periods of disorientation and loss of meaning that precede transformation, and how to survive and use them"),
    ("power-dynamics.md", "power — how it works, how it accumulates, how it corrupts, and how to hold it without being destroyed by it"),
    ("creative-process.md", "the creative process — divergence and convergence, the role of constraints, creative blocks as diagnostic signals, and building a sustainable creative practice"),
]


# ─── Config I/O ───────────────────────────────────────────────────────────────

def load_config():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH) as f:
            data = json.load(f)
        # Merge with defaults to handle new keys
        for key, val in DEFAULT_CONFIG.items():
            if key not in data:
                data[key] = val
        return data
    return dict(DEFAULT_CONFIG)


def save_config(cfg):
    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2, default=str)


def log(msg: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_PATH, "a") as f:
        f.write(line + "\n")


# ─── Math ─────────────────────────────────────────────────────────────────────

def minutes_until_reset(window: dict) -> float | None:
    """Return minutes until the window resets, or None if unknown."""
    if not window.get("reset_at"):
        return None
    reset = datetime.fromisoformat(window["reset_at"])
    delta = (reset - datetime.now()).total_seconds() / 60
    return max(0.0, delta)


def projected_waste(window: dict, settings: dict) -> float | None:
    """
    How much capacity (%) will go unused if we do nothing.

    waste = remaining - expected_natural_consumption
    expected_natural_consumption ≈ 0  (conservative assumption: don't count on
    organic usage, so all remaining is treated as potential waste)
    """
    remaining = window.get("remaining_pct")
    if remaining is None:
        return None
    mins_left = minutes_until_reset(window)
    if mins_left is None:
        return None
    # If the window has already expired, waste is 0
    if mins_left <= 0:
        return 0.0
    return float(remaining)


def optimal_burn_time(window: dict, settings: dict) -> datetime | None:
    """When to start the burn session to hit the reset just right."""
    mins_left = minutes_until_reset(window)
    if mins_left is None:
        return None
    buffer = settings["safe_buffer_minutes"]
    burn_in_minutes = max(0, mins_left - buffer)
    return datetime.now() + timedelta(minutes=burn_in_minutes)


# ─── Display ──────────────────────────────────────────────────────────────────

def fmt_minutes(mins: float) -> str:
    if mins < 60:
        return f"{mins:.0f}m"
    h = int(mins // 60)
    m = int(mins % 60)
    return f"{h}h {m}m"


def print_window_status(name: str, window: dict, settings: dict):
    remaining = window.get("remaining_pct")
    mins_left = minutes_until_reset(window)
    waste = projected_waste(window, settings)
    burn_time = optimal_burn_time(window, settings)

    print(f"\n  ┌─ {name.upper()} WINDOW ({'%.0f' % (window['duration_minutes']/60)}h)")

    if remaining is None or mins_left is None:
        print(f"  │  Status:    NOT CONFIGURED")
        print(f"  │  Run:       --set-window --window {name} --remaining <pct> --resets-in <minutes>")
    else:
        stale_warn = ""
        if window.get("last_updated"):
            updated = datetime.fromisoformat(window["last_updated"])
            stale_mins = (datetime.now() - updated).total_seconds() / 60
            if stale_mins > 30:
                stale_warn = f" ⚠ data is {fmt_minutes(stale_mins)} old"

        print(f"  │  Remaining: {remaining:.0f}%{stale_warn}")
        print(f"  │  Resets in: {fmt_minutes(mins_left)}")
        if waste is not None:
            print(f"  │  Projected waste: {waste:.0f}%")
        if waste and waste >= settings["burn_threshold_pct"]:
            print(f"  │  ✓ Burn recommended: ~{waste:.0f}% before reset")
            if burn_time:
                delta = (burn_time - datetime.now()).total_seconds() / 60
                if delta <= 0:
                    print(f"  │  Burn time:  NOW (window closing soon)")
                else:
                    print(f"  │  Burn time:  in {fmt_minutes(delta)} ({burn_time.strftime('%H:%M:%S')})")
        else:
            print(f"  │  No burn needed (waste {waste:.0f}% < threshold {settings['burn_threshold_pct']}%)")
    print(f"  └{'─' * 50}")


# ─── Commands ─────────────────────────────────────────────────────────────────

def cmd_check(cfg):
    print(f"\n{'═' * 54}")
    print(f"  USAGE-DRAIN STATUS  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'═' * 54}")
    for name, window in cfg["windows"].items():
        print_window_status(name, window, cfg["settings"])
    print()


def cmd_set_window(cfg, args):
    window_name = args.window or "short"
    if window_name not in cfg["windows"]:
        print(f"Error: unknown window '{window_name}'. Choose: {list(cfg['windows'].keys())}")
        sys.exit(1)

    window = cfg["windows"][window_name]

    if args.duration:
        window["duration_minutes"] = args.duration
    if args.remaining is not None:
        window["remaining_pct"] = args.remaining
    if args.resets_in is not None:
        window["reset_at"] = (datetime.now() + timedelta(minutes=args.resets_in)).isoformat()
    if args.resets_at:
        window["reset_at"] = datetime.fromisoformat(args.resets_at).isoformat()

    window["last_updated"] = datetime.now().isoformat()
    save_config(cfg)
    print(f"✓ {window_name} window updated.")
    cmd_check(cfg)


def cmd_schedule(cfg):
    scheduled_any = False
    for name, window in cfg["windows"].items():
        waste = projected_waste(window, cfg["settings"])
        if waste is None:
            print(f"[{name}] Skipping — not configured. Run --set-window first.")
            continue
        if waste < cfg["settings"]["burn_threshold_pct"]:
            print(f"[{name}] No burn needed. Projected waste ({waste:.0f}%) < threshold ({cfg['settings']['burn_threshold_pct']}%).")
            continue

        burn_time = optimal_burn_time(window, cfg["settings"])
        if burn_time is None:
            continue

        delta_secs = (burn_time - datetime.now()).total_seconds()
        if delta_secs < 0:
            delta_secs = 0

        log(f"[{name}] Scheduled burn of {waste:.0f}% in {fmt_minutes(delta_secs/60)} at {burn_time.strftime('%H:%M:%S')}")
        scheduled_any = True

        # Sleep until burn time, then execute
        if delta_secs > 0:
            print(f"Sleeping {fmt_minutes(delta_secs/60)}... (Ctrl+C to cancel)")
            try:
                time.sleep(delta_secs)
            except KeyboardInterrupt:
                print("\nSchedule cancelled.")
                return

        burn_pct = max(int(waste), cfg["settings"]["min_burn_pct"])
        cmd_burn(cfg, burn_pct, window_name=name)

    if not scheduled_any:
        print("Nothing to schedule.")


def cmd_burn(cfg, target_pct: int, window_name: str = "short"):
    api_key = os.environ.get(cfg["anthropic"]["api_key_env"])
    if not api_key:
        print(f"Error: set {cfg['anthropic']['api_key_env']} environment variable to enable burns.")
        sys.exit(1)

    try:
        import anthropic
    except ImportError:
        print("Error: anthropic package not installed. Run: pip3 install anthropic")
        sys.exit(1)

    repo_path = Path(cfg["anthropic"]["playbook_repo"])
    model = cfg["anthropic"]["model"]
    client = anthropic.Anthropic(api_key=api_key)

    # Pick a topic that doesn't already exist
    existing = {f.name for f in repo_path.glob("*.md")}
    candidates = [(fname, topic) for fname, topic in PLAYBOOK_TOPICS if fname not in existing]

    if not candidates:
        log("All predefined topics exist — generating a custom expansion instead.")
        candidates = [("custom-expansion.md", "a deep, actionable expansion of the most underdeveloped area of the Life Playbook")]

    log(f"BURN START — target: {target_pct}% of {window_name} window, model: {model}")

    # Scale the number of topics to generate based on target_pct
    # 10% ≈ 1 topic, 100% ≈ 8 topics (rough heuristic)
    n_topics = max(1, math.ceil(target_pct / 12))
    topics_to_generate = candidates[:n_topics]

    generated = []
    for filename, topic_desc in topics_to_generate:
        out_path = repo_path / filename
        log(f"  Generating: {filename}")

        prompt = f"""You are writing a section of a personal Life Playbook — a private, opinionated knowledge base for elite personal development.

Write a comprehensive, deeply useful file on: {topic_desc}

STYLE RULES (follow exactly):
- Direct, second-person voice ("you"), imperative default ("Do X")
- Short declarative sentences. No hedging.
- Numbered principles (3-5 per section)
- Specific metrics, thresholds, techniques — not vague guidance
- Sections follow: purpose statement → principles → protocols/frameworks
- Cross-link to related files with relative Markdown links when relevant
- Tone: warrior-philosopher. Think Marcus Aurelius meets a Navy SEAL meets Nassim Taleb.
- No fluff, no caveats, no academic hedging.

Existing files in the playbook you can reference:
principles.md, warrior-codes.md, stoic-practice.md, shadow-work.md,
antifragility.md, flow-states.md, mythology-archetypes.md, longevity-protocols.md,
maxims.md, heuristics.md, strategy.md, force-multipliers.md,
tactics/social.md, tactics/field.md, tactics/cognitive.md

Format: pure Markdown, start with # [Title]"""

        try:
            response = client.messages.create(
                model=model,
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )
            content = response.content[0].text
            out_path.write_text(content)
            generated.append(filename)
            tokens_used = response.usage.input_tokens + response.usage.output_tokens
            log(f"  ✓ {filename} ({tokens_used} tokens)")
        except Exception as e:
            log(f"  ✗ {filename} — ERROR: {e}")

    if generated:
        # Commit the generated files
        try:
            files_str = " ".join(f'"{f}"' for f in generated)
            subprocess.run(
                ["git", "add"] + generated,
                cwd=repo_path, check=True, capture_output=True
            )
            commit_msg = f"Auto-generated playbook content: {', '.join(generated)}"
            subprocess.run(
                ["git", "commit", "-m", commit_msg],
                cwd=repo_path, check=True, capture_output=True
            )
            log(f"✓ Committed {len(generated)} files: {', '.join(generated)}")
        except subprocess.CalledProcessError as e:
            log(f"  Git commit failed: {e}")

        # Record burn in history
        cfg["burn_history"].append({
            "time": datetime.now().isoformat(),
            "window": window_name,
            "target_pct": target_pct,
            "files_generated": generated
        })
        save_config(cfg)

    log(f"BURN COMPLETE — {len(generated)} files generated")


def cmd_watch(cfg):
    interval = cfg["settings"]["watch_interval_minutes"] * 60
    log(f"WATCH mode started — polling every {cfg['settings']['watch_interval_minutes']}m")
    print("Press Ctrl+C to stop.\n")
    try:
        while True:
            cmd_check(cfg)
            cfg = load_config()  # Reload in case user updated via --set-window
            for name, window in cfg["windows"].items():
                waste = projected_waste(window, cfg["settings"])
                burn_time = optimal_burn_time(window, cfg["settings"])
                if waste and waste >= cfg["settings"]["burn_threshold_pct"] and burn_time:
                    delta = (burn_time - datetime.now()).total_seconds()
                    if delta <= 0:
                        log(f"[{name}] Burn window open — executing now")
                        cmd_burn(cfg, int(waste), window_name=name)
                        cfg = load_config()
            time.sleep(interval)
    except KeyboardInterrupt:
        log("WATCH mode stopped.")


# ─── Entry point ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Consume Claude subscription capacity before it resets.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("check", help="Show current usage status and projected waste")

    sw = sub.add_parser("set-window", help="Update a window's remaining capacity and reset time")
    sw.add_argument("--window", choices=["short", "weekly"], default="short")
    sw.add_argument("--remaining", type=float, help="Remaining capacity (0–100%%)")
    sw.add_argument("--resets-in", type=float, dest="resets_in", metavar="MINUTES", help="Minutes until reset")
    sw.add_argument("--resets-at", dest="resets_at", metavar="DATETIME", help="Reset datetime (ISO format)")
    sw.add_argument("--duration", type=int, help="Window duration in minutes")

    sub.add_parser("schedule", help="Sleep until burn time, then execute")

    burn_p = sub.add_parser("burn", help="Execute a burn session now")
    burn_p.add_argument("pct", type=int, nargs="?", default=25, help="Target %% of capacity to consume (default: 25)")
    burn_p.add_argument("--window", choices=["short", "weekly"], default="short")

    sub.add_parser("watch", help="Run continuously, auto-scheduling burns")

    # Also support the old --flag style for convenience
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--schedule", action="store_true")
    parser.add_argument("--watch", action="store_true")
    parser.add_argument("--burn", type=int, metavar="PCT")
    parser.add_argument("--set-window", action="store_true", dest="set_window")
    parser.add_argument("--window", choices=["short", "weekly"], default="short")
    parser.add_argument("--remaining", type=float)
    parser.add_argument("--resets-in", type=float, dest="resets_in", metavar="MINUTES")
    parser.add_argument("--resets-at", dest="resets_at", metavar="DATETIME")
    parser.add_argument("--duration", type=int)

    args = parser.parse_args()
    cfg = load_config()

    # Subcommand dispatch
    if args.command == "check" or args.check:
        cmd_check(cfg)
    elif args.command == "set-window" or args.set_window:
        cmd_set_window(cfg, args)
    elif args.command == "schedule" or args.schedule:
        cmd_schedule(cfg)
    elif args.command == "burn":
        cmd_burn(cfg, args.pct, window_name=args.window)
    elif args.burn is not None:
        cmd_burn(cfg, args.burn)
    elif args.command == "watch" or args.watch:
        cmd_watch(cfg)
    else:
        parser.print_help()
        print("\nQuickstart:")
        print("  1. Check the claude.ai UI for your remaining % and minutes until reset")
        print("  2. python3 usage-drain.py --set-window --remaining 72 --resets-in 95")
        print("  3. python3 usage-drain.py --check")
        print("  4. python3 usage-drain.py --schedule   (sleeps then burns)")
        print("  5. export ANTHROPIC_API_KEY=sk-ant-...")


if __name__ == "__main__":
    main()
