import os

from dataclasses import dataclass
from pathlib import Path

from app.config.database import DatabaseConfig
from app.config.telegram import TelegramConfig


@dataclass
class Config:

    telegram: TelegramConfig
    database: DatabaseConfig

    @property
    def webhook_url(self) -> str:
        return f"{self.telegram.webhook_host}{self.telegram.webhook_path}"


def load_config() -> Config:

    telegram = TelegramConfig(
        bot_token=os.environ["BOT_TOKEN"],
        webhook_host=os.environ["WEBHOOK_HOST"],
        webhook_path=os.getenv("WEBHOOK_PATH", "/webhook"),
        webhook_secret=os.environ["WEBHOOK_SECRET"]
    )

    BASE_DIR = Path(__file__).resolve().parent
    database = DatabaseConfig(
        url=f"sqlite+aiosqlite:///{BASE_DIR / 'expenses.db'}"
    )

    return Config(
        telegram=telegram,
        database=database
    )
