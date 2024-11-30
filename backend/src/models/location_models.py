from .base_models import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List
from src.models.track_models import TrackModels


class LocationModels(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]
    image_url: Mapped[str | None]
    track: Mapped[List["TrackModels"]] = relationship(
        back_populates="location",
    )

    def __repr__(self):
        return f"<LocationOrm(id={self.id}, name={self.name})>"
