from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class Tag(BaseModel):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String())
