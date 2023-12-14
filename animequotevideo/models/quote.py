from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Quote:
    anime: str
    character: str
    quote: str
    animeImage: Optional[str] = field(default=None)
    characterImage: Optional[str] = field(default=None)
