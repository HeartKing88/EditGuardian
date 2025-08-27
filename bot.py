import logging
import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    CommandHandler,
    filters
)
from config import Config

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 📌 /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    caption = (
        f"👋 Hello {user.mention_markdown()},\n\n"
        f"🚨 *This is Edit Guard Bot!*\n"
        f"🗑️ All edited messages will be deleted.\n"
        f"⚠️ Warning will be shown and auto-deleted.\n\n"
        f"👑 *Owner*: [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})\n"
        f"💬 *Support Group*: {Config.SUPPORT_GROUP}\n"
        f"📢 *Support Channel*: {Config.SUPPORT_CHANNEL}"
    )

    if Config.START_IMAGE:
        try:
            await update.message.reply_photo(
                photo=Config.START_IMAGE,
                caption=caption,
                parse_mode="Markdown"
            )
        except Exception as e:
            logger.error("Failed to send start image: %s", e)
            await update.message.reply_text(caption, parse_mode="Markdown")
    else:
        await update.message.reply_text(caption, parse_mode="Markdown")

# 📌 Handle edited messages
async def on_edited_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.edited_message
    if not msg:
        return

    user = msg.from_user

    try:
        # 🗑️ Edited message delete
        await context.bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
        logger.info("Deleted edited message %s in chat %s", msg.message_id, msg.chat.id)

        # ⚠️ Warning bhejna
        if user:
            mention = f"[{user.first_name}](tg://user?id={user.id})"
            warning_text = f"⚠️ {mention}, edited messages are not allowed!"
            warning_msg = await context.bot.send_message(
                chat_id=msg.chat.id,
                text=warning_text,
                parse_mode="Markdown"
            )

            # ⏳ Warning ko X sec baad auto-delete
            await asyncio.sleep(Config.WARNING_DELETE_DELAY)
            await context.bot.delete_message(chat_id=msg.chat.id, message_id=warning_msg.message_id)

    except Exception as e:
        logger.exception("Failed to handle edited message: %s", e)

# 📌 Main entrypoint
async def main():
    if not Config.BOT_TOKEN:
        raise RuntimeError("⚠️ Please set TG_BOT_TOKEN environment variable")

    app = ApplicationBuilder().token(Config.BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, on_edited_message))

    logger.info("Bot is running...")
    await app.initialize()  # Initialize the application
    await app.start()       # Start the application
    await app.run_polling() # Run polling
    await app.stop()        # Stop the application
    await app.shutdown()    # Shutdown the application

if __name__ == "__main__":
    try:
        # Check if an event loop is already running
        loop = asyncio.get_event_loop()
        if loop.is_running():
            logger.warning("Event loop is already running. Running main() in existing loop.")
            loop.create_task(main())
        else:
            asyncio.run(main())
    except RuntimeError as e:
        if "no running event loop" in str(e):
            logger.info("No running event loop found. Starting new event loop.")
            asyncio.run(main())
        else:
            logger.error("Unexpected error: %s", e)
            raise
