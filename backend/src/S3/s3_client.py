import boto3
from src.config.environment import settings


class S3Client:
    def __init__(self):
        self.client = boto3.client(
            service_name="s3",
            endpoint_url=settings.S3_ENDPOINT_URL,
            aws_access_key_id=settings.S3_ACCESS_KEY,
            aws_secret_access_key=settings.S3_SECRET_KEY,
        )

    def list_obj_urls(self):
        contents = self.client.list_objects(Bucket=settings.S3_BUCKET_NAME).get(
            "Contents", []
        )
        return [
            f"{settings.S3_ENDPOINT_URL}/{settings.S3_BUCKET_NAME}/{content['Key']}"
            for content in contents
        ]

    def find_url_by_name(self, filename):
        public_urls = self.list_obj_urls()
        for url in public_urls:
            if filename in url:
                return url
        return None
