from fastapi import FastAPI
from app.routes import items, health
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

# Include routers
app.include_router(health.router)
app.include_router(items.router, prefix="/items")