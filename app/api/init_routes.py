from fastapi import FastAPI
from app.api.v1.init_routes import router as v1_router

# As new versions are developed, import their routers here:
# from app.api.v2.init_routes import router as v2_router


def init_routes(app: FastAPI):
    """
    Central API Route Initializer.
    Mounts all API versions (/api/v1, /api/v2, etc.) to the FastAPI application.
    """
    app.include_router(v1_router)
    # app.include_router(v2_router)
