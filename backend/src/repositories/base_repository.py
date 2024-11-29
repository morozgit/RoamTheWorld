from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    async def get_all(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, **kwargs):
        raise NotImplementedError