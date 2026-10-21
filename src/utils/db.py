from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.settings import settings

Base=declarative_base()

engine=create_engine(url=settings.DB_CONNECTION)

Session_Local=sessionmaker(bind=engine,autoflush=False, autocommit=False)

def get_db():
    session=Session_Local()
    try:
        yield session 
    finally:
        session.close()