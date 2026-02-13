from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class DeveloperProfile:
    handle: str
    interests: List[str] = field(default_factory=list)
    skills: List[str] = field(default_factory=list)
    bio: Optional[str] = None

    def affinity_vector(self) -> List[str]:
        return list(set(self.interests + self.skills))
