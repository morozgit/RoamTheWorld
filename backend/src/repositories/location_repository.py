from sqlalchemy import select
from .base_repository import AbstractRepository
from ..schemas.location_schemas import SLocation
from ..models.models import LocationModels
from src.config.db.session import async_session_maker
import rollbar


class LocationRepository(AbstractRepository):
    def __init__(self):
        super().__init__(SLocation)

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
            try:
                query = select(LocationModels)
                result = await session.execute(query)
                locations = result.scalars().all()
                print(f"Locations fetched: {locations}")
                if not locations:
                    return []
                return [SLocation.model_validate(loc) for loc in locations]
            except Exception as e:
                rollbar.report_message(f"Error in LocationRepository.get_all: {e}")
                return []