from sqlalchemy import Column, Integer, String
from core.database import Base
from router.realtime import time
# from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100), index=True)
    Email = Column(String(100), nullable=False, unique=True)
    password = Column(String(1000), nullable=False)
    time = Column(String(40), default=time.current_time)
