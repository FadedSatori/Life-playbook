# Operational Security and Privacy

Operational security is the discipline of asking what an adversary could learn about you from pieces you never thought were secret, and then closing the gaps that matter. It is not secrecy for its own sake. It is deciding what is worth protecting, from whom, and at what cost.

For a civilian, the realistic enemy is rarely a spy. It is a scammer with your leaked data, a criminal who wants your email account, a data broker selling your address, an ex-partner who knows your passwords, or a stranger assembling your routine from your posts. The defenses are mostly boring: updates, unique passwords, strong second factors, backups, and fewer public details.

Everything here is defensive. It protects you and your family. Never use these ideas to hide wrongdoing, evade lawful process, or deceive people who are owed the truth. See [ethics.md](ethics.md) and [warrior-codes.md](warrior-codes.md).

---

## Where OPSEC Comes From

Operations security became a formal process in the US military during the Vietnam War. A team set up to work out how the enemy kept learning about American operations in advance concluded that the leaks were not coming from broken codes. They came from ordinary, observable activity. The effort is commonly known by its code name, Purple Dragon, and the dates are usually given as the mid-1960s. A national OPSEC program was later formalized by presidential directive in the late 1980s.

The process is usually taught as five steps, run in a loop rather than once:

1. **Identify critical information.** What would hurt if an adversary had it?
2. **Analyze the threat.** Who wants it, and what can they actually do?
3. **Analyze vulnerabilities.** Where does that information leak from?
4. **Assess risk.** How likely is exposure, and how bad is it?
5. **Apply countermeasures.** Close the gaps with the cheapest effective fix.

The sequence matters. Most people jump to step 5 (buy a tool) without doing steps 1 through 4. That is how you end up with an expensive VPN and a public profile listing your employer, street, and kids' school.

---

## Applying the Five Steps to a Person

**1. Critical information.** For most men this is short:
- Money access: bank, brokerage, crypto, tax and identity numbers.
- Control of your email, phone number, and primary accounts.
- Where you and your family will be, and when.
- Where you live and where your children spend their days.
- Medical, legal, and relationship details that could be used against you.
- Business plans, client data, and employer-confidential material.

**2. Threats.** Match each item to a realistic adversary (see tiers below).

**3. Vulnerabilities.** Reused passwords, a phone number that can be ported, a public home address, a fitness app that maps your runs, a relative who posts everything.

**4. Risk.** Rank by likelihood times damage. An email takeover is common and devastating. A government targeting you is rare. Spend effort accordingly. See [mental-models/probabilistic-thinking.md](mental-models/probabilistic-thinking.md).

**5. Countermeasures.** Fix the top three risks first. Re-run the loop when your life changes: a divorce, a new job, a public role, a move, a business exit.

---

## Threat Modeling by Tier

Pick the tier that honestly describes you. Do not borrow the threat model of someone far more exposed.

**Baseline (almost everyone).** Realistic adversaries: scammers, phishers, credential-stuffing criminals, data brokers, marketers, and the occasional opportunistic thief. Goal: avoid being an easy target. The baseline checklist below covers you.

**Elevated.** You have a public profile, handle other people's money or data, run a business, hold a security clearance or sensitive job, are going through a contentious divorce or custody fight, or have an ex or a stranger who fixates on you. Added adversaries: stalkers and ex-partners, disgruntled people, targeted fraud, competitors, doxxers. Goal: shrink your footprint and harden accounts beyond the default.

**High-risk.** Journalists in hostile settings, activists under pressure, people fleeing abusive partners, those with credible threats against them, or people targeted by well-resourced actors. State-level adversaries are rare and not a concern for most readers. If this is you, do not rely on a playbook alone. Use specialist help: advocates, legal counsel, and organizations such as the EFF's Surveillance Self-Defense guide, and for abuse situations a domestic-violence advocate. See [personal-security.md](personal-security.md).

**Rule:** most people spend too little on baseline and too much on exotic threats. Finish the baseline before anything else.

---

## What You Leak: The Aggregation Problem

No single public fact is dangerous. Combined, they are. A name from a tagged photo, a street from a delivery selfie, a school from a sports post, a schedule from a gym check-in: together that is a map of your life. Intelligence analysts call this mosaic building, and it is the same technique scammers and stalkers use. See [intelligence-tradecraft.md](intelligence-tradecraft.md).

**Common leaks:**
- **Metadata.** Files and messages carry data about the data: who, when, how often, from where. Often more revealing than content.
- **Photos.** Many phones embed location and device data (EXIF) in image files. Major social platforms generally strip much of it on upload, but not every channel does (email, cloud links, some messaging and file-sharing paths). Check your camera settings. Backgrounds (house numbers, street signs, mail, school logos, license plates) leak too.
- **Social posts.** Real-time travel, tagged locations, children's names and schools, birthdays, and pet names (often used in security questions).
- **Fitness apps.** Public routes and start/stop points can reveal your home and routine. Set privacy zones and keep activity private by default.
- **Delivery and shipping.** Labels, receipts, and parcels show your name and address. Consider a mailbox service or locker for sensitive deliveries, and shred labels.
- **Public records.** Property, voter, court, and business registrations are often searchable and are the raw material for data brokers. What is public varies by jurisdiction.
- **Your own mouth.** The easiest leak. See elicitation in [intelligence-tradecraft.md](intelligence-tradecraft.md).

---

## Account Security Fundamentals

Most real-world compromise comes from a short list of failures. Fix these and you beat most attackers.

1. **Secure your email first.** Whoever controls your email can reset every other account. Give it your strongest password and strongest second factor. See also [technology-leverage.md](technology-leverage.md).
2. **Use a password manager** and a unique, long password for every account. Current NIST guidance emphasizes length and screening against known-breached passwords over forced complexity rules and routine rotation. Change a password when you suspect compromise, not on a calendar.
3. **Turn on multi-factor authentication, strongest available.** Ranked, best to worst:
   - **Passkeys or hardware security keys (FIDO/WebAuthn).** Resistant to phishing because they are tied to the real site.
   - **Authenticator app codes.** Much better than SMS, but a convincing fake login page can still capture a code in real time.
   - **SMS or voice codes.** Better than nothing, weakest of the common options, exposed to SIM swapping and interception. Use only where nothing else is offered.
4. **Store recovery codes offline.** Print them or keep them in your password manager, and put a copy somewhere a house fire cannot reach. Losing your second factor without recovery codes can lock you out for good.
5. **Defend your phone number against SIM swaps.** In a SIM swap, an attacker convinces your carrier to move your number to their SIM. Ask your carrier for a port-out PIN or number lock, and a strong account PIN. In the US, the FCC has required carriers to offer protections against unauthorized SIM changes and port-outs, but specifics vary by carrier. Check yours.
6. **Audit connected apps and logged-in sessions** on your email and social accounts. Remove what you do not use.

---

## Device Hygiene

- **Update promptly.** Turn on automatic updates for the operating system, browser, and apps. Most attacks use known, already-fixed flaws.
- **Lock screens** with a strong passcode (not 1234 or a birthday). Biometrics are convenient but can be compelled in some settings; know your risk.
- **Encrypt storage.** Modern phones do this by default when a passcode is set. Turn on full-disk encryption for laptops using the built-in tools.
- **Back up.** Follow the 3-2-1 rule in [technology-leverage.md](technology-leverage.md). Keep one backup offline so ransomware cannot reach it.
- **Review app permissions.** Does a flashlight app need your contacts and location? Set location to "while using" or off, and review microphone and camera access.
- **Delete unused apps and old accounts.** Every account is a future breach.

---

## Phishing and Social Engineering in Brief

The most common attack on a person is a message that creates urgency and asks for a code, a payment, or a click. Whether it is a fake bank alert, a "family emergency" call, or a boss asking for gift cards, the pattern is the same: pressure, authority, secrecy.

**Rules:**
- Never act on an unexpected request through the channel it arrived. Hang up and call a number you already trust.
- Slow down when you feel rushed. Urgency is the tell.
- Never read a one-time code to anyone who contacted you.
- Agree on a family verification word for emergency calls, since voice cloning exists.
- Report scams in the US to the FTC and the FBI's Internet Crime Complaint Center (IC3).

For the psychology see [counter-strategies.md](counter-strategies.md), [dark-psychology.md](dark-psychology.md), and [epistemic-self-defense.md](epistemic-self-defense.md).

---

## Reducing Your Footprint

You cannot vanish, but you can raise the cost of finding you.

- **Data brokers.** These companies compile and sell profiles from public records and purchased data. Most have opt-out forms; the process is tedious and records tend to reappear, so repeat it periodically or consider a reputable paid removal service (check current independent reviews). Some US states give residents legal deletion rights, with California's the best known. Treat this as a US-specific, evolving area.
- **Privacy settings.** Make social accounts private, limit who can see friend lists, tags, and old posts, and turn off location history where you can.
- **Email aliases.** Use a separate address or alias for shopping, newsletters, and sign-ups, distinct from your banking and primary identity email. A leak then points to its source and does not expose the real account.
- **Credit freeze (US).** A freeze at the credit bureaus stops new credit being opened in your name. By US law it is free. It is one of the highest-value steps against identity theft; place it with each bureau and lift it temporarily when you apply for credit.

---

## Communications

**What end-to-end encryption does:** only the sender and recipient devices can read the message content in transit. A provider or network eavesdropper cannot.

**What it does not do:**
- It does not hide metadata: who talked to whom, when, and often your IP address or approximate location.
- It does not protect against someone with access to your unlocked phone, or against a screenshot.
- It does not protect messages that are backed up unencrypted. Check whether your chat backups are encrypted.
- It does not protect against a compromised device, or a person you trusted who then shared the conversation.

**Habits:** assume anything written can be forwarded. Do not put in writing what you could not defend. Use disappearing messages where a conversation needs no record. Verify unexpected contact from a "known" number, since numbers can be spoofed.

---

## Working and Traveling With Devices

- **Public Wi-Fi.** Modern encrypted websites limit snooping, but fake hotspots and shared networks remain a risk. Prefer your phone's hotspot for anything sensitive. A VPN shifts trust from the local network to the VPN company; it is not a cloak. Check independent reviews if you use one.
- **Lock and shield.** Use a screen privacy filter in public, never leave devices unattended, and avoid public USB charging ports (use your own charger or a data-blocking adapter).
- **Borders.** Authorities in many countries can inspect devices at borders, and rules differ by country. Know the rules for where you are going, carry less, and keep data in encrypted cloud storage you can reach later if that suits your risk.
- **High-risk travel.** If you have real reason for concern, use a clean loaner device with minimal data and fresh accounts, and wipe or reset it on return. Keep this general and proportionate; most travelers never need it.

---

## Compartmentation

Separate identities so one breach does not become all breaches.

- **Work and personal.** Different email, separate browser profiles, and no work data on personal accounts or the reverse.
- **Money.** A dedicated email and strongest security for financial accounts, used for nothing else.
- **Public and private.** If you have a public presence, keep it on separate accounts from family and friends.

Compartments only work if you keep them separate. Reusing a password, phone number, or photo across them rebuilds the link.

---

## Family and Kids

Your exposure includes everyone you live with and everyone who posts about you.

- **Teach kids the basics early:** do not share location, school, or full name publicly; never send photos to strangers; tell a parent if anyone online makes them uncomfortable. See [parenting.md](parenting.md).
- **Ask relatives to hold back.** Grandparents often post school names, birthdays, and travel plans. Ask once, kindly, and give them a reason.
- **Be careful posting children.** Consider whether posting is worth the permanent record.
- **Set a family verification word** and a plan for lost phones.
- **Secure the household:** router password changed from the default, router updated, and guest network for visitors and smart-home devices.

---

## The Cost of Overdoing It

Security that you will actually use beats perfect security you abandon.

- Paranoia is a failure mode. It costs sleep, relationships, and focus, and it makes you easier to manipulate with fear.
- Friction kills habits. If a system is too painful, you will route around it and end up worse off.
- Chasing exotic threats while skipping the baseline is the classic mistake.
- Do the high-value steps well, accept residual risk, and move on.

Match effort to risk. See [resilience.md](resilience.md) and [antifragility.md](antifragility.md): the goal is a life that survives a breach, not one that never experiences one. Have backups, freezes, and a recovery plan so an incident is an inconvenience.

---

## Baseline Checklist (Everyone)

- [ ] Password manager in use; unique passwords on important accounts
- [ ] Email secured first with strong password and strongest available MFA
- [ ] MFA on banking, email, social, and cloud accounts; prefer app, key, or passkey over SMS
- [ ] Recovery codes stored safely offline
- [ ] Carrier port-out PIN or number lock set
- [ ] Automatic updates on for phone, computer, browser
- [ ] Screen lock and device encryption on
- [ ] Backups following 3-2-1, one offline
- [ ] Credit freeze placed (US)
- [ ] Never share one-time codes; verify unexpected requests by a trusted channel
- [ ] Family verification word agreed

## Elevated Checklist (Added)

- [ ] Hardware security keys or passkeys on email, finance, and key accounts
- [ ] Data broker opt-outs submitted and calendar reminder to repeat
- [ ] Separate aliases for sign-ups; compartmented work and personal identities
- [ ] Social accounts set to private; location sharing audited; fitness privacy zones set
- [ ] Public records exposure reviewed; mail service or business address where appropriate
- [ ] Encrypted messaging with encrypted backups for sensitive conversations

## Quarterly Privacy Audit (30 Minutes)

1. Review logged-in sessions, devices, and connected apps on email and top accounts; remove strangers and stale entries.
2. Check whether your email addresses appear in known breaches using a reputable breach-notification service; change affected passwords.
3. Review app permissions and delete unused apps and accounts.
4. Search your own name and address as a stranger would; note what is exposed.
5. Re-check social privacy settings and old tagged content.
6. Ask what changed in your life this quarter, and re-run the five OPSEC steps if so.

---

## Cross-References

- Defensive side of intelligence: [intelligence-tradecraft.md](intelligence-tradecraft.md)
- Digital sovereignty and backups: [technology-leverage.md](technology-leverage.md)
- Manipulation and social engineering: [counter-strategies.md](counter-strategies.md), [dark-psychology.md](dark-psychology.md)
- Physical safety and stalking response: [personal-security.md](personal-security.md)
- Counterintelligence mindset: [counterintelligence.md](counterintelligence.md)
- Protecting children: [parenting.md](parenting.md)
- Preparedness and digital resilience: [preparedness.md](preparedness.md)
