from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات پیکسیم فعاله ✅")


TOKEN = os.getenv("8761878376:AAFZ32BXX1gzUseWIqv1lRtOT1JmsJltoS4")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
