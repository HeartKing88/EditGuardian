import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
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
    )
    
    # Create inline keyboard with buttons
    keyboard = [
        [
            InlineKeyboardButton("👑 Owner", url=f"tg://user?id={Config.OWNER_ID}"),
        ],
        [
            InlineKeyboardButton("📢 Support Channel", url=Config.SUPPORT_CHANNEL)],
            InlineKeyboardButton("💬 Support Group", url=Config.SUPPORT_GROUP),
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if Config.START_IMAGE:
        try:
            await update.message.reply_photo(
                photo=Config.START_IMAGE,
                caption=caption,
                parse_mode="Markdown",
                reply_markup=reply_markup
            )
        except Exception as e:
            logger.error("Failed to send start image: %s", e)
            await update.message.reply_text(
                text=caption,
                parse_mode="Markdown",
                reply_markup=reply_markup
            )
    else:
        await update.message.reply_text(
            text=caption,
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

# 📌 Handle edited messages
async def on_edited_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.edited_message
    if not msg:
        return
    user = msg.from_user
    try:
        await context.bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
        logger.info("Deleted edited message %s in chat %s", msg.message_id, msg.chat.id)
        if user:
            mention = f"[{user.first_name}](tg://user?id={user.id})"
            warning_text = f"⚠️ {mention}, edited messages are not allowed!"
            warning_msg = await context.bot.send_message(
                chat_id=msg.chat.id,
                text=warning_text,
                parse_mode="Markdown"
            )
            await asyncio.sleep(Config.WARNING_DELETE_DELAY)
            await context.bot.delete_message(chat_id=msg.chat.id, message_id=warning_msg.message_id)
    except Exception as e:
        logger.exception("Failed to handle edited message: %s", e)

# 📌 Main
def main():
    if not Config.BOT_TOKEN:
        raise RuntimeError("⚠️ Please set TG_BOT_TOKEN environment variable")

    app = ApplicationBuilder().token(Config.BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, on_edited_message))

    logger.info("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
