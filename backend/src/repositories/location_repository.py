from sqlalchemy import select
from .base_repository import AbstractRepository
from ..schemas.location_schemas import SLocation
from ..models.models import LocationModels
from src.config.db.session import async_session_maker


class LocationRepository(AbstractRepository):
    async def add_one(self, location: SLocation) -> int:
        async with async_session_maker() as session:
            location_dict = location.model_dump()
            location_orm = LocationModels(**location_dict)
            session.add(location_orm)
            await session.flush()
            await session.commit()
            return location_orm.id

    async def get_all(self) -> list[SLocation]:
        async with async_session_maker() as session:
            query = select(LocationModels)
            result = await session.execute(query)
            locations = result.scalars().all()
            location_schemas = [SLocation.model_validate(loc.__dict__) for loc in locations]
            return location_schemas

    async def get_one(self, location_id: int) -> SLocation:
        pass
