from datetime import datetime, timezone
from fastapi import APIRouter

router = APIRouter(tags=["Healthcheck"])


@router.get("", summary="API healthcheck")
@router.get("/", include_in_schema=False)
def healthcheck():
    """Returns the operational status of the service."""
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
