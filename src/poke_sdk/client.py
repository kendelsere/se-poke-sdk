import requests
from typing import Optional
import time
from .exceptions import APIError, RateLimitError

class Client:
    def __init__(
        self, 
        base_url: str = "https://pokeapi.co/api/v2",
        timeout: int = 30
    ):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()

    def _request(
        self,
        endpoint: str, 
        params: Optional[dict] = None, 
    ) -> dict:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()
    
    def _request_with_retry(
            self,
            endpoint: str, 
            params: Optional[dict] = None, 
            max_retries: int = 3
    ) -> dict:
        """Makes a request with exponential backoff retry logic
        
        Args:
            method: HTTP method to use
            endpoint: API endpoint to call
            params: Optional query parameters
            max_retries: Maximum number of retry attempts
            
        Returns:
            Response JSON from the API
            
        Raises:
            APIError: If all retries fail
        """

        attempt = 0
        while attempt <= max_retries:
            try:
                return self._request(endpoint, params)
            except Exception as e:
                if attempt == max_retries:
                    raise e if isinstance(e, RateLimitError) else APIError(f"Request failed after {max_retries} retries: {str(e)}")
                wait = (2 ** attempt)
                time.sleep(wait)
                attempt += 1