from sqlalchemy import select
from .base_repository import AbstractRepository
from ..schemas.track_schemas import STrack
from ..models.models import TrackModels
from src.config.db.session import async_session_maker


class TrackRepository(AbstractRepository):
    def __init__(self):
        super().__init__(STrack)

    async def add_one(self, track: STrack) -> int:
        async with async_session_maker() as session:
            track_dict = track.model_dump()
            track_orm = TrackModels(**track_dict)
            session.add(track_orm)
            await session.flush()
            await session.commit()
            return track_orm.id

    async def get_one(self, track_id: int) -> STrack:
        async with async_session_maker() as session:
            result = await session.execute(select(TrackModels).filter(TrackModels.id == track_id))
            track = result.scalar_one_or_none()
            return track

    async def get_all(self, location_id: int) -> list[STrack]:
        async with async_session_maker() as session:
            result = await session.execute(select(TrackModels).filter_by(location_id=location_id))
            tracks = result.scalars().all()
            track_schemas = [STrack.model_validate(track) for track in tracks]
            return track_schemas
