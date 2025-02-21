class APIError(Exception):
    """Base exception for API errors"""
    pass

class RateLimitError(APIError):
    """Raised when API rate limit is exceeded"""
    pass
