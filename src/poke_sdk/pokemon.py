from dataclasses import dataclass, field
from typing import List, Optional
from .fetchable import Fetchable
from .client import Client
from .collection import Collection

@dataclass
class Ability:
    is_hidden: bool
    slot: int
    ability: Fetchable

@dataclass
class GameIndex:
    game_index: int
    version: Fetchable

@dataclass
class VersionDetail:
    rarity: int
    version: Fetchable

@dataclass
class HeldItem:
    item: Fetchable
    version_details: List[VersionDetail]

@dataclass
class Stat:
    base_stat: int
    effort: int
    stat: Fetchable

@dataclass
class Type:
    slot: int
    type: Fetchable

@dataclass
class PastType:
    generation: Fetchable
    types: List[Type]

@dataclass
class Move:
    move: Fetchable
    version_group_details: List[dict]

@dataclass
class VersionGroupDetails:
    level_learned_at: int
    version_group: Fetchable
    move_learn_method: Fetchable

@dataclass
class Cry:
    latest: str
    legacy: str


@dataclass
class Pokemon:
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: List[Ability]
    forms: List[Fetchable]
    game_indices: List[GameIndex]
    held_items: List[HeldItem]
    sprites: Optional[dict] = None
    stats: Optional[List[dict]] = None
    types: Optional[List[dict]] = None
    past_types: Optional[List[dict]] = None
    cries: Optional[dict] = None
    location_area_encounters: Optional[Fetchable] = None
    moves: Optional[List[Move]] = None
    species: Optional[Fetchable] = None
    
    @classmethod
    def from_json(cls, data: dict, base_url: str) -> "Pokemon":
        return cls(
            id=data["id"],
            name=data["name"], 
            base_experience=data["base_experience"],
            height=data["height"],
            is_default=data["is_default"],
            order=data["order"],
            weight=data["weight"],
            abilities=[Ability(**ability) for ability in data["abilities"]],
            forms=[Fetchable(name=form["name"], url=form["url"]) for form in data["forms"]],
            game_indices=[GameIndex(**index) for index in data["game_indices"]],
            held_items=[
                HeldItem(
                    item=item["item"],
                    version_details=[VersionDetail(**detail) for detail in item["version_details"]]
                ) for item in data["held_items"]
            ],
            location_area_encounters=Fetchable(name=None, url=f"{base_url}/{data.get('location_area_encounters').lstrip('/')}"),
            sprites=data.get("sprites"),
            stats=data.get("stats"),
            types=data.get("types"),
            past_types=data.get("past_types"),
            cries=data.get("cries")
        )
    
    