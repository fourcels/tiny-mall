import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Tiny Mall API"
    database_url: str
    admin_username: str = 'admin'
    admin_password: str = 'admin'
    secret_key: str
    access_token_expire_minutes = 120

    class Config:
        env_file = ".env"


settings = Settings()
