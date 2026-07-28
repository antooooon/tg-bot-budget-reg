from aiogram import Dispatcher

from app.handlers.start import router as start_router
from app.handlers.stats import router as stats_router
from app.handlers.settings import router as settings_router
from app.handlers.common import router as common_router
from app.handlers.banking import router as banking_router
from app.handlers.expenses_inline import router as expenses_router


def create_dispatcher() -> Dispatcher:

    dp = Dispatcher()

    dp.include_router(expenses_router)
    dp.include_router(start_router)
    dp.include_router(stats_router)
    dp.include_router(settings_router)
    dp.include_router(common_router)
    dp.include_router(banking_router)

    return dp