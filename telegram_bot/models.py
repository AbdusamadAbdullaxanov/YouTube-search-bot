from start_database import Base
from sqlalchemy import Column, Integer, String
from datetime import datetime


class Videos(Base):
    __tablename__ = "video_id"

    id = Column(Integer, nullable=False, primary_key=True)
    video_id = Column(String, nullable=False)
    username = Column(String, nullable=False)
    search_title = Column(String, nullable=False)
    modified = Column(String, nullable=False, default=str(datetime.utcnow()))

