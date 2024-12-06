from pydantic import BaseModel, Field


class SLocationAdd(BaseModel):
    name: str = Field(..., description="Название локации")
    description: str = Field(..., description="Краткое описание локации")
    image_url: str = Field(..., description="Ссылка на изображение локации")


class SLocation(SLocationAdd):
    id: int

    model_config = {
        "from_attributes": True
    }


class SLocationId(BaseModel):
    ok: bool = True
    location_id: int
