from slack_bolt.adapter.socket_mode import SocketModeHandler
from app.event_handlers import app
from app.config import SLACK_APP_TOKEN

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()