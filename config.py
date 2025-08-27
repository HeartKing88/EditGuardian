import os

class Config:
    # Bot token (from BotFather)
    BOT_TOKEN = os.getenv("BOT_TOKEN", "8484447768:AAGj5TwSGne1XuWV26fEEPKPnl1I0IYq-TQ")

    # Owner info
    OWNER_ID = int(os.getenv("OWNER_ID", "7548614955"))  # apna Telegram numeric user_id daalo
    OWNER_NAME = os.getenv("OWNER_NAME", "")

    # Start image (url ya local file path)
    START_IMAGE = os.getenv("START_IMAGE", "https://files.catbox.moe/aud3y6.jpg")  # e.g. "https://i.imgur.com/xyz.png"

    # Support group/channel
    SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/Exampurrs")
    SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/FONT_CHANNEL_01")

    # Warning delete delay (seconds)
    WARNING_DELETE_DELAY = int(os.getenv("WARNING_DELETE_DELAY", "5"))

    # Debug mode
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
