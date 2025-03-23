import os
from dotenv import load_dotenv

load_dotenv()  # Loads from .env

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")