from datetime import datetime
from typing import Iterable

from sqlalchemy import create_engine
from sqlalchemy.orm import joinedload, sessionmaker

from tagged_text_storage import entities, usecases

from . import models
from .config import StorageConfig


class Storage(usecases.interfaces.Storage):
    def __init__(self, storage_config: StorageConfig) -> None:
        engine = create_engine(storage_config.conn_uri)
        self._session_maker = sessionmaker(engine)

    def get_tags(self, filter_: str | None) -> Iterable[entities.Tag]:
        with self._session_maker() as s:
            query = s.query(models.Tag)
            if filter_:
                query = query.filter(models.Tag.title.ilike(f"%{filter_}%"))

            yield from (entities.Tag(tag.id, tag.title) for tag in query)

    def get_sources(self, filter_: str | None) -> Iterable[entities.Source]:
        with self._session_maker() as s:
            query = s.query(models.Source)
            if filter_:
                query = query.filter(models.Source.title.ilike(f"%{filter_}%"))

            yield from (entities.Source(source.id, source.title, source.url) for source in query)

    def get_texts(
        self,
        tags: list[entities.Tag] | None,
        sources: list[entities.Source] | None,
        since: datetime | None,
        until: datetime | None,
    ) -> Iterable[entities.TaggedText]:
        with self._session_maker() as s:
            query = (
                s.query(models.Text)
                .join(models.Source, models.Text.source_id == models.Source.id)
                .join(models.Text2Tag, models.Text.id == models.Text2Tag.text_id)
                .join(models.Tag, models.Text2Tag.tag_id == models.Tag.id)
            )
            if sources:
                query = query.filter(models.Source.id.in_([s.id for s in sources]))

            if tags:
                query = query.filter(models.Tag.id.in_([t.id for t in tags]))

            if since:
                query = query.filter(models.Text.created_at >= since)

            if until:
                query = query.filter(models.Text.created_at <= until)

            query = (
                query.options(joinedload(models.Text.source))
                # .options(joinedload(models.Text.text2tags).joinedload(models.Text2Tag.tag))
            )

            """
            sql query:

            select *
            from tags
            inner join text2tag
            on tags.id = text2tag.tag_id
            inner join texts
            on texts.id = text_id
            """

        return
