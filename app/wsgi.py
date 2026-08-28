import asyncio
import sys
from dotenv import load_dotenv


load_dotenv()

sys.path.insert(
    0,
    ""
)

from app.web.webhook import flask_app, initialize

asyncio.run(initialize())

application = flask_app
