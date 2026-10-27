from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

Base = declarative_base()

engine = create_engine(url=settings.DB_CONNECTION)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Session_Local = SessionLocal  # backward compatibility alias


def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
