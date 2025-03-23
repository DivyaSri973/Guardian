import os
from dotenv import load_dotenv

load_dotenv()  # Loads from .env

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
HR_EMAIL = os.getenv("HR_EMAIL")