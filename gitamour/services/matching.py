from typing import Iterable, List
from gitamour.core.profile import DeveloperProfile

def naive_match(profile: DeveloperProfile, others: Iterable[DeveloperProfile]) -> List[DeveloperProfile]:
    base = set(profile.affinity_vector())
    scored = []
    for candidate in others:
        overlap = base.intersection(candidate.affinity_vector())
        if overlap:
            scored.append((len(overlap), candidate))
    return [c for _, c in sorted(scored, reverse=True)]
