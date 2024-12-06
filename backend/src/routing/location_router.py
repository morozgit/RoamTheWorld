from src.schemas.location_schemas import SLocationAdd, SLocationId, SLocation
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.location_repository import LocationRepository
from src.repositories.track_repository import TrackRepository
from fastapi import APIRouter, Depends
from src.config.db.session import get_async_session
import rollbar
from src.S3.s3_client import S3Client

location_router = APIRouter(
    prefix="/api/location",
    tags=["locations"],
)


@location_router.post("", response_model=SLocationId)
async def add_location(
    location: SLocationAdd, db: AsyncSession = Depends(get_async_session)
) -> SLocationId:
    try:
        s3 = S3Client()
        s3_url = s3.find_url_by_name(location.image_url)
        location.image_url = s3_url
        location_repository = LocationRepository()
        location_id = await location_repository.add_one(location)
        return SLocationId(ok=True, location_id=location_id)
    except Exception as e:
        rollbar.report_message(f"Error in add_location: {e}")
        return -1


@location_router.get("/all_locations")
async def get_all_locations(
    db: AsyncSession = Depends(get_async_session),
) -> list[SLocation]:
    try:
        print("get_all_locations")
        repository = LocationRepository()
        print("repository", repository)
        locations = await repository.get_all()
        return locations
    except Exception as e:
        rollbar.report_message(f"Error in get_all_locations: {e}")
        print(e)
        return []



@location_router.get("/{location_id}")
async def get_location(location_id: int):
    try:
        tracks = await TrackRepository.get_location_tracks(location_id)
        return tracks
    except Exception as e:
        rollbar.report_message(f"Error in get_location: {e}")
        return []
