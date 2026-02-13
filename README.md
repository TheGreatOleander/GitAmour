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

GitAmour instead models **attraction surfaces**:

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
