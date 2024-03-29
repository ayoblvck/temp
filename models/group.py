"""Model for the Groups"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base
from models.event import group_events
from models.user_group import user_groups


class Group(BaseModel, Base):
    """Group Model"""

    __tablename__ = "groups"
    title = Column(String(60), unique=True)
    users = relationship("User", secondary=user_groups,
                         back_populates="groups")
    events = relationship("Event", secondary=group_events,
                          back_populates="groups")

    def __init__(self, title: str):
        """Initializes the Group"""
        self.title = title

        super().__init__()
