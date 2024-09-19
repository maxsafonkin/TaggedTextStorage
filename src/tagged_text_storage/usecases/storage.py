from datetime import datetime
from typing import Iterable

from tagged_text_storage import entities

from . import errors, interfaces


class StorageUseCases:
    def __init__(self, storage: interfaces.storage.Storage) -> None:
        self._storage = storage

    def get_all_tags(self) -> Iterable[entities.Tag]:
        yield from self._storage.get_all_tags()

    def get_all_sources(self) -> Iterable[entities.Source]:
        yield from self._storage.get_all_sources()

    def get_texts(
        self,
        tags: list[entities.Tag] | None = None,
        sources: list[entities.Source] | None = None,
        since: datetime | None = None,
        until: datetime | None = None,
    ) -> Iterable[entities.TaggedText]:
        try:
            yield from self._storage.get_texts(tags=tags, sources=sources, since=since, until=until)
        except interfaces.storage.errors.NotFoundError:
            return
        except interfaces.storage.errors.StorageError as exc:
            raise errors.TextStorageError(str(exc)) from exc
