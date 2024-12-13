from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    ROLLBAR_TOKEN: str
    S3_ACCESS_KEY: str
    S3_SECRET_KEY: str
    S3_BUCKET_NAME: str
    S3_ENDPOINT_URL: str
    USER_SECRET_KEY: str
    DEFAULT_USERNAME: str
    DEFAULT_PASSWORD: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def ROLLBAR_ACCESS_TOKEN(self):
        return self.ROLLBAR_TOKEN

    @property
    def S3_ACCESS_KEY(self):
        return self.S3_ACCESS_KEY

    @property
    def S3_SECRET_KEY(self):
        return self.S3_SECRET_KEY

    @property
    def S3_BUCKET_NAME(self):
        return self.S3_BUCKET_NAME

    @property
    def S3_ENDPOINT_URL(self):
        return self.S3_ENDPOINT_URL

    @property
    def USER_SECRET_KEY(self):
        return self.USER_SECRET_KEY
    
    @property
    def DEFAULT_USERNAME(self):
        return self.DEFAULT_USERNAME

    @property
    def DEFAULT_PASSWORD(self):
        return self.DEFAULT_PASSWORD

    model_config = SettingsConfigDict(env_file=".env")


settings = Environment()
