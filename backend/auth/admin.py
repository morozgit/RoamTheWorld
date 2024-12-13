from sqladmin import ModelView
from src.models.models import User
from .auth import BasicAuth
from src.config.environment import settings
from src.models.models import LocationModels, TrackModels
from src.S3.s3_client import S3Client


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name]


auth_backend = BasicAuth(
    secret_key=settings.USER_SECRET_KEY,
    default_username=settings.DEFAULT_USERNAME,
    default_password=settings.DEFAULT_PASSWORD
)


class S3ModelView(ModelView):
    async def on_model_change(self, data, model, is_created, request):
        s3_client = S3Client()

        if data['image_url']:
            s3_url = s3_client.find_url_by_name(data['image_url'])
            if s3_url:
                data['image_url'] = s3_url
                print('on_model_change', data['image_url'])
            else:
                raise ValueError(f"Image with name {data['image_url']} not found in S3.")


class LocationAdmin(S3ModelView, model=LocationModels):
    column_list = ["id", "name", "description", "image_url"]


class TrackAdmin(S3ModelView, model=TrackModels):
    column_list = ["id", "name", "short_description", "image_url", "location_id", "description"]
