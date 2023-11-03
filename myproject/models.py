from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Platform(Base):
    __tablename__ = "program"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    gamelist = relationship("Games", back_populates="platform")


class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    is_installed = Column(Boolean, default=False)
    platform_id = Column(Integer, ForeignKey("program.id"))

    platform = relationship("Platform", back_populates="gamename")
