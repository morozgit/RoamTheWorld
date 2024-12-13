from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)


class LocationModels(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))
    image_url: Mapped[str | None] = mapped_column(String(255))

    def __repr__(self):
        return f"<LocationModels(id={self.id}, name={self.name})>"


class TrackModels(Base):
    __tablename__ = "tracks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    short_description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    image_url: Mapped[str | None] = mapped_column(String(255), nullable=True)
    location_id: Mapped[int] = mapped_column(
        ForeignKey("locations.id", ondelete="CASCADE")
    )
    location: Mapped["LocationModels"] = relationship(
        "LocationModels"
    )

    def __repr__(self):
        return (
            f"<TrackModels(id={self.id}, "
            f"name={self.name}, "
            f"short_description={self.short_description}, "
            f"location_id={self.location_id})>"
        )
