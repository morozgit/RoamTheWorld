from .base_repository import AbstractRepository
from ..schemas.location_schemas import SLocation
from ..models.location_models import LocationModels
from sqlalchemy import select


class LocationRepository(AbstractRepository):
    async def find_all(cls) -> list[SLocation]:
        query = select(LocationModels)
        location_models, location_dicts = await cls._execute_query(query)
        if not location_dicts:
            return []
        location_schemas = [
            SLocation.model_validate(loc_dict) for loc_dict in location_dicts
        ]
        return location_schemas
