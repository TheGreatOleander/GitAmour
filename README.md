# GitAmour — Courtship Network

GitAmour is an experimental social–technical substrate designed to help developers
**discover, resonate, and align** with other developers.

It is not a chat app.  
It is not a job board.  
It is not a social feed.

GitAmour explores a different question:

> *What if developer collaboration emerged from affinity, intent, and signal —
> rather than profiles, resumes, or follower graphs?*

---

## Core Idea

Most systems force connection through explicit actions:

- Send request
- Follow user
- Apply to role
- Join channel

GitAmour instead models **attraction surfaces**.

Developers emit signals (interests, skills, activity, intent), and the network
allows patterns of compatibility to emerge.

The system experiments with:

- Affinity instead of popularity  
- Discovery instead of search  
- Alignment instead of recruitment  

---

## Conceptual Model

GitAmour treats collaboration as a form of **mutual selection dynamics**.

Developers are represented as evolving state entities rather than static accounts.

Early primitives include:

- **DeveloperProfile** — identity seed  
- **Affinity Vector** — merged interest/skill signal  
- **Matching Mechanisms** — compatibility experiments  

This architecture supports future layers such as:

- Intent modeling  
- Reputation fields  
- Temporal interaction dynamics  
- Multi-agent emergence  

---

## Current Capabilities

### Developer Profiles

Profiles describe signal surfaces rather than credentials.

```python
DeveloperProfile(
    handle="alice",
    interests=["distributed systems", "graphics"],
    skills=["rust", "simulation"]
)
```

Profiles expose an **affinity vector**, used by matching logic.

---

### Matching (Experimental)

A naive matcher is provided as a baseline reference model:

- Detects shared affinity signals  
- Scores overlap  
- Returns compatibility ordering  

This is intentionally simple — the system is designed for iterative evolution.

---

### Logging Utility

GitAmour includes a lightweight logging layer to stabilize observability:

- Consistent formatting  
- Centralized logger creation  
- Extensible for future runtime modes  

---

### Configuration Surface

`config.yaml` introduces controlled runtime variation:

- Environment modes  
- Debug behavior  
- Logging policies  

This decouples system behavior from code changes.

---

## Design Philosophy

GitAmour is built around several principles:

**1. Signals over declarations**  
Compatibility should be inferred, not self-reported.

**2. Emergence over enforcement**  
Connections arise from dynamics, not forced mechanics.

**3. Infrastructure before complexity**  
Stability layers precede intelligence layers.

**4. Systems thinking over features**  
GitAmour evolves as a behavioral environment, not an app.

---

## Why “Courtship Network”?

Because collaboration resembles courtship dynamics more than transactions.

Healthy collaboration involves:

- Mutual relevance  
- Timing  
- Shared intent  
- Compatibility gradients  

GitAmour models these properties directly.

---

## Project Status

GitAmour is an evolving experimental system.

Recent releases have focused on:

- Release hygiene & version memory  
- Runtime foundations  
- Identity primitives  

Future releases may explore:

- Richer affinity models  
- Interaction protocols  
- Network dynamics  
- Intent & state evolution  

---

## Intended Audience

GitAmour is for developers interested in:

- Experimental systems  
- Emergent behavior  
- Social dynamics of engineering  
- Alternative collaboration models  

---

## Warning

This project is exploratory.

Expect:

- Rapid evolution  
- Incomplete abstractions  
- Conceptual shifts  
- Unconventional design choices  

---

## Contributing

Contributions are welcome, especially in:

- Matching algorithms  
- Signal modeling  
- Network mechanics  
- System architecture  
- Theoretical framing  

Open an issue or propose an experiment.

---

## Closing Thought

GitAmour is not trying to optimize developer networking.

It is asking:

> *What kinds of collaboration become possible if alignment is treated as a
> first-class systems problem?*
