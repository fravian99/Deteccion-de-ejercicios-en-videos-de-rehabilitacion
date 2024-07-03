from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

@lru_cache
def get_settings():
    return Settings()

class Settings(BaseSettings):
    PRODUCTION: bool = False

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    FIRST_SUPERUSER: str
    FIRST_SUPERUSER_PASSWORD: str
    ADMIN_ROLE: str
    CAN_EDIT_ROLES: list

    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )

settings = get_settings()
print(settings)
