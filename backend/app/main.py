from fastapi import FastAPI, Depends
from app.routers import items, interactions, learners, pipeline, analytics
from app.auth import verify_api_key
from app.settings import settings

app = FastAPI(title="Learning Management Service")

app.include_router(
    items.router,
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(verify_api_key)],
)

app.include_router(
    interactions.router,
    prefix="/interactions",
    tags=["interactions"],
    dependencies=[Depends(verify_api_key)],
)

if settings.enable_learners:
    app.include_router(
        learners.router,
        prefix="/learners",
        tags=["learners"],
        dependencies=[Depends(verify_api_key)],
    )

app.include_router(
    pipeline.router,
    prefix="/pipeline",
    tags=["pipeline"],
    dependencies=[Depends(verify_api_key)],
)

app.include_router(
    analytics.router,
    prefix="/analytics",
    tags=["analytics"],
    dependencies=[Depends(verify_api_key)],
)
