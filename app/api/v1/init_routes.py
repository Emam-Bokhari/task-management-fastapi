from fastapi import APIRouter, FastAPI

from app.api.v1.routes import (
    blog,
    healthcheck,
    product,
    task,
    user,
)

# Base router for API version 1
router = APIRouter(prefix="/api/v1")

# Standard versioned routes
router.include_router(router=healthcheck.router, prefix="/healthcheck")
router.include_router(router=user.router, prefix="/users")
router.include_router(router=task.router, prefix="/tasks")
router.include_router(router=product.router, prefix="/products")
router.include_router(router=blog.router, prefix="/blogs")

# Backward compatibility aliases
# 1. Direct /api/v1/register and /api/v1/login without /users prefix
router.include_router(router=user.router, include_in_schema=False)
# 2. Singular prefixes /task, /product, /blog
router.include_router(router=task.router, prefix="/task", include_in_schema=False)
router.include_router(router=product.router, prefix="/product", include_in_schema=False)
router.include_router(router=blog.router, prefix="/blog", include_in_schema=False)


def init_routes(app: FastAPI):
    """
    Register API v1 routes to the given FastAPI application.
    """
    app.include_router(router)
