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
            session.add(location)
            await session.flush()
            await session.commit()
            return location.id

    async def get_all(db) -> list[SLocation]:
        query = select(LocationModels)
        location_query = await db.execute(query)
        locations = location_query.scalars().all()
        return locations if locations else []

    async def get_one(self, location_id: int) -> SLocation:
        pass
