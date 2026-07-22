"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.name,
    debug=settings.debug,
    version="0.1.0",
    description="API foundation for the Personal Knowledge Agent.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["system"])
async def root() -> dict[str, str]:
    """Describe the API and expose its documentation URL."""

    return {"name": settings.name, "docs": "/docs"}


@app.get("/health", tags=["system"])
async def health() -> dict[str, str]:
    """Report process health for containers and deployment platforms."""

    return {"status": "healthy", "environment": settings.environment}

