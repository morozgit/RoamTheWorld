from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_models import Base
from .location_models import LocationModels


class TrackModels(Base):
    __tablename__ = "tracks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    short_description: Mapped[str | None]
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    image: Mapped[str | None]
    location_id: Mapped[int] = mapped_column(
        ForeignKey("locations.id", ondelete="CASCADE")
    )
    location: Mapped["LocationModels"] = relationship(
        back_populates="track",
    )

    def __repr__(self):
        return f"<TrackModels(id={self.id}, \
                name={self.name}, \
                short_description={self.short_description}, \
                location_id={self.location_id})>"
