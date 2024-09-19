from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class Text(BaseModel):
    __tablename__ = "texts"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String())
    created_at: Mapped[datetime] = mapped_column(DateTime())
    source_id: Mapped[int] = mapped_column(Integer, ForeignKey("sources.id"))
    url: Mapped[str] = mapped_column(String())

    source: Mapped[str] = relationship("Source")
    tags: Mapped[list[str]] = relationship("Text2Tag")
    