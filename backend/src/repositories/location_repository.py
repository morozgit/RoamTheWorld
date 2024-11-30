from .base_repository import AbstractRepository
from ..schemas.location_schemas import SLocation
from ..models.location_models import LocationModels
from sqlalchemy import select
from src.config.db.session import async_session_maker


class LocationRepository(AbstractRepository):
    async def add_one(self, location: SLocation) -> int:
        async with async_session_maker() as session:
            location_dict = location.model_dump()
            location = LocationModels(**location_dict)
            session.add(location)
            await session.flush()
            await session.commit()
            return location.id

    async def find_all(cls) -> list[SLocation]:
        query = select(LocationModels)
        location_models, location_dicts = await cls._execute_query(query)
        if not location_dicts:
            return []
        location_schemas = [
            SLocation.model_validate(loc_dict) for loc_dict in location_dicts
        ]
        return location_schemas
