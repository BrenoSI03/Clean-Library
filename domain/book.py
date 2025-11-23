from dataclasses import dataclass

@dataclass
class Book:
    id: int | None
    title: str
    author: str
    available: bool
