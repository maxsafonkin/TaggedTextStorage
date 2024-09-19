from dataclasses import dataclass


@dataclass
class Source:
    id: int
    title: str
    url: str
