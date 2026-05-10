
class StartRepository():

    def __init__(self, session):
        self.session = session

    async def get_stats(self, user_id: int):

        result = self.session.execute(

        )

        return result.all()