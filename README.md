# 🚨 Telegram Edit Guard Bot

A Telegram moderation bot that **deletes all edited messages (text/media)** in groups and warns the user.  
The warning is also **auto-deleted** after a few seconds, keeping the chat clean.  

🔒 Perfect for:  
- Professional communities 👨‍💻👩‍💻  
- Spam-free groups 🚫  
- Preventing fake edits / scam forwards 🕵️‍♂️  

---

## ✨ Features
- 🗑️ Deletes **all edited messages** automatically  
- ⚠️ Sends **user-tagged warning** (auto-deletes after few seconds)  
- 🖼️ `/start` command with image + owner info + support group + channel  
- 🌍 Deploy anywhere (Heroku, Render, VPS, Docker, Local)  

---

## 🚀 Deploy

### 🔹 Deploy to Render
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/HeartKing88/EditGuardian)

### 🔹 Deploy to Heroku
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/HeartKing88/EditGuardian)

---

## ⚙️ Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Bot token from [@BotFather](https://t.me/BotFather) | ✅ |
| `OWNER_ID` | Numeric Telegram User ID of the bot owner | ✅ |
| `OWNER_NAME` | Owner display name (shown in /start) | ❌ |
| `START_IMAGE` | Optional image URL shown in /start | ❌ |
| `SUPPORT_GROUP` | Telegram support group link | ❌ |
| `SUPPORT_CHANNEL` | Telegram support channel link | ❌ |
| `WARNING_DELETE_DELAY` | Seconds after which warning auto-deletes (default 5) | ❌ |
| `DEBUG` | Enable debug logging (true/false) | ❌ |

---

## 🛠️ Local / VPS Setup

```bash
git clone https://github.com/<your-username>/telegram-edit-guard-bot.git
cd telegram-edit-guard-bot
pip install -r requirements.txt
python3 bot.py
