"""
Redis caching service (optional enhancement).
Caches Google Places / Yelp results for popular queries.
"""

import json
from typing import Optional
from app.core.config import settings


class CacheService:
    """Simple Redis wrapper for query result caching."""

    def __init__(self):
        self._client = None

    @property
    def client(self):
        if self._client is None:
            try:
                import redis
                self._client = redis.from_url(settings.REDIS_URL)
            except Exception:
                self._client = None
        return self._client

    def get(self, key: str) -> Optional[dict]:
        """Retrieve cached JSON by key."""
        if not self.client:
            return None
        raw = self.client.get(key)
        return json.loads(raw) if raw else None

    def set(self, key: str, value: dict, ttl: int = 3600):
        """Cache a JSON value with TTL (default 1 hour)."""
        if not self.client:
            return
        self.client.setex(key, ttl, json.dumps(value))


cache_service = CacheService()
