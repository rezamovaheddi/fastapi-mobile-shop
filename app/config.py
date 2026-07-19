from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str

    class Config:
        env_file = ".env"


setting = Setting()
