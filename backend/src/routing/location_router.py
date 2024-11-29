from fastapi import APIRouter

location_router = APIRouter(
    prefix="/api/location",
    tags=["locations"],
)


@location_router.get("/all_locations")
async def get_all_locations():
    return [
        {
            "id": 1,
            "name": "Локация 1",
            "description": "Описание 1",
            "image": "location1.jpg",
        },
        {
            "id": 2,
            "name": "Локация 2",
            "description": "Описание 2",
            "image": "location2.jpg",
        },
        {
            "id": 3,
            "name": "Локация 3",
            "description": "Описание 3",
            "image": "location3.jpg",
        },
    ]
