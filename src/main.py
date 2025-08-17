from fastapi import FastAPI
from .routes.user_routes import router as user_router
from .config.env_variables import settings

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION
)

app.include_router(user_router, prefix="/api/v1")