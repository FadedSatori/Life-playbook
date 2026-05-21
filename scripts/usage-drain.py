#!/usr/bin/env python3
"""
usage-drain.py — Consume Claude subscription capacity before it resets.

The problem: claude.ai subscription windows reset on a rolling basis.
Unused capacity in a window is wasted — it doesn't roll over.
This script auto-fetches real usage data from Anthropic's internal API
(the same endpoint used by the claude-usage-extension Chrome extension),
calculates optimal burn time, and generates Life-playbook content to
consume near-expiring capacity.

Quickstart:
  python3 usage-drain.py --setup        # extract & store your OAuth token
  python3 usage-drain.py --check        # show live usage + projected waste
  python3 usage-drain.py --schedule     # sleep until burn time, then auto-fire
  python3 usage-drain.py --watch        # run continuously
  python3 usage-drain.py --burn 30      # burn ~30% now (needs ANTHROPIC_API_KEY)
"""

import argparse
import json
import math
import os
import platform
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ─── Constants ────────────────────────────────────────────────────────────────

USAGE_ENDPOINT = "https://api.anthropic.com/api/oauth/usage"
USAGE_HEADERS  = {
    "anthropic-beta": "oauth-2025-04-20",
    "User-Agent":     "claude-code/2.1.34",
}

CONFIG_PATH = Path(__file__).parent / "usage-drain.config.json"
LOG_PATH    = Path.home() / ".usage-drain.log"

DEFAULT_CONFIG = {
    "oauth_token": None,           # sk-ant-oat01-... stored here after --setup
    "settings": {
        "burn_threshold_pct":    15,   # only burn if >15% will go to waste
        "safe_buffer_minutes":   12,   # start burn this many minutes before reset
        "watch_interval_minutes": 5,   # how often --watch polls (minutes)
        "min_burn_pct":          10,   # minimum burn size (avoid tiny sessions)
    },
    "anthropic": {
        "api_key_env":   "ANTHROPIC_API_KEY",
        "model":         "claude-haiku-4-5-20251001",
        "playbook_repo": str(Path(__file__).parent.parent),
    },
    "burn_history": [],
}

PLAYBOOK_TOPICS = [
    ("energy-management.md",    "energy management and ultradian rhythms, peak performance windows, recovery cycles, and the science of managing energy rather than time"),
    ("identity-design.md",      "deliberately designing your identity — the concept that identity precedes behavior, how to choose and reinforce who you are, and techniques for identity-level change"),
    ("communication-mastery.md","communication at the highest level — written precision, spoken clarity under pressure, listening as a competitive advantage, and difficult conversations"),
    ("resilience-protocols.md", "mental and emotional resilience — the difference between resilience and toughness, recovery from failure, post-traumatic growth, and the neuroscience of bouncing back"),
    ("wealth-philosophy.md",    "a deep philosophy of wealth — what it actually is (time, options, freedom), how to build it without losing yourself, and the relationship between money and meaning"),
    ("social-dynamics.md",      "deep social dynamics — status hierarchies, dominance vs. prestige, how groups really work, and how to navigate social environments with precision"),
    ("the-body-as-instrument.md","the body as primary instrument — martial arts philosophy applied to daily movement, proprioception, ground, and treating the body as a tool to be mastered"),
    ("mental-health-protocols.md","a rigorous, non-clinical approach to mental health — emotional regulation, nervous system regulation, processing difficulty, and building psychological strength"),
    ("time-philosophy.md",      "a complete philosophy of time — deep work, time blocking, the 4Ds, Eisenhower matrix, and the radical idea that most urgency is manufactured"),
    ("the-dark-night.md",       "navigating the dark night of the soul — the periods of disorientation and loss of meaning that precede transformation, and how to survive and use them"),
    ("power-dynamics.md",       "power — how it works, how it accumulates, how it corrupts, and how to hold it without being destroyed by it"),
    ("creative-process.md",     "the creative process — divergence and convergence, the role of constraints, creative blocks as diagnostic signals, and building a sustainable creative practice"),
]


# ─── Config I/O ───────────────────────────────────────────────────────────────

def load_config() -> dict:
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH) as f:
            data = json.load(f)
        for key, val in DEFAULT_CONFIG.items():
            if key not in data:
                data[key] = val
        return data
    return dict(DEFAULT_CONFIG)


def save_config(cfg: dict):
    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2, default=str)


def log(msg: str):
    ts   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_PATH, "a") as f:
        f.write(line + "\n")


# ─── OAuth token extraction ───────────────────────────────────────────────────

def extract_token_auto() -> str | None:
    """Try to extract the Claude Code OAuth token from platform credentials."""
    system = platform.system()

    if system == "Darwin":
        # macOS Keychain
        try:
            result = subprocess.run(
                ["security", "find-generic-password", "-s", "Claude Code-credentials", "-w"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0 and result.stdout.strip():
                raw = result.stdout.strip()
                # May be raw token or JSON with accessToken key
                try:
                    data = json.loads(raw)
                    return data.get("claudeAiOauth", {}).get("accessToken") or data.get("accessToken")
                except json.JSONDecodeError:
                    return raw if raw.startswith("sk-ant-") else None
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

    elif system == "Windows":
        creds_path = Path(os.environ.get("APPDATA", "")) / "Claude" / "credentials.json"
        if creds_path.exists():
            with open(creds_path) as f:
                data = json.load(f)
            return data.get("claudeAiOauth", {}).get("accessToken") or data.get("accessToken")

    else:
        # Linux — check common paths
        for candidate in [
            Path.home() / ".config" / "claude" / "credentials.json",
            Path.home() / ".claude" / "credentials.json",
        ]:
            if candidate.exists():
                with open(candidate) as f:
                    data = json.load(f)
                return data.get("claudeAiOauth", {}).get("accessToken") or data.get("accessToken")

    return None


def get_token(cfg: dict) -> str | None:
    """Return stored token, or env override."""
    return os.environ.get("CLAUDE_OAUTH_TOKEN") or cfg.get("oauth_token")


# ─── Live usage fetch ─────────────────────────────────────────────────────────

def fetch_usage(token: str) -> dict | None:
    """
    Hit api.anthropic.com/api/oauth/usage and return parsed JSON.

    Response shape:
      five_hour:        { utilization, resetsAt, ... }
      seven_day:        { utilization, resetsAt, ... }
      seven_day_sonnet: { utilization, resetsAt, ... }
      extra_usage:      { enabled, used, monthlyLimit, utilization }
    """
    try:
        import httpx
    except ImportError:
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "httpx", "-q"], check=True)
            import httpx
        except Exception:
            print("Error: install httpx — pip3 install httpx")
            return None

    headers = {**USAGE_HEADERS, "Authorization": f"Bearer {token}"}
    try:
        r = httpx.get(USAGE_ENDPOINT, headers=headers, timeout=10)
        r.raise_for_status()
        return r.json()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 401:
            print("✗ Token rejected (401). Run --setup to refresh your token.")
        else:
            print(f"✗ API error {e.response.status_code}: {e.response.text[:200]}")
        return None
    except Exception as e:
        print(f"✗ Request failed: {e}")
        return None


def parse_window(raw: dict) -> dict:
    """Normalise a usage window from the API into our internal format."""
    utilization = raw.get("utilization", 0) or 0      # 0–1 float or 0–100 int
    if utilization > 1:
        utilization /= 100                             # normalise to 0–1
    remaining_pct = round((1 - utilization) * 100, 1)

    reset_at = None
    for key in ("resetsAt", "resets_at", "resetAt", "reset_at"):
        if raw.get(key):
            val = raw[key]
            # May be ISO string or epoch millis
            if isinstance(val, (int, float)):
                reset_at = datetime.fromtimestamp(val / 1000).isoformat()
            else:
                reset_at = val
            break

    return {
        "remaining_pct": remaining_pct,
        "reset_at":      reset_at,
        "last_updated":  datetime.now().isoformat(),
        "raw":           raw,
    }


# ─── Math ─────────────────────────────────────────────────────────────────────

def minutes_until_reset(window: dict) -> float | None:
    if not window.get("reset_at"):
        return None
    reset_str = window["reset_at"]
    try:
        reset = datetime.fromisoformat(reset_str)
        # Make timezone-naive for comparison
        if reset.tzinfo is not None:
            reset = reset.astimezone(timezone.utc).replace(tzinfo=None)
    except ValueError:
        return None
    delta = (reset - datetime.utcnow()).total_seconds() / 60
    return max(0.0, delta)


def projected_waste(window: dict, settings: dict) -> float | None:
    remaining = window.get("remaining_pct")
    if remaining is None:
        return None
    mins_left = minutes_until_reset(window)
    if mins_left is None:
        return None
    if mins_left <= 0:
        return 0.0
    return float(remaining)


def optimal_burn_time(window: dict, settings: dict) -> datetime | None:
    mins_left = minutes_until_reset(window)
    if mins_left is None:
        return None
    burn_in = max(0, mins_left - settings["safe_buffer_minutes"])
    return datetime.now() + timedelta(minutes=burn_in)


# ─── Display ──────────────────────────────────────────────────────────────────

def fmt_mins(mins: float) -> str:
    if mins < 60:
        return f"{mins:.0f}m"
    h, m = int(mins // 60), int(mins % 60)
    return f"{h}h {m}m"


def print_window_status(label: str, window: dict, settings: dict):
    remaining  = window.get("remaining_pct")
    mins_left  = minutes_until_reset(window)
    waste      = projected_waste(window, settings)
    burn_time  = optimal_burn_time(window, settings)
    threshold  = settings["burn_threshold_pct"]

    print(f"\n  ┌─ {label}")
    if remaining is None or mins_left is None:
        print(f"  │  No data — run --check after --setup")
    else:
        stale = ""
        if window.get("last_updated"):
            age = (datetime.now() - datetime.fromisoformat(window["last_updated"])).total_seconds() / 60
            if age > 15:
                stale = f"  ⚠ {fmt_mins(age)} old"

        bar_filled = int(remaining / 5)
        bar = "█" * bar_filled + "░" * (20 - bar_filled)
        print(f"  │  Remaining : {remaining:.1f}%  [{bar}]{stale}")
        print(f"  │  Resets in : {fmt_mins(mins_left)}")

        if waste is not None:
            if waste >= threshold:
                print(f"  │  Waste risk: {waste:.0f}% → BURN RECOMMENDED")
                if burn_time:
                    delta = (burn_time - datetime.now()).total_seconds() / 60
                    if delta <= 0:
                        print(f"  │  Trigger at: NOW")
                    else:
                        print(f"  │  Trigger at: {burn_time.strftime('%H:%M')} (in {fmt_mins(delta)})")
            else:
                print(f"  │  Waste risk: {waste:.0f}%  (below {threshold}% threshold — no burn needed)")
    print(f"  └{'─' * 52}")


# ─── Commands ─────────────────────────────────────────────────────────────────

def cmd_setup(cfg):
    """Extract the OAuth token and store it in config."""
    print("Looking for Claude Code OAuth token...\n")
    token = extract_token_auto()

    if token and token.startswith("sk-ant-"):
        print(f"✓ Token found automatically: {token[:18]}...")
    else:
        print("Automatic extraction didn't find a token.")
        print("\nGet it manually:")
        print("  macOS:   security find-generic-password -s 'Claude Code-credentials' -w")
        print("  Windows: open %APPDATA%\\Claude\\credentials.json → accessToken")
        print("  Linux:   cat ~/.config/claude/credentials.json | python3 -c \"import sys,json; print(json.load(sys.stdin)['accessToken'])\"")
        print("\nOr open claude.ai → DevTools (F12) → Console → run:")
        print("  JSON.parse(localStorage.getItem('__claude_ai_oauth') || '{}')?.accessToken")
        token = input("\nPaste token here: ").strip()

    if not token or not token.startswith("sk-ant-"):
        print("✗ Invalid token format. Expected sk-ant-oat01-...")
        sys.exit(1)

    cfg["oauth_token"] = token
    save_config(cfg)
    print("\nToken saved. Testing connection...")
    usage = fetch_usage(token)
    if usage:
        print("✓ Connection successful. Run --check to see your usage.")
    else:
        print("✗ Could not reach usage endpoint. Token may be expired.")


def cmd_check(cfg, live: bool = True):
    token = get_token(cfg)
    windows = {}

    if live and token:
        usage = fetch_usage(token)
        if usage:
            if "five_hour" in usage:
                windows["5-HOUR WINDOW"] = parse_window(usage["five_hour"])
            if "seven_day" in usage:
                windows["7-DAY WINDOW"] = parse_window(usage["seven_day"])
            if usage.get("extra_usage", {}).get("enabled"):
                eu = usage["extra_usage"]
                used_pct = (eu.get("used", 0) / eu.get("monthlyLimit", 1)) * 100
                print(f"\n  Extra credits: {100 - used_pct:.1f}% remaining this month")
        else:
            print("Could not fetch live data.")
    elif not token:
        print("No OAuth token. Run --setup first.")
        return

    print(f"\n{'═' * 56}")
    print(f"  USAGE-DRAIN  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'═' * 56}")

    if not windows:
        print("  No window data available.")
    for label, window in windows.items():
        print_window_status(label, window, cfg["settings"])

    print()
    return windows


def cmd_schedule(cfg):
    token = get_token(cfg)
    if not token:
        print("No OAuth token. Run --setup first.")
        sys.exit(1)

    usage = fetch_usage(token)
    if not usage:
        sys.exit(1)

    schedule = []
    for key, label in [("five_hour", "5-hour"), ("seven_day", "7-day")]:
        if key not in usage:
            continue
        window = parse_window(usage[key])
        waste  = projected_waste(window, cfg["settings"])
        if waste is None or waste < cfg["settings"]["burn_threshold_pct"]:
            print(f"[{label}] No burn needed (waste {waste or 0:.0f}%)")
            continue
        bt = optimal_burn_time(window, cfg["settings"])
        if bt:
            schedule.append((label, waste, bt))

    if not schedule:
        print("Nothing to schedule.")
        return

    for label, waste, bt in schedule:
        delta_secs = max(0, (bt - datetime.now()).total_seconds())
        log(f"[{label}] Burn {waste:.0f}% scheduled at {bt.strftime('%H:%M:%S')} (in {fmt_mins(delta_secs/60)})")

    # Wait for the earliest burn
    schedule.sort(key=lambda x: x[2])
    label, waste, bt = schedule[0]
    delta_secs = max(0, (bt - datetime.now()).total_seconds())

    if delta_secs > 0:
        print(f"\nSleeping {fmt_mins(delta_secs / 60)}... (Ctrl+C to cancel)")
        try:
            time.sleep(delta_secs)
        except KeyboardInterrupt:
            print("\nCancelled.")
            return

    cmd_burn(cfg, int(waste))


def cmd_burn(cfg, target_pct: int):
    api_key = os.environ.get(cfg["anthropic"]["api_key_env"])
    if not api_key:
        print(f"Error: export {cfg['anthropic']['api_key_env']}=sk-ant-api03-...")
        print("(This is your Anthropic API key — different from the OAuth token.)")
        sys.exit(1)

    try:
        import anthropic as sdk
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "anthropic", "-q"], check=True)
        import anthropic as sdk

    repo_path = Path(cfg["anthropic"]["playbook_repo"])
    model     = cfg["anthropic"]["model"]
    client    = sdk.Anthropic(api_key=api_key)

    existing   = {f.name for f in repo_path.glob("*.md")}
    candidates = [(f, t) for f, t in PLAYBOOK_TOPICS if f not in existing]
    if not candidates:
        log("All topics done — appending custom expansion")
        candidates = [("expansion.md", "the single most underdeveloped area of the current Life Playbook")]

    n_topics = max(1, math.ceil(target_pct / 12))
    to_gen   = candidates[:n_topics]

    log(f"BURN START — target {target_pct}%, generating {len(to_gen)} topic(s)")
    generated = []

    for filename, topic_desc in to_gen:
        out_path = repo_path / filename
        log(f"  Generating: {filename}")
        prompt = f"""You are writing a section of a personal Life Playbook — a private, opinionated knowledge base for elite personal development.

Write a comprehensive, deeply useful file on: {topic_desc}

STYLE RULES (follow exactly):
- Direct, second-person imperative voice ("Do X")
- Short declarative sentences. Zero hedging.
- Numbered principles (3-5 per section)
- Specific metrics, thresholds, named techniques — never vague
- Structure: purpose statement → principles → protocols/frameworks
- Cross-link to related playbook files with relative Markdown links
- Tone: warrior-philosopher. Marcus Aurelius meets Nassim Taleb meets a Navy SEAL.

Format: pure Markdown, start with # [Title]"""

        try:
            resp    = client.messages.create(model=model, max_tokens=2000,
                                             messages=[{"role": "user", "content": prompt}])
            content = resp.content[0].text
            out_path.write_text(content)
            generated.append(filename)
            log(f"  ✓ {filename} ({resp.usage.input_tokens + resp.usage.output_tokens} tokens)")
        except Exception as e:
            log(f"  ✗ {filename} — {e}")

    if generated:
        try:
            subprocess.run(["git", "add"] + generated, cwd=repo_path, check=True, capture_output=True)
            subprocess.run(["git", "commit", "-m",
                            f"Auto-generated playbook content: {', '.join(generated)}"],
                           cwd=repo_path, check=True, capture_output=True)
            log(f"✓ Committed {len(generated)} file(s)")
        except subprocess.CalledProcessError as e:
            log(f"Git commit failed: {e}")

        cfg["burn_history"].append({
            "time": datetime.now().isoformat(),
            "target_pct": target_pct,
            "files": generated,
        })
        save_config(cfg)

    log(f"BURN COMPLETE — {len(generated)} file(s) generated")


def cmd_watch(cfg):
    interval = cfg["settings"]["watch_interval_minutes"] * 60
    log(f"WATCH mode — polling every {cfg['settings']['watch_interval_minutes']}m")
    token = get_token(cfg)
    if not token:
        print("No OAuth token. Run --setup first.")
        sys.exit(1)

    print("Press Ctrl+C to stop.\n")
    try:
        while True:
            usage = fetch_usage(token)
            if usage:
                for key, label in [("five_hour", "5-hour"), ("seven_day", "7-day")]:
                    if key not in usage:
                        continue
                    window = parse_window(usage[key])
                    waste  = projected_waste(window, cfg["settings"])
                    bt     = optimal_burn_time(window, cfg["settings"])
                    if waste and waste >= cfg["settings"]["burn_threshold_pct"] and bt:
                        delta = (bt - datetime.now()).total_seconds()
                        if delta <= 0:
                            log(f"[{label}] Window closing — burning {waste:.0f}%")
                            cmd_burn(cfg, int(waste))
                            cfg = load_config()
                        else:
                            log(f"[{label}] {waste:.0f}% waste projected — burn in {fmt_mins(delta/60)}")
            time.sleep(interval)
    except KeyboardInterrupt:
        log("WATCH stopped.")


# ─── Entry point ──────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(
        description="Zero-waste Claude subscription manager.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  --setup       Extract & store your OAuth token (run once)
  --check       Show live usage and projected waste
  --schedule    Sleep until burn time, then auto-generate playbook content
  --watch       Run continuously, fires automatically near each reset
  --burn PCT    Burn PCT% now (needs ANTHROPIC_API_KEY env var)
        """
    )
    p.add_argument("--setup",    action="store_true", help="Extract and store OAuth token")
    p.add_argument("--check",    action="store_true", help="Show live usage status")
    p.add_argument("--schedule", action="store_true", help="Schedule and execute burn")
    p.add_argument("--watch",    action="store_true", help="Run continuously")
    p.add_argument("--burn",     type=int, metavar="PCT", help="Burn PCT%% of capacity now")

    args = p.parse_args()
    cfg  = load_config()

    if   args.setup:    cmd_setup(cfg)
    elif args.check:    cmd_check(cfg)
    elif args.schedule: cmd_schedule(cfg)
    elif args.watch:    cmd_watch(cfg)
    elif args.burn is not None: cmd_burn(cfg, args.burn)
    else:               p.print_help()


if __name__ == "__main__":
    main()
