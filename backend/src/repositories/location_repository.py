from sqlalchemy import select
from .base_repository import AbstractRepository
from ..schemas.location_schemas import SLocation
from ..models.models import LocationModels
from src.config.db.session import async_session_maker


class LocationRepository(AbstractRepository):
    async def add_one(self, location: SLocation) -> int:
        async with async_session_maker() as session:
            location_dict = location.model_dump()
            location = LocationModels(**location_dict)
            print(location.id)
            session.add(location)
            await session.flush()
            await session.commit()
            return location.id

    async def get_all(db) -> list[SLocation]:
        query = select(LocationModels)
        result = await db.execute(query)
        print("query", result)
        return result.scalars().all()
        # location_models, location_dicts = await cls._execute_query(query)
        # if not location_dicts:
        #     return []
        # location_schemas = [
        #     SLocation.model_validate(loc_dict) for loc_dict in location_dicts
        # ]
        # return location_schemas

    async def get_one(self, location_id: int) -> SLocation:
        pass
