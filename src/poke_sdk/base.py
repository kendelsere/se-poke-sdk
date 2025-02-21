from typing import Optional

class BaseResource:
    def __init__(self, client):
        self.client = client

    def _get(self, endpoint: str, params: Optional[dict] = None) -> dict:
        return self.client._request('GET', endpoint, params=params)