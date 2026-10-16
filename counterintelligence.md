# Counterintelligence

Counterintelligence is the discipline of protecting information, people, and operations from adversaries who want them. Governments built it to stop foreign services. The same logic applies at civilian scale: a competitor who wants your client list, a fraudster who wants your money, an acquaintance who collects your weak points, a former partner who knows your routines.

Most of this is not exotic. It is the habit of asking who wants what you have, how they would get it, and what it would cost you. Then closing the cheapest doors first.

This file is defensive. It teaches you to recognize and resist elicitation, manipulation, and insider risk, using public guidance and published history. It does not teach you to surveil, track, or recruit anyone. For the analytic side, see [intelligence-tradecraft.md](intelligence-tradecraft.md). For the history behind these lessons, see [intelligence-history.md](intelligence-history.md).

---

## What Counterintelligence Is

**Security protects. Counterintelligence thinks about the opponent.** Security is locks, passwords, and policies. Counterintelligence asks who is trying to get past them, what they already know, and what they are likely to try next. A lock without a threat model is decoration.

Professionals describe three parts:

1. **Defense:** reduce what an adversary can learn or reach. Limit access, limit disclosure, harden the people and systems that matter.
2. **Offense:** actively engage the adversary's operations. This belongs to governments and is lawful only for them. It is not your job and it is not in this file.
3. **Analysis:** study how adversaries behave, what they have gotten right before, and where your own gaps are.

For a civilian, defense and analysis are the whole game. Your analysis is a short, honest look at your own exposure. Your defense is a handful of habits.

---

## Threat Modeling in Plain Terms

You cannot protect everything, and trying to makes you paranoid and ineffective. Decide what matters.

**Four questions:**

1. **Assets.** What do I have that someone else would value? Money and account access, client or customer data, unreleased plans, intellectual property, my schedule and location, my family's information, my reputation, my health and legal details.
2. **Adversaries.** Who might want it? Opportunistic criminals (the most common by far), competitors, a disgruntled employee or ex-partner, a business counterparty, a stalker, a hostile state if you work in a sensitive field. Most people face only the first few.
3. **Capabilities and methods.** How would they realistically get it? Phishing, a phone call posing as your bank, a friendly stranger asking questions, a shared password, an unlocked laptop, an employee with too much access. Rank by likelihood, not drama.
4. **Consequences.** What happens if they succeed? Rank by damage and by reversibility. A leaked email address is an annoyance. A drained account or a leaked client file is not.

**Then prioritize:** high likelihood and high damage first. Cheap, boring fixes (unique passwords, two-factor authentication, verifying odd requests) usually beat elaborate measures. Write it on one page and revisit it when life changes.

**Proportion rule.** Scale protection to what is at stake and who realistically wants it. Overbuilding is its own failure.

---

## The Human Factor

The recurring finding across public breach reports and espionage histories is that people, not technology, are the weak point. Industry breach studies such as the Verizon Data Breach Investigations Report have consistently attributed a large majority of breaches (roughly two-thirds or more in recent editions) to a human element: phishing, stolen credentials, errors, misuse. Treat the exact figure as approximate, but the direction is not in doubt.

People are the entry point because we are polite, trust by category (title, school, shared hobby), act under urgency, talk to feel connected, and carry pressure points that can be pushed.

The fix is not distrust of everyone. It is verification where the stakes are high, and silence where the other person does not need to know. See [epistemic-self-defense.md](epistemic-self-defense.md) and [cognitive-biases.md](cognitive-biases.md).

---

## How Approaches Are Framed: MICE

US counterintelligence training and public writing often use the mnemonic **MICE** to explain why people are drawn into helping an adversary:

- **Money:** debt, greed, lifestyle pressure, a sense of being underpaid.
- **Ideology:** belief in a cause or opposition to one's own side.
- **Coercion / Compromise:** leverage over a secret, a vulnerability, or a threat to someone the person loves.
- **Ego:** the need to feel important, recognized, or vindicated; resentment at being passed over.

**Use it carefully.**

- The origin of the acronym is murky. Sources variously credit US counterintelligence, the FBI, or a Soviet-era formulation. Do not repeat a confident attribution.
- Real motives are mixed and shift over time.
- Critics say MICE describes surface labels rather than root causes. A common alternative view is that ego-type injuries (feeling unrecognized, wronged, or small) sit under many of the other categories.
- It is a lens for self-examination and for understanding how a manipulator thinks. It is not a profile for diagnosing coworkers. Plenty of people with debts or grievances never do anything wrong.

**Defensive use on yourself:** list your own pressure points, honestly and privately. Debt, an unrecognized contribution, a secret you fear exposed, a cause you feel strongly about. Anyone running a manipulation, from a romance scammer to a recruiter-for-hire, will look for exactly these. Knowing yours makes you harder to move. The government version of this advice, including the NCSC's "Think Before You Link" campaign on fake professional-network approaches, applies directly to career and online life.

**Typical shape of a recruitment-style approach:** a friendly contact appears; builds rapport; flatters your expertise; asks small, harmless favors; offers something (a consulting fee, a paid talk, a "job interview," a trip); and gradually asks for more specific or sensitive information while making the relationship feel valuable. The tell is not any single step. It is a pattern of escalating requests combined with reluctance to be transparent about who they are and who is paying.

---

## Elicitation: Recognize and Deflect

Elicitation is getting information from someone through ordinary-seeming conversation, without them realizing what has been extracted. Public FBI guidance describes it as discreet collection of information not otherwise publicly available, and gives a recognizable set of techniques. Salespeople, journalists, recruiters, and competitors use versions of these. So do honest friends, often without any bad intent. Recognition is not accusation.

**Common techniques (as described in public FBI-type guidance):**

- **Flattery:** praise your expertise so you prove it by explaining.
- **Deliberate false statement:** say something wrong so you correct it with the truth.
- **Quid pro quo:** share something first so you feel obliged to match it.
- **Bracketing:** offer a high and low estimate so you narrow to the real number.
- **Feigned ignorance:** pretend not to know a topic so you teach it.
- **Assumed knowledge:** talk as though both of you already know the detail, so confirming or adding to it feels natural.

**Deflection that is honest and legal:**

1. **Answer a different question.** Reply to the safe version of what was asked.
2. **Redirect.** "That's outside my area. What are you working on?"
3. **Ask "why do you ask?"** Said lightly, it often ends the line of questioning or reveals the purpose.
4. **Defer to authority or policy.** "I'd need to check with legal," "Our policy covers that." This is true and unarguable.
5. **Be vague on purpose.** "It depends" and "I haven't thought about it" are honest and give nothing.
6. **Say nothing.** A pause is allowed. Most people fill silence; you do not have to.
7. **Leave.** You may end any conversation.

**Rules of thumb.** You do not have to lie; declining to answer is not lying. Do not correct strangers who misstate your work. Before any conference or networking event, decide in advance what you will not discuss. Notice who circles the same topic from different angles.

See [counter-strategies.md](counter-strategies.md) and [tactics/social.md](tactics/social.md).

---

## Insider Risk

An insider is anyone with legitimate access: an employee, contractor, partner, vendor, family member, or friend with your passwords. Most harm from insiders is not dramatic spying. It is theft, fraud, data loss through carelessness, and quiet resentment turned into action.

**The core idea in public frameworks is a combination.** Harm needs **access**, **motive**, and **opportunity**. A related idea from criminologist Donald Cressey's work on fraud is the "fraud triangle": pressure, opportunity, and rationalization. You usually cannot see motive. You can control access and opportunity.

**Controls that work without suspicion:** least privilege (only the access the job requires); need to know; separation of duties (no one both initiates and approves money movement); trust but verify, applied to everyone including you, which makes it no insult; prompt offboarding (many incidents start with an unclosed account); and clear channels to raise concerns.

**Indicators in public frameworks** (the US National Insider Threat Task Force and similar bodies publish them) include unexplained financial stress or affluence, repeated policy violations, unusual access outside role, serious unresolved grievances, and sudden changes in behavior. Any one of these is weak evidence, since each has innocent explanations. Look for patterns and use them to start a conversation or a quiet check by the right person, not to convict.

**The danger of overcorrecting.** Witch-hunts destroy trust, drive out the good people, and often miss the real problem. Never act on a hunch alone. Never share suspicions casually. Escalate facts to the proper authority and let a process decide. See [leadership.md](leadership.md) and [community.md](community.md).

---

## Compartmentation and Need-to-Know

Compartmentation means limiting what each person or system knows so that one failure cannot expose everything.

**In a small business:** separate the keys (banking, admin, client data, vendor payments) so no one person or login holds all of them; give people what their job requires; use a shared password manager with role-based access; list who has what access and update it quarterly; and have a second person verify any change to payment details, since invoice-redirect fraud depends on one person acting on one email.

**In a household:** decide what children, guests, and extended family should not have (financial details, alarm codes, travel dates). Teach the call-back rule: anyone asking for money or codes, even in a familiar voice, is verified through a second channel.

**Limit:** compartmentation has costs. Over-restricting information slows work and builds resentment. History shows the opposite failure too: stove-piping where nobody connects the dots. Share on purpose, with the right people. See [intelligence-history.md](intelligence-history.md).

---

## Vetting People and Partners

Vetting is due diligence on someone who will have access to your money, information, or reputation. It must stay within the law and proportion. Public sources and references only. See [intelligence-tradecraft.md](intelligence-tradecraft.md) for the full open-source method.

**Checks that are legitimate and effective:**

- Verify identity, registration, and licenses through official registries.
- Check court records and regulatory actions where public.
- Take references from people you found independently, not just those the person offered.
- Test **consistency:** does the story told to you match what they told others, their résumé, their profile, and public records?
- Look for **verifiable specifics** rather than polish.
- For employees, use lawful background screening with consent, following the rules in your jurisdiction.
- Watch behavior over time, especially under small tests: promises kept, details accurate, boundaries respected.

**Red flags:** pressure to move fast or keep it secret, reluctance to be verified, a story that changes, flattery that precedes a request, offers too good for the effort.

---

## The Limits of Detecting Deception

Do not trust your ability to read liars.

- A large meta-analysis by Bond and DePaulo found people detect lies at about 54 percent accuracy, barely above chance. Common cues like gaze aversion do not reliably separate truth from lies.
- The polygraph is scientifically contested; a 2003 National Research Council review found limited evidence of accuracy, especially for screening. Aldrich Ames reportedly passed polygraphs while spying.

**What works better:** verify claims against documents and third parties; look for inconsistency over time; ask for specifics and check them; watch what incentives the person has; and design systems so that you do not need to trust anyone's face. Control access and verify, rather than reading minds.

---

## Managing Your Footprint

What adversaries cannot get from you, they try to get about you. Your accounts, posts, public records, and connections form a map.

Assume anything online is permanent, searchable, and combinable. Search yourself for an hour as a stranger would, then shrink what is public about your family, routines, and employer.

The full protocol is in [opsec-and-privacy.md](opsec-and-privacy.md). For physical safety, see [personal-security.md](personal-security.md).

---

## If You Think You Are Being Targeted

**Do not confront, and do not retaliate.** Confronting warns the person, escalates risk, and can expose you legally.

1. **Document.** Save messages, emails, dates, and details. Write a plain timeline: what happened, when, and who was involved. Facts, not theories.
2. **Stop sharing.** Say nothing more about the topic. Do not play along to learn more.
3. **Tell the right person.** At work: your employer's security or compliance contact, in writing. In business: your lawyer. At home: someone you trust who can give you a second view.
4. **Report where appropriate.** Local police for harassment, stalking, threats, or fraud. For US persons, matters that look national-security-related, such as an approach by someone who seems to be seeking sensitive information or recruiting, go to the FBI (tips.fbi.gov or 1-800-CALL-FBI). Online fraud can go to the FBI's IC3 (ic3.gov).
5. **Secure the basics.** Change passwords, enable multi-factor authentication, review account access.
6. **Check your reading.** Most oddities have boring explanations; list alternatives first.
7. **Immediate danger:** call emergency services.

---

## The Ethics Line

Counterintelligence is a defensive craft. It does not give you license.

- **No spying on friends or family.** Reading a partner's messages or covertly monitoring someone's device is a betrayal and often illegal. Open, agreed controls for minor children are different.
- **Know the law.** Recording and account-access rules vary by place; unauthorized access is a crime in many jurisdictions.
- **Proportion.** A hunch is not evidence.
- **No vigilantism.** Take real threats to those authorized to act.
- **Honesty.** Declining to share is fine. Lying, impersonating, or manipulating to get information is not. See [ethics.md](ethics.md) and [warrior-codes.md](warrior-codes.md).

A person who defends well and treats others honestly keeps both his security and his integrity.

---

## One-Page Personal Counterintelligence Checklist

1. I have written my assets, adversaries, methods, and consequences on one page.
2. I know my pressure points and have decided what I will not discuss with new contacts.
3. I verify unusual requests for money, access, or information through a second channel.
4. I answer probing questions with deflections and I do not correct false statements.
5. Each person with access to my money, data, or systems has the minimum they need.
6. No one controls every critical function without a check; my key accounts use unique passwords and multi-factor authentication.
7. I have looked at what a stranger can find about me and trimmed it.
8. I vet new partners and hires with independent references and public records.
9. I escalate concerns to the right person with documentation, not to rumor.
10. I have not spied on anyone I should trust.

---

## Quarterly Review

Set a 60-minute block each quarter.

1. **Update the threat model** for any new job, project, relationship, or attention.
2. **Audit access** to your accounts, files, and money; remove what is stale.
3. **Review the footprint** and old accounts.
4. **Review near-misses:** odd emails, strange questions, requests that felt wrong.
5. **Test one control:** call-back verification, backup restore, or a password reset.
6. **Check yourself** for over-sharing and for paranoia.
7. **Log it** in your [decision-journal.md](decision-journal.md) so the pattern is visible over time.

---

## Cross-References

- Analysis and source evaluation: [intelligence-tradecraft.md](intelligence-tradecraft.md)
- Case studies and patterns: [intelligence-history.md](intelligence-history.md)
- Privacy and digital hygiene: [opsec-and-privacy.md](opsec-and-privacy.md)
- Physical and travel safety: [personal-security.md](personal-security.md)
- Manipulation and deception: [deception-and-active-measures.md](deception-and-active-measures.md)
- Manipulation counter-moves: [counter-strategies.md](counter-strategies.md)
- Bias and persuasion defense: [epistemic-self-defense.md](epistemic-self-defense.md)
- Ethics: [ethics.md](ethics.md)
