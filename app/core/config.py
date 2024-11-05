from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: str
    database_host: str
    database_port: int
    database_user: str
    database_password: str
    database_name: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
