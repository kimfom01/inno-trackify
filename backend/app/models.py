from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    email = Column(String(50), unique=True, index=True)
    password = Column(String(100))

    activity = relationship("Activity", back_populates="owner")


class ActivityType(Base):
    __tablename__ = "activity_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    icon_name = Column(String(200))

    activity = relationship("Activity", back_populates="activity_type")

class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    user_id = Column(Integer, ForeignKey("users.id"))
    type_id = Column(Integer, ForeignKey("activity_types.id"))
    duration = Column(String(50))
    start_time = Column(DateTime, default=datetime.datetime.utcnow)
    end_time = Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String(2000), nullable=True)

    owner = relationship("User", back_populates="activity")
    activity_type = relationship("ActivityType", back_populates="activity")