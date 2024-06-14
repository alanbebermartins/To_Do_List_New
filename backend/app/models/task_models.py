from sqlalchemy import Column, Integer, String
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, index=True)
    task_title = Column(String(20), nullable=False)
    task_description = Column(String(100), nullable=False)
