from typing import Any
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

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
            "success":success,
            "message":message,
            "data":data,
            "meta":meta
        })
    )