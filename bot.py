import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN", "8863529261:AAETqI4dolU6k-9eIxOPIxr3FL97xb9gDhg")
SUB_URL = "https://raw.githubusercontent.com/eternal60123-cell/proxi/refs/heads/main/sub.txt"

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton("⚡ Подключиться", url=f"happ://add/{SUB_URL}")
    ]])
    await update.message.reply_text(
        "👋 Добро пожаловать в *Eternal VPN*\n\n"
        "Нажмите кнопку ниже чтобы добавить подписку в приложение Happ\\.",
        parse_mode="MarkdownV2",
        reply_markup=kb
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
