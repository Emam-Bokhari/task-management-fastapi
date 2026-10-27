from typing import Any
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def send_response(
    success: bool,
    status_code: int,
    message: str,
    data: Any | None = None,
    meta: dict[str, Any] | None = None,
):
    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder({
            "success": success,
            "message": message,
            "data": data,
            "meta": meta,
        }),
    )
