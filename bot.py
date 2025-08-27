import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def on_edited_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.edited_message
    if not msg:
        return

    user = msg.from_user

    try:
        # ✅ Edited message delete
        await context.bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
        logger.info("Deleted edited message %s in chat %s", msg.message_id, msg.chat.id)

        # ✅ Warning bhejna (mention ke saath)
        if user:
            mention = f"[{user.first_name}](tg://user?id={user.id})"
            warning_text = f"⚠️ {mention}, edited messages are not allowed!"
            warning_msg = await context.bot.send_message(
                chat_id=msg.chat.id,
                text=warning_text,
                parse_mode="Markdown"
            )

            # ✅ Warning ko 5 seconds baad auto-delete karna
            await asyncio.sleep(5)
            await context.bot.delete_message(chat_id=msg.chat.id, message_id=warning_msg.message_id)

    except Exception as e:
        logger.exception("Failed to handle edited message: %s", e)

async def main():
    import os
    token = os.getenv("TG_BOT_TOKEN")
    if not token:
        raise RuntimeError("⚠️ Please set TG_BOT_TOKEN environment variable")

    app = ApplicationBuilder().token(token).build()

    # Handler for edited messages
    app.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, on_edited_message))

    logger.info("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
