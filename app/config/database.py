from dataclasses import dataclass


@dataclass(slots=True)
class DatabaseConfig:
    url: str

# @dataclass
# class DatabaseConfig:
#     BASE_DIR: str                | говорит dataclass:"у объекта будет поле BASE_DIR"
#     DATABASE_URL: str
#
#     BASE_DIR = Path(__file__).resolve().parent        ты создаешь атрибут класса, а не поле экземпляра.
#     DATABASE_URL = (
#         f"sqlite+aiosqlite:///{BASE_DIR / 'expenses.db'}"
#     )