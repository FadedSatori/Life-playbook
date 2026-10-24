# Scientific Thinking

Science is the best error-correcting method humans have built. But you almost never meet science directly. You meet it through headlines, press releases, podcasts, supplement labels, and self-help books, and each step strips out caveats and adds certainty. By the time a finding reaches you, it may be something the original authors would not recognize.

When this playbook was fact-checked, roughly 150 errors turned up: invented precision, quotes pinned on famous people who never said them, and findings that had already failed to replicate. None of it was malicious. All of it came from trusting the retelling instead of going to the source.

This file is the defense. Richard Feynman set the standard in his 1974 Caltech commencement address, "Cargo Cult Science": "The first principle is that you must not fool yourself — and you are the easiest person to fool."

---

## How Science Actually Works

**Conjecture and refutation.** Karl Popper (*The Logic of Scientific Discovery*, German original 1934) argued that a scientific claim must be falsifiable: it must forbid something, so that some possible observation could prove it wrong. A thousand white swans can't prove all swans are white; one black swan refutes it. A theory that explains every possible outcome explains nothing.

**The complication.** Real tests rest on auxiliary assumptions (the instrument worked, the sample was clean), so one failed prediction doesn't automatically kill a theory. Neither one confirmation nor one refutation settles much. Patterns across many tests do.

**Replication is the filter.** A single study is a data point, not a fact. A finding becomes knowledge when independent teams, using different samples and ideally different methods, keep getting it.

**Self-correcting, slowly.** Science corrects itself at the level of the system, not the individual paper. John Ioannidis's 2005 essay "Why Most Published Research Findings Are False" (*PLoS Medicine*) argued from modeling that small studies, small effects, flexible analyses, and hot fields push the share of false findings very high. It is an argument about conditions, not a measured rate, but replication projects since then have found serious problems in several fields.

**Your working scale:**
- One new study: a hypothesis worth watching.
- Replicated by independent groups: provisional knowledge.
- Consistent across methods, populations, and decades: as close to settled as science gets. Still revisable.

---

## The Hierarchy of Evidence

The usual ladder, roughly from weakest to strongest, and how each rung misleads:

| Level | What it is | How it misleads |
|-------|-----------|-----------------|
| Anecdote, testimonial | "It worked for me" | Placebo, natural recovery, regression to the mean; you only hear from people it worked for |
| Expert opinion | A credentialed person's view | Authority is not evidence; expertise doesn't transfer outside a field |
| Lab studies | Cells in a dish, animals | Doses and biology often don't carry over to humans (see below) |
| Case reports and series | Detailed accounts of a few patients | No comparison group |
| Observational studies | Cohort, case-control, cross-sectional: watch people, compare groups | Confounding, reverse causation, self-report error; shows association, not cause |
| Randomized controlled trials | Random assignment to treatment or control | Can be small, short, run in unrepresentative people, measure proxies, or be funded by interested parties |
| Systematic reviews, meta-analyses | Pooled results of all relevant studies | Garbage in, garbage out; publication bias; pooling unlike studies; rival meta-analyses can disagree |

**The ladder is a heuristic, not a law.** The case against smoking was built largely on observational studies (Richard Doll and Austin Bradford Hill, from 1950 on), and it was right. Many questions can't ethically be randomized. Bradford Hill's 1965 considerations help judge observational evidence: strength, consistency, temporality (cause before effect), dose-response, plausibility, and coherence with other evidence.

**When observation got it wrong.** Observational studies suggested hormone replacement therapy protected women's hearts; the Women's Health Initiative trial (2002) found no such protection and some added risks, at least in the older women it studied. HRT users had tended to be healthier and better off to begin with. Observational data linked beta-carotene to less lung cancer; trials in smokers (ATBC in 1994, then CARET) found more. That is confounding, and it is why trials matter.

---

## Correlation Is Not Causation

When two things move together, there are several explanations, and "A causes B" is only one.

1. **Confounding.** A third factor drives both. Ice cream sales and drownings rise together because of summer. People who take vitamins also tend to exercise, eat well, and see doctors (the healthy-user effect), so they look healthier whatever the vitamins do.
2. **Reverse causation.** B causes A. In older alcohol studies, "non-drinkers" included people who had quit because they were already ill, which flattered moderate drinkers by comparison (the sick-quitter problem).
3. **Selection effects.** How the sample was chosen creates the pattern. If you only date people who are attractive or kind, the two traits will look opposed in your dating history even if they're unrelated in the population. Studying only survivors, patients, or winners does the same.
4. **Chance.** Test enough variables and some will correlate by luck. Tyler Vigen's collection of spurious correlations (cheese consumption tracking deaths by bedsheet entanglement) makes the point.
5. **Causation,** sometimes running both ways.

**The questions that separate them:** Was exposure randomly assigned? What else differs between the groups? Which came first? Does more exposure mean more effect? Is there a plausible mechanism? Does it hold across different populations and designs?

---

## Signal, Noise, and Significance

**Statistical significance is not importance.** "Significant" means the result would be surprising if there were no effect. It says nothing about whether the effect is big enough to matter. With a large enough sample, a trivial difference becomes significant.

**Ask for the effect size,** in units you care about: kilograms, minutes, years of life. Psychologists often use Cohen's d, where Jacob Cohen offered 0.2, 0.5, and 0.8 as small, medium, and large, and warned these were rough conventions. A supplement that "significantly" lowers blood pressure by 1 mmHg is real and nearly useless.

**What a p-value is:** the probability of getting data at least as extreme as what was observed, if there were truly no effect and the model's assumptions held. **What it is not** (spelled out in the American Statistical Association's 2016 statement):
- Not the probability that the hypothesis is true.
- Not the probability that the result was produced by chance alone.
- Not a measure of the size or importance of an effect.
- Not a truth switch at 0.05. That line is a convention; 0.049 and 0.051 are nearly the same evidence.

**Prefer confidence intervals.** An effect of 5 with an interval from 4 to 6 is informative. An effect of 5 with an interval from -1 to 11 means the study doesn't know much.

**Small samples are noisy in both directions.** In *Thinking, Fast and Slow*, Kahneman describes how the US counties with the lowest kidney cancer rates are mostly rural and sparsely populated, and so are the counties with the highest. Small populations produce extreme rates by chance. Likewise, the most dramatic results tend to come from the smallest studies, and they tend to shrink on replication.

**Regression to the mean.** Extreme measurements tend to be followed by more ordinary ones. People try a remedy when symptoms peak, improve anyway, and credit the remedy. Any before-and-after claim without a control group has this problem.

**Forking paths.** If researchers can pick outcomes, subgroups, and cutoffs after seeing the data, they can find "significance" almost anywhere. Joseph Simmons, Leif Nelson, and Uri Simonsohn showed this in 2011 by using common flexible practices to "find" that listening to "When I'm Sixty-Four" made people younger. Andrew Gelman calls this the garden of forking paths.

---

## Risk: Relative, Absolute, and Base Rates

**Headlines use relative risk; decisions need absolute risk.** Suppose a drug cuts the risk of a disease from 2 in 1,000 to 1 in 1,000. The press release says "halves your risk." The absolute reduction is 0.1 percentage points: about 1,000 people take the drug for one to benefit. That number needed to treat belongs beside the number needed to harm. Always ask: out of how many?

**Base rates decide what a positive test means.** Take a condition affecting 1 in 100 people and a test that catches 90% of cases but also flags 9% of healthy people. Of 1,000 people tested:
- 10 have the condition; 9 test positive.
- 990 don't; about 89 test positive anyway.
- Of roughly 98 positives, only 9 are real: about 1 in 11.

The numbers are illustrative; the structure is how real screening works. Gerd Gigerenzer's research shows that people, physicians included, reason far better when probabilities are restated as natural frequencies like these. Do it yourself: convert every percentage into "out of 1,000 people." More in [mental-models/probabilistic-thinking.md](mental-models/probabilistic-thinking.md). Use this to ask your clinician better questions, not to self-diagnose.

---

## The Replication Crisis

In 2015 the Open Science Collaboration, coordinated by Brian Nosek, published attempts to replicate 100 studies from three leading psychology journals (*Science*, 2015). About 97% of the originals had reported significant results; about 36% of the replications did. Judged subjectively, about 39% replicated. On average, effects came in at roughly half their original size.

It isn't only psychology. In 2012, scientists at the biotech firm Amgen reported confirming the findings of only 6 of 53 "landmark" preclinical cancer studies (Begley and Ellis, *Nature*), though they did not publish full details.

**Why it happened:** publication bias (null results left in file drawers, a problem Robert Rosenthal named in 1979); small samples chasing small effects; flexible analysis and selective reporting; HARKing (hypothesizing after the results are known); and incentives that reward novelty over accuracy.

**The fixes, and what to look for:**
- **Preregistration:** hypotheses, outcomes, and analysis plan filed publicly before data collection. Leading medical journals have required clinical trial registration since 2005.
- **Registered Reports:** journals review the question and method before results exist and commit to publish either way.
- **Large multi-lab replications** and open data.

A preregistered, well-powered study whose primary outcome matches its registration deserves far more trust than a small, surprising, unregistered one.

**Findings that didn't hold up** (all still circulate as settled fact):
- **Ego depletion** (willpower as a tank that runs dry): a preregistered replication across more than 20 labs (Hagger et al., 2016) found an effect near zero. Still debated; don't build on it.
- **Power posing:** the hormonal effects didn't replicate (Ranehill et al., 2015), and co-author Dana Carney said in 2016 she no longer believes the effects are real. Effects on feeling powerful are weaker and still argued over.
- **10,000 hours:** Malcolm Gladwell's *Outliers* (2008) popularized K. Anders Ericsson's research as a threshold; Ericsson objected. A 2014 meta-analysis (Macnamara, Hambrick, and Oswald) found deliberate practice explained a minority of performance differences, from about a quarter in games to under 1% in professions.
- **21 days to form a habit:** Lally and colleagues (2010) found a median of about 66 days, with a range of roughly 18 to 254.
- **Mehrabian's 7-38-55:** from narrow 1960s experiments on single words conveying feelings. Mehrabian has said it doesn't apply to communication in general.
- **Learning styles:** a 2008 review (Pashler and colleagues) found little good evidence that matching teaching to a preferred style improves learning.
- **The marshmallow test as destiny:** a larger 2018 replication (Watts, Duncan, and Quan) found a much weaker link to later achievement, shrinking further after accounting for family background.
- **The backfire effect** (corrections strengthening false beliefs): large studies (Wood and Porter, 2019) found it rare.
- **"We use 10% of our brains":** a myth.

---

## Animal and Cell Studies

**In a dish.** Plenty of things kill cancer cells in a petri dish, including bleach and heat. The question is whether a safe dose, delivered through a human body, does anything at the target.

**In mice.** Mice differ in metabolism, lifespan, and disease; lab strains are inbred and tightly controlled; doses often far exceed human equivalents. Many promising animal results never translate, and roughly nine in ten drugs that enter human trials never win approval.

**Mechanism is not outcome.** In the Cardiac Arrhythmia Suppression Trial (1989), drugs that suppressed abnormal heartbeats on monitors *increased* deaths. Biomarkers are proxies. What matters is whether people live longer and better.

**Rule:** "in mice" or "in cells" means interesting, not actionable. Wait for human trials with outcomes that matter.

---

## How Findings Get Distorted

The chain runs: paper, press release, news story, social post, podcast, your friend. Each link adds certainty and drops caveats.

**It often starts with the institution.** Sumner and colleagues (*BMJ*, 2014) examined 462 health press releases from 20 UK universities. About 40% contained exaggerated advice, 33% exaggerated causal claims from correlational data, and 36% exaggerated human relevance from animal work. When the release exaggerated, the news usually did too.

**Decode the headline:**
- "Linked to" or "associated with": correlation.
- "May," "could," "might": speculation.
- "Study finds": one study. "Scientists say": possibly one scientist.
- "Breakthrough," "miracle," "cure": marketing.

**One study, long shadow.** Andrew Wakefield's 1998 *Lancet* paper linking the MMR vaccine to autism described 12 children, was found to be fraudulent, and was retracted in 2010. Large studies since have found no link. The fear outlived the paper by decades.

---

## How to Read a Study: The Checklist

1. **Does it exist, and does it say what's claimed?** Find the actual paper: authors, journal, year. Many claims fail here.
2. **Who or what was studied?** Cells, animals, or humans? How many? What age, sex, health?
3. **What design?** Trial, cohort, case-control, cross-sectional, review?
4. **Compared to what?** Is there a control group? Placebo? Were participants and assessors blinded?
5. **What was measured?** Hard outcomes (death, fractures, disease) or proxies (biomarkers, self-report)?
6. **How big is the effect,** in absolute terms, with what confidence interval?
7. **Was it preregistered,** and does the reported primary outcome match the registration?
8. **How many outcomes and subgroups were tested?** Is the headline result one of many?
9. **How long did it run?** Long enough for the outcome to matter?
10. **Who paid,** and what conflicts do the authors declare?
11. **Does it fit the larger body of evidence?** Look for systematic reviews (Cochrane is a good start).
12. **Has it replicated? Has it been corrected or retracted?** (Retraction Watch keeps a database.)
13. **Read the limitations section.** It is often the most honest paragraph in the paper.

Reading order: abstract, methods, results tables, limitations, then discussion last. The discussion is where authors sell.

---

## Red Flags in Health and Self-Help Claims

- **Precise numbers with no source** ("boosts testosterone 43%"). Real research comes with intervals and citations.
- **A quote from a famous person with no source.** Check Quote Investigator before repeating it.
- **One study,** especially if small, new, or in animals.
- **Testimonials and before-and-after photos** in place of data.
- **The source sells the product,** or the course, or the supplement.
- **Suppression stories:** "what doctors don't want you to know."
- **Vague mechanisms:** detox, boosts immunity, balances hormones, quantum anything, neuro-jargon used as decoration.
- **One cure for many unrelated problems.**
- **Credentials from another field.**
- **"Natural" offered as proof of safety.**
- **Unfalsifiable framing:** if it didn't work, you didn't do it right.
- **A big effect from a tiny intervention.** Carl Sagan: "Extraordinary claims require extraordinary evidence."

For anything touching medication, diagnosis, or treatment, take the claim to a qualified clinician. See [health/health-intelligence.md](health/health-intelligence.md).

---

## Verify a Claim in Five Minutes

Mike Caulfield's SIFT method, built on lateral reading research (see [intelligence-tradecraft.md](intelligence-tradecraft.md)):

1. **Stop.** Notice your reaction. Strong emotion or a perfect fit with what you already believe is a reason to slow down.
2. **Investigate the source.** Leave the page. Search who is behind it and what independent sources say about them.
3. **Find better coverage.** Search the claim plus "study," "fact check," or "systematic review." See what trustworthy sources report.
4. **Trace to the original.** Find the primary study, dataset, or text (PubMed, Google Scholar, the journal itself). For quotes, find the original speech or book. If you can't find the source, treat the claim as unverified.

Then write it down with the confidence it has earned: "one small trial suggests," "observational studies associate," "well established." If a number or attribution can't be traced, cut it or flag it. Precision you can't source is decoration.

---

## Cross-References

- Manipulation and memetic defense: [epistemic-self-defense.md](epistemic-self-defense.md)
- Source evaluation and lateral reading: [intelligence-tradecraft.md](intelligence-tradecraft.md)
- Base rates and Bayesian updating: [mental-models/probabilistic-thinking.md](mental-models/probabilistic-thinking.md)
- The biases that make bad evidence persuasive: [cognitive-biases.md](cognitive-biases.md)
- Reading health data and working with clinicians: [health/health-intelligence.md](health/health-intelligence.md)
- Reading for understanding: [learning/reading-system.md](learning/reading-system.md)
- Keeping score on your own judgment: [decision-journal.md](decision-journal.md)
