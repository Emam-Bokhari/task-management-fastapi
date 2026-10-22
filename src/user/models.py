from sqlalchemy import Column, String, Integer, Boolean, DateTime, func 
from src.utils.db import Base

class UserModel(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_name = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, index=True)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())