"""Smoke tests for the FastAPI application."""

import asyncio

from app.main import app, health, root


def test_root_describes_the_api() -> None:
    response = asyncio.run(root())

    assert response == {
        "name": "Personal Knowledge Agent API",
        "docs": "/docs",
    }


def test_health_reports_service_status() -> None:
    response = asyncio.run(health())

    assert response == {
        "status": "healthy",
        "environment": "development",
    }


def test_openapi_schema_exposes_system_routes() -> None:
    schema = app.openapi()

    assert "/" in schema["paths"]
    assert "/health" in schema["paths"]
