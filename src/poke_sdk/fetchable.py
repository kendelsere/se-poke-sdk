from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Fetchable:
    name: Optional[str]
    url: str
    _json: dict = field(default=None, init=False)

    def __str__(self) -> str:
        return self.name

    def get(self, cls: type):
        """Makes a GET request to the url and constructs an instance of cls from the response
        
        Args:
            cls: The class to construct from the response
            
        Returns:
            An instance of cls constructed from the response JSON
        """
        return cls.from_json(self.get_json())
    
    def get_json(self) -> any:
        if (self._json is None):
            import requests
            response = requests.get(self.url)
            response.raise_for_status()
            self._json = response.json()
        return self._json
