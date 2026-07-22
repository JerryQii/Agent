"""Application configuration loaded from environment variables."""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings shared by the API and future service integrations."""

    model_config = SettingsConfigDict(
        env_file=("../.env", ".env"),
        env_file_encoding="utf-8",
        env_prefix="APP_",
        extra="ignore",
    )

    name: str = "Personal Knowledge Agent API"
    environment: str = "development"
    debug: bool = False
    api_prefix: str = "/api/v1"
    frontend_url: str = "http://localhost:3000"

    database_url: str = Field(
        default="postgresql+psycopg://knowledge:knowledge@localhost:5432/knowledge_agent"
    )
    redis_url: str = "redis://localhost:6379/0"
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "knowledge-password"
    openai_api_key: str | None = None


@lru_cache
def get_settings() -> Settings:
    """Return one validated settings object per process."""

    return Settings()

