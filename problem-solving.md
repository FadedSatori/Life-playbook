# Problem Solving

Most problems aren't hard because they're complex. They're hard because people solve the wrong problem, grab the first solution, or keep treating a symptom while the cause sits untouched. Skill at problem solving is mostly discipline: slow down at the start, speed up at the end.

This file is a general method. It works on a broken process at work, a recurring fight at home, a stalled project, a health puzzle, or a business that won't grow. The tools are old and proven: Pólya's four steps, root-cause analysis from Toyota, inversion, decomposition, small experiments. The protocol at the end puts them in order, and the template fits on one page. [mental-models/decision-making.md](mental-models/decision-making.md) covers choosing among options; this file covers finding the right problem and generating options worth choosing among.

---

## Define the Problem Before You Touch It

**A problem stated precisely is half solved.** The line about Einstein spending 55 of 60 minutes defining a problem has no good source, but the idea is sound. Vague problems produce vague solutions.

**Write a problem statement:**
1. **Current state:** what's happening, in observable facts.
2. **Desired state:** what should be happening, in measurable terms.
3. **Gap:** the difference, quantified where possible.
4. **Constraints:** time, money, people, rules that can't move.
5. **Done looks like:** how you'll know it's solved.

**Symptom, problem, or disguised solution?** "We keep missing deadlines" is a symptom. The problem might be bad estimates, too many projects, unclear ownership, or one overloaded person; treat the symptom and it returns. "We need a new app" and "I need a new job" are solutions someone already picked. Ask what problem each is meant to solve, then check whether something else solves it better.

**Reframe at least once.** In the old slow-elevator story (often told, origin uncertain), tenants complained about waiting; instead of buying a faster elevator, the owner installed mirrors, and complaints dropped. The problem wasn't speed. It was boredom.

**Is / is not.** Charles Kepner and Benjamin Tregoe (*The Rational Manager*, 1965) taught specifying a problem by contrast: where, when, and how much it happens, against where, when, and how much it could happen but doesn't. The machine fails on the night shift, not the day shift. The fight happens on Sundays, not Saturdays. The difference points at the cause.

---

## Pólya's Four Steps

George Pólya's *How to Solve It* (1945) was written for mathematics students. Its method is general.

1. **Understand the problem.** What is unknown? What data do you have? What are the conditions? Restate it in your own words. Draw it.
2. **Devise a plan.** Have you seen a related problem? Can you solve part of it, a simpler version, or a special case? Can you work backward from the goal?
3. **Carry out the plan.** Execute carefully and check each step. If the plan fails, return to step 2, not to random effort.
4. **Look back.** Check the result. Could you reach it another way? What method can you reuse?

Most people skip steps 1 and 4. Skipping the first solves the wrong problem; skipping the last means solving the same kind of problem from scratch next time. Pólya's most useful single move: if you can't solve the problem, find a related, easier one you can solve, and start there.

---

## First Principles and Decomposition

**First principles** (the idea goes back to Aristotle) means reasoning from what you can verify rather than from convention or analogy.
1. Write down the conventional assumption: "this costs X," "this takes six months," "this is how it's done."
2. Break it into fundamentals: physical requirements, real input costs, hard constraints, the human need underneath.
3. Rebuild from those fundamentals and compare.

Use it on high-stakes problems where convention may be stale. Not on everything: it's expensive, and convention often encodes hard-won knowledge. G.K. Chesterton's fence (from *The Thing*, 1929): don't tear down a fence until you know why it was put up.

**Decomposition.** Split a big problem into pieces you can solve, test, or delegate.
- **Issue trees.** Break the question into sub-questions that don't overlap and together cover everything (MECE, a consulting staple associated with Barbara Minto). "Why are profits down?" splits into revenue and costs, then each into its parts.
- **Find the bottleneck.** Eliyahu Goldratt's *The Goal* (1984) and his Theory of Constraints: a system's output is set by its tightest constraint. Improving anything else is wasted until that one moves.
- **Estimate the unknowns.** Build a Fermi estimate when a number is missing; see [mental-models/decision-making.md](mental-models/decision-making.md).
- **Solve the smallest version first,** then scale.

---

## Root-Cause Analysis

**The 5 Whys.** Associated with Sakichi Toyoda and built into the Toyota Production System by Taiichi Ohno: ask why the problem happened, then why that happened, until you reach a cause you can fix. Five is a rule of thumb, not a quota.
- You're late every morning. *Why?* You leave late. *Why?* You hunt for keys and bag. *Why?* They have no fixed place. *Why?* You come home tired and drop things anywhere. Fix: a hook and a tray by the door, not "try harder."

**Its limits.** It assumes a single chain, when most failures have several contributing causes, and it stops where the asker's knowledge stops. If the chain ends at "someone made a mistake," keep going: why did the system let one mistake through? James Reason's Swiss cheese model makes the point: accidents happen when holes in several layers of defense line up.

**The fishbone diagram.** Kaoru Ishikawa, a pioneer of Japanese quality control, drew the problem as a fish's head and the categories of cause as its bones. Manufacturing uses people, methods, machines, materials, measurement, and environment. For personal problems, try body, mind, environment, people, systems, and money. Brainstorm causes under each, then test the likeliest. A root cause is a hypothesis: if it's right, removing it should stop the problem. Verify before you declare victory.

---

## Inversion and Working Backward

**Inversion.** Carl Jacobi's advice to invert, made famous by Charlie Munger: instead of asking how to succeed, ask how you'd guarantee failure, then avoid that. Ask what would make the problem worse, and check whether you're already doing it. Full treatment in [cross-domain-thinking.md](cross-domain-thinking.md).

**Working backward.** Start at the goal and ask what must be true just before it, then just before that, until you reach the present. Mazes are easier from the exit. Amazon's version: write the press release and FAQ for a product before building it, to force clarity about what the customer gets. Its mirror image is the pre-mortem: assume the solution failed, explain why, and fix those causes first (see [decision-journal.md](decision-journal.md)).

---

## Constraints as Tools

**Sort your constraints.** Hard constraints are physics, law, and real deadlines. Soft constraints are budgets and preferences that bend at a price. False constraints are habits and assumptions nobody has checked. Many stuck problems are stuck on a false one.

**Remove them to see.** Ask what you'd do with unlimited money, time, or permission. Then bring the real constraints back one at a time and see which ideas survive.

**Add them to create.** On Apollo 13 (1970), engineers on the ground had to fit square carbon dioxide filters into round sockets using only what was aboard; they improvised an adapter from items like plastic bags, cardboard, and duct tape, and the crew built it. Dr. Seuss wrote *Green Eggs and Ham* on a bet that he couldn't write a book with only 50 different words. Try it: solve the problem in a day, with no budget, or with half the people.

---

## Analogy and Cross-Domain Transfer

Many hard problems have been solved before, somewhere else. The skill is noticing.

**Transfer isn't automatic.** Mary Gick and Keith Holyoak (1980) gave people Karl Duncker's radiation problem: destroy a tumor with rays that also destroy healthy tissue at full strength. The answer is several weak rays converging from different angles. People who had just read a story with the same structure (an army splitting up to converge on a fortress) mostly still failed, until told the story might help. Then most solved it.

**So ask deliberately:**
- What is the structure of this problem without its surface details? Allocation, bottleneck, coordination, search, trust?
- Who else faces that structure? Militaries, hospitals, ecosystems, sports teams, other industries.
- How did they solve it, and what would that look like here?

**Break functional fixedness.** In Duncker's candle problem, people struggle to see a box of tacks as a shelf because they see it as a container. List the parts of your problem and what else each could be. Then widen the range of structures you know: [cross-domain-thinking.md](cross-domain-thinking.md), [polymath-system.md](polymath-system.md).

---

## Explain It Out Loud

**Rubber-duck debugging.** *The Pragmatic Programmer* (Andrew Hunt and David Thomas, 1999) describes programmers explaining their code, line by line, to a rubber duck. Forcing each step into words exposes the step you skipped. Research on self-explanation (Michelene Chi and colleagues) points the same way: learners who explain material to themselves understand it better.

**Practice:** When stuck, explain the problem from the beginning, aloud or in writing, to someone who knows nothing about it. Often you'll hear the answer before you finish. See [writing.md](writing.md).

**Step away, deliberately.** After real effort, a break can help: a 2009 meta-analysis (Sio and Ormerod) found a modest incubation benefit. Load the problem fully first, then walk, sleep, or switch tasks, then return.

---

## Satisficing vs. Maximizing

Herbert Simon coined "satisficing" in 1956: instead of searching for the best possible option, set criteria for good enough and take the first option that meets them. Real minds have limited time, information, and computing power (his "bounded rationality"), so satisficing is often the rational response, not a lazy one. Simon won the 1978 Nobel prize in economics. Barry Schwartz and colleagues (2002) later found that people who score as maximizers report less happiness and more regret than satisficers. The data are correlational, but the pattern matches experience.

**The rule:** Maximize on one-way doors: career moves, partners, houses, large irreversible bets. Satisfice on everything else. Write your good-enough criteria before you start looking, and stop when an option meets them.

---

## Tame vs. Wicked Problems

Horst Rittel and Melvin Webber ("Dilemmas in a General Theory of Planning," 1973) separated tame problems from wicked ones.

**Tame:** a clear definition, a clear stopping point, and a solution you can test as right or wrong. Fixing a leak, solving an equation, debugging a crash.

**Wicked:** no definitive formulation (how you define it shapes the solution); no stopping rule; solutions are better or worse, not right or wrong; every attempt changes the situation, so there are no free trial runs; each case is essentially unique; and each problem can be seen as a symptom of another. Social policy is their home ground. In a life: a strained marriage, a teenager in trouble, a career that has lost its meaning.

**How to work them:**
- Don't wait for a complete definition; it won't come. Act, observe, adjust. Dave Snowden's Cynefin framework calls this probe, sense, respond.
- Involve the people who live inside the problem; they hold part of the definition.
- Aim for better, not solved. Revisit on a schedule.

**The two errors:** treating a wicked problem as tame (engineering a fix for a relationship), and treating a tame problem as wicked (philosophizing about a flat tire).

---

## Run Small Experiments

When you don't know what will work, buy information cheaply. Jim Collins and Morten Hansen (*Great by Choice*, 2011) call it firing bullets, then cannonballs: cheap, low-risk tests first, then concentrate resources on what's proven.

1. **Hypothesis:** if I do X, Y should change by about Z.
2. **Smallest test:** the cheapest, fastest, most reversible version.
3. **Measure:** decide what you'll look at before you start.
4. **Kill criteria:** the result that means stop.
5. **Time box:** when you'll judge it.

This is the Plan-Do-Check-Act cycle that Walter Shewhart and W. Edwards Deming spread through quality management. For experiments on yourself (diet, sleep, training), change one thing at a time, run it long enough to see past normal variation, and remember regression to the mean. See [scientific-thinking.md](scientific-thinking.md).

---

## When to Stop or Escalate

**Set a time box at the start,** based on what solving the problem is worth. When it's spent, choose deliberately: continue with a new budget, change approach, escalate, or accept the problem.

**Escalate when:**
- You've passed your time box with no new information.
- The decision exceeds your authority, or the downside exceeds what you can absorb.
- It's irreversible and outside your competence.
- Safety, health, legal, or serious financial risk is involved. Bring in a qualified professional; a general method doesn't replace specialist judgment.

**Escalate well:** what you're trying to do, what you tried, what happened, and exactly what you need. One clear message, not "it's not working."

**Stop when** further work costs more than a better answer is worth, when a good-enough solution exists, or when the problem has dissolved. Past effort is not a reason to continue; see sunk cost in [cognitive-biases.md](cognitive-biases.md).

---

## The Protocol

1. **Name it.** One sentence: what's wrong.
2. **Write the problem statement:** current state, desired state, gap, constraints, done-looks-like.
3. **Classify it.** Tame or wicked? Reversible or one-way? What is solving it worth? Set the time box.
4. **Understand it.** Separate facts from assumptions. Run is / is not. Gather the missing data.
5. **Find the cause.** 5 Whys, fishbone. Verify the cause before treating it.
6. **Generate at least three options,** including "do nothing." Use first principles, decomposition, analogy, inversion, working backward, and shifted constraints.
7. **Choose.** Set criteria first. Satisfice or maximize based on stakes and reversibility.
8. **Test small** where you can, with kill criteria.
9. **Execute,** checking each step.
10. **Look back.** Did it work? Why? What generalizes? Log it in your [decision journal](decision-journal.md).

---

## One-Page Template

```
PROBLEM:                           DATE:          OWNER:
TIME BOX:                          WORTH SOLVING BECAUSE:

1. DEFINE
   Current state (facts):
   Desired state (measurable):
   Gap:
   Constraints (hard / soft / possibly false):
   Done looks like:
   Type: tame / wicked        reversible / one-way

2. UNDERSTAND
   Is:                         Is not:
   Facts:                      Assumptions to check:

3. CAUSE
   Why > Why > Why > Why > Why:
   Other contributing causes:
   How I'll confirm the cause:

4. OPTIONS (at least three, including do nothing)
   A:            B:            C:
   Inversion (how would I guarantee failure?):
   Analogy (who has solved this structure before?):

5. CHOOSE AND TEST
   Criteria (set before choosing):
   Choice and why:
   Smallest test:              Kill criteria:
   Escalate if:

6. LOOK BACK (date: ____)
   What happened / what worked / lesson that generalizes:
```

---

## Cross-References

- Choosing among options: [mental-models/decision-making.md](mental-models/decision-making.md)
- Inversion and the latticework: [cross-domain-thinking.md](cross-domain-thinking.md)
- Where small effort moves big systems: [leverage-points.md](leverage-points.md)
- Testing claims and self-experiments: [scientific-thinking.md](scientific-thinking.md)
- The biases that derail problem solving: [cognitive-biases.md](cognitive-biases.md)
- Recording and reviewing decisions: [decision-journal.md](decision-journal.md)
