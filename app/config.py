import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    BOT_TOKEN: str
    WEBHOOK_HOST: str
    WEBHOOK_PATH: str
    WEBHOOK_SECRET: str

    @property
    def WEBHOOK_URL(self) -> str:
        return f"{self.WEBHOOK_HOST}{self.WEBHOOK_PATH}"


def load_config() -> Config:
    return Config(
        BOT_TOKEN=os.environ["BOT_TOKEN"],
        WEBHOOK_HOST=os.environ["WEBHOOK_HOST"],
        WEBHOOK_PATH=os.environ.get("WEBHOOK_PATH", "/webhook"),
        WEBHOOK_SECRET=os.environ.get("WEBHOOK_SECRET", "")
    )


BASE_DIR = Path(__file__).resolve().parent

DATABASE_URL = (
    f"sqlite+aiosqlite:///{BASE_DIR / 'expenses.db'}"
)