import os

class Config:
    # Telegram Bot Token
    BOT_TOKEN = os.getenv("TG_BOT_TOKEN", "")

    # Warning auto-delete time (seconds)
    WARNING_DELETE_DELAY = int(os.getenv("WARNING_DELETE_DELAY", "5"))

    # Debug mode (True/False)
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
