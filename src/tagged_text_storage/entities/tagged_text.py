from dataclasses import dataclass
from datetime import datetime

from .source import Source
from .tag import Tag


@dataclass
class TaggedText:
    id: int
    text: str
    created_at: datetime
    tags: list[Tag]
    source: Source
