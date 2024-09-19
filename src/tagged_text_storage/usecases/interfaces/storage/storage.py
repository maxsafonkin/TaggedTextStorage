import abc
from datetime import datetime
from typing import Iterable

from tagged_text_storage import entities


class Storage(abc.ABC):
    @abc.abstractmethod
    def get_tags(self, filter_: str | None) -> Iterable[entities.Tag]:
        pass

    @abc.abstractmethod
    def get_sources(self, filter_: str | None) -> Iterable[entities.Source]:
        pass

    @abc.abstractmethod
    def get_texts(
        self,
        tags: list[entities.Tag] | None,
        sources: list[entities.Source] | None,
        since: datetime | None,
        until: datetime | None,
    ) -> Iterable[entities.TaggedText]:
        pass
