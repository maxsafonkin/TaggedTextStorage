from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class Source(BaseModel):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String())
    url: Mapped[str] = mapped_column(String())
