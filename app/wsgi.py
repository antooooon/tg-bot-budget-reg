import sys

sys.path.insert(
    0,
    "/home/antoonka/tg-bot-budget-reg"
)

from web.webhook import flask_app

application = flask_app