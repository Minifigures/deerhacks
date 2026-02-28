"""
Application configuration — loaded from environment variables.
"""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # ── Google Cloud (Gemini + Google Places) ──
    GOOGLE_CLOUD_API_KEY: str = ""

    # ── Yelp ──
    YELP_API_KEY: str = ""

    # ── Mapbox ──
    MAPBOX_ACCESS_TOKEN: str = ""

    # ── OpenWeather ──
    OPENWEATHER_API_KEY: str = ""

    # ── PredictHQ ──
    PREDICTHQ_API_KEY: str = ""

    # ── Snowflake ──
    SNOWFLAKE_ACCOUNT: str = ""
    SNOWFLAKE_USER: str = ""
    SNOWFLAKE_PASSWORD: str = ""
    SNOWFLAKE_DATABASE: str = "PATHFINDER"
    SNOWFLAKE_SCHEMA: str = "PUBLIC"
    SNOWFLAKE_WAREHOUSE: str = "COMPUTE_WH"
    SNOWFLAKE_ROLE: str = "ACCOUNTADMIN"

    # ── Redis ──
    REDIS_URL: str = "redis://localhost:6379/0"

    # ── Firecrawl ──
    FIRECRAWL_API_KEY: str = ""

    # ── CORS ──
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
