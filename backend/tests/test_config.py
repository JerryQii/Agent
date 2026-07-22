"""Tests for environment-driven application settings."""

from app.config import Settings


def test_settings_use_safe_development_defaults() -> None:
    settings = Settings(_env_file=None)

    assert settings.environment == "development"
    assert settings.api_prefix == "/api/v1"
    assert settings.openai_api_key is None


def test_settings_read_prefixed_environment_variables(monkeypatch) -> None:
    monkeypatch.setenv("APP_ENVIRONMENT", "test")
    monkeypatch.setenv("APP_DEBUG", "true")

    settings = Settings(_env_file=None)

    assert settings.environment == "test"
    assert settings.debug is True

