# Telegram Expense/Income Tracker

Проект в первую очередь предназначен для демонстрации backend-разработки

Бот для контроля расходов и отслеживания доходов в разрезе категорий.
Есть возможность посмотреть статистику и вести учет в разрезе бюджета.
Бюджет задается в настройках или используется по умолчанию.


Features
- учет доходов и расходов
- категоризация операций
- статистика по категориям
- настройка бюджета на определенный период
- парсинг данных из банковских SMS


## Tech Stack
- Python
- aiogram   - Telegram Bot API
- FastAPI   - health-check endpoint
- SQLite    - база данных
- SQLAlchemy - ORM и работа с базой данных
- Pydantic  - валидация и схемы данных
- Flask     - webhook / deployment adapter


## Architecture
Telegram Bot
   ↓
Handlers        — обработка Telegram updates
   ↓
Services        — бизнес-логика
   ↓
Repositories    — работа с БД
   ↓
SQLAlchemy
   ↓
SQLite

Такое разделение позволяет отделить Telegram-логику от бизнес-логики и работы с базой данных,
что упрощает дальнейшее развитие и тестирование проекта.


## Project Structure
app/
├── bot/            # инициализация бота и диспетчера
├── config/         # конфигурация приложения
├── db/             # модели, engine и инициализация БД
├── formatters/     # форматирование сообщений
├── handlers/       # Telegram handlers и keyboards
├── parsers/        # парсинг банковских SMS
├── repositories/   # работа с данными и запросами к БД
├── schemas/        # Pydantic-схемы для валидации и передачи данных
├── services/       # бизнес-логика приложения
├── utils/          # вспомогательные функции и расчеты
└── web/            # webhook и endpoints


## Getting Started
1. Clone repository
    git clone https://github.com/antooooon/tg-bot-budget-reg.git
    cd tg-bot-budget-reg

2. Create virtual environment
    Windows:
        python -m venv .venv
        .venv\Scripts\activate
    Linux / macOS:
        python3 -m venv .venv
        source .venv/bin/activate

3. Install dependencies
    pip install -r requirements.txt

4. Create `.env`
    Create a .env file in the project root:
        BOT_TOKEN=your_telegram_bot_token

5. Run application
    python main.py


## Environment Variables
BOT_TOKEN="your_telegram_bot_token"
Другие переменные окружения зависят от конфигурации приложения.


## Screenshots
Coming soon.


## What I Learned
В процессе разработки проекта я:
- разобрался с aiogram и обработкой Telegram updates;
- изучил работу с async SQLAlchemy;
- разобрался с жизненным циклом database sessions и транзакциями;
- изучил разделение приложения на handlers, services и repositories;
- получил практический опыт работы с SQL-запросами через ORM;
- применил принципы ООП при проектировании архитектуры;
- попробовал webhook-based deployment на PythonAnywhere;
- получил практический опыт отладки приложения в локальной и серверной среде.


## Future Improvements
- добавить автоматические тесты
- добавить настройку пользовательских категорий
- возможность вести бюджет в разрезе нескольких пользователей
- добавит календарь ближайших событий
- улучшить production deployment
