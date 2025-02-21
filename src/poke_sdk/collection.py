from dataclasses import dataclass
from typing import List, Optional
from .fetchable import Fetchable

@dataclass
class Result:
    name: str
    url: str

@dataclass
class Collection:
    count: int
    next: Optional[str]
    previous: Optional[str] 
    results: List[Fetchable]

    @classmethod
    def from_json(cls, data: dict) -> "Collection":
        return cls(
            count=data["count"],
            next=data["next"],
            previous=data["previous"],
            results=[
                Fetchable(result["name"], result["url"])
                for result in data["results"]
            ]
        )
