from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class Text2Tag(BaseModel):
    __tablename__ = "text2tag"

    text_id: Mapped[int] = mapped_column(Integer)
    tag_id: Mapped[int] = mapped_column(Integer)
