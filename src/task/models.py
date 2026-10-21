from sqlalchemy import Column, String, Integer, Boolean, Text, DateTime, func
from src.utils.db import Base

class Task(Base):
    __tablename__="tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    is_completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now() )
