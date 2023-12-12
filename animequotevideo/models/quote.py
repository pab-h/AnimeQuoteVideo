from dataclasses import dataclass
from dataclasses import field
from typing import Optional

@dataclass
class Quote:
    anime: str
    animeImage: Optional[str] = field(default = None)
    character: str
    characterImage: Optional[str] = field(default = None)
    quote: str