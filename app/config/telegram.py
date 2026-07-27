from dataclasses import dataclass


@dataclass(slots=True)
class TelegramConfig:
    bot_token: str
    webhook_host: str
    webhook_path: str
    webhook_secret: str

    @property
    def webhook_url(self) -> str:
        return f"{self.webhook_host}{self.webhook_path}"