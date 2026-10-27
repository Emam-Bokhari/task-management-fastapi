import utils.session
from fastapi import FastAPI
from app.api import init_routes
from app.core.database import Base, engine

# Create tables in the database if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="Task Management RESTful API with FastAPI",
    version="1.0.0",
)


@app.get("/", tags=["Root"])
def read_root():
    """Welcome message for API root."""
    return {
        "message": "Welcome to the Task Management API. Check out /docs for the interactive API spec!"
    }


# Initialize all routes (v1, and future v2)
init_routes(app)