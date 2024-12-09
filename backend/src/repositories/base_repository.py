from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    def __init__(self, schema_model):
        self.schema_model = schema_model

    @abstractmethod
    async def add_one(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, **kwargs):
        raise NotImplementedError
