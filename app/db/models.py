from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Document(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  doc_id: str = Field(index=True, unique=True)
  filename: str
  chunk_count: int = Field(default=0)
  status: str = Field(default="processing")
  created_at: datetime = Field(default_factory=datetime.utcnow)

class FlashCard(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  doc_id: str = Field(index=True)
  question: str
  answer: str
  ease_factor: float = Field(default=2.5)
  interval: int = Field(default=1)
  due_date: datetime = Field(default_factory=datetime.utcnow)

class ReviewLog(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  card_id: int = Field(index=True)
  score: int = Field(default=0)
  review_date: datetime = Field(default_factory=datetime.utcnow)

class Assignment(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  doc_id: str = Field(index=True)
  title: str
  status: str = Field(default="pending")
  due_date: datetime = Field(default_factory=datetime.utcnow)