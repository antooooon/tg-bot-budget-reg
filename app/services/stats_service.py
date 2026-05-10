from traceback import format_stack

from app.db.session import async_session
from app.repositories.stats_repo import StartRepository
from app.formatters.stats_formatters import format_stats


class StatsService:

    async def get_stats(self, user_id: int):

        async with async_session() as session:

            repo = StartRepository(session=session)

            stats = await repo.get_stats(user_id=user_id)

            if not stats:
                return "Нет данных"

            return format_stats(stats)



