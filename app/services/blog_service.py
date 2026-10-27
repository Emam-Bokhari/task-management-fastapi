from sqlalchemy.orm import Session

from app.models.blog import Blog
from app.schema.blog_schema import BlogCreate


class BlogService:
    def __init__(self, db: Session):
        self.db = db

    def create_blog(self, payload: BlogCreate) -> Blog:
        new_blog = Blog(**payload.model_dump())
        self.db.add(new_blog)
        self.db.commit()
        self.db.refresh(new_blog)
        return new_blog


def create_blog(payload: BlogCreate, db: Session) -> Blog:
    return BlogService(db).create_blog(payload)
