from .client import Client
from .pokemon import Pokemon
from .generation import Generation
from .collection import Collection
from typing import Union

class PokeClient:
    def __init__(self):
        self.client = Client()

    def list_pokemon(self, page: int = 1, limit: int = 100):
        return Collection.from_json(self.client._request_with_retry('pokemon', params={'offset': page, 'limit': limit}))

    def get_pokemon(self, poke_identifier: Union[str, int]):
        response = self.client._request_with_retry(f'pokemon/{poke_identifier}')
        return Pokemon.from_json(data=response, base_url=self.client.base_url)
    
    def list_generations(self, page: int = 1, limit: int = 20):
        return Collection.from_json(self.client._request_with_retry('generation', params={'offset': page, 'limit': limit}))

    def get_generation(self, poke_identifier: Union[str, int]):
        response = self.client._request_with_retry(f'generation/{poke_identifier}')
        return Generation.from_json(data=response)
    