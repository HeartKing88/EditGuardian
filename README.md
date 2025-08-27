# Telegram Edit Guard Bot

This bot deletes **all edited messages (text/media)** in a Telegram group and warns the user.
The warning itself is auto-deleted after 5 seconds.

## 🚀 Features
- Deletes all edited messages
- Warns tagged user
- Warning auto-deletes after 5s
- Works for admins & members both
- Deployable anywhere (Local, VPS, Render, Heroku, Docker)

---

## 🖥 Local Run
```bash
pip install -r requirements.txt
export TG_BOT_TOKEN="123456:ABC-DEF-your_token"
python bot.py
