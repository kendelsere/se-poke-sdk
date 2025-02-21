from .client import Client
from dataclasses import dataclass, field
from typing import List
from .fetchable import Fetchable


@dataclass
class Name:
    name: str
    language: Fetchable

@dataclass
class Generation:
    id: int
    name: str
    abilities: List[Fetchable]
    main_region: Fetchable
    moves: List[Fetchable]
    names: List[Name]
    pokemon_species: List[Fetchable]
    types: List[Fetchable]
    version_groups: List[Fetchable]

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            id=data['id'],
            name=data['name'],
            abilities=[Fetchable(name=a['name'], url=a['url']) for a in data['abilities']],
            main_region=Fetchable(name=data['main_region']['name'], url=data['main_region']['url']),
            moves=[Fetchable(name=m['name'], url=m['url']) for m in data['moves']],
            names=[Name(name=n['name'], language=Fetchable(name=n['language']['name'], url=n['language']['url'])) for n in data['names']],
            pokemon_species=[Fetchable(name=p['name'], url=p['url']) for p in data['pokemon_species']],
            types=[Fetchable(name=t['name'], url=t['url']) for t in data['types']],
            version_groups=[Fetchable(name=v['name'], url=v['url']) for v in data['version_groups']]
        )