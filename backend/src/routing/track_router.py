from src.config.db.session import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
import rollbar
from fastapi import APIRouter, Depends
from src.schemas.track_schemas import STrackAdd, STrackId
from src.repositories.track_repository import TrackRepository
from src.S3.s3_client import S3Client

track_router = APIRouter(
    prefix="/api/track",
    tags=["tracks"],
)


@track_router.post("", response_model=STrackId)
async def add_track(
    track: STrackAdd,
    db: AsyncSession = Depends(get_async_session)
) -> STrackId:
    try:
        s3 = S3Client()
        s3_url = s3.find_url_by_name(track.image_url)
        track.image_url = s3_url
        track_repository = TrackRepository()
        track_id = await track_repository.add_one(track)
        return STrackId(ok=True, track_id=track_id)
    except Exception as e:
        rollbar.report_message(f"Error in add_track: {e}")
        return []


@track_router.get("/{track_id}")
async def get_track(track_id: int):
    try:
        track_repository = TrackRepository()
        track = await track_repository.get_one(track_id)
        return track
    except Exception as e:
        rollbar.report_message(str(e))
        return -1
