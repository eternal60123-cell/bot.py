import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8863529261:AAETqI4dolU6k-9eIxOPIxr3FL97xb9gDhg"
SUB_URL = "https://raw.githubusercontent.com/eternal60123-cell/proxi/refs/heads/main/sub.txt"
SUPPORT = "https://t.me/permanentlyyy"

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

SERVERS = [
    ("🇫🇮", "Финляндия",  "Helsinki",  "2 сервера"),
    ("🇵🇱", "Польша",     "Warsaw",    "2 сервера"),
    ("🇨🇿", "Чехия",      "Prague",    "1 сервер"),
    ("🇯🇵", "Япония",     "Tokyo",     "1 сервер"),
    ("🇰🇿", "Казахстан",  "Almaty",    "1 сервер"),
    ("🇩🇪", "Германия",   "Berlin ⚡", "2 сервера"),
]

def main_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⚡ Подключиться", callback_data="connect")],
        [InlineKeyboardButton("🌍 Серверы", callback_data="servers"),
         InlineKeyboardButton("📖 Инструкция", callback_data="howto")],
        [InlineKeyboardButton("💬 Поддержка", url=SUPPORT)],
    ])

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ *Добро пожаловать в Eternal VPN*\n\n"
        "Высокоскоростной VPN с серверами в 5 странах\\.\n"
        "Без логов\\. Без регистрации\\. Бесплатно\\.\n\n"
        "📊 *Статистика:*\n"
        "├ Серверов: 9\n"
        "├ Стран: 5\n"
        "├ Трафик: безлимит\n"
        "└ Логи: отсутствуют\n\n"
        "Выберите действие ниже 👇",
        parse_mode="MarkdownV2",
        reply_markup=main_kb()
    )

async def button(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    d = q.data

    if d == "connect":
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("🍎 App Store (iPhone)", url="https://apps.apple.com/app/happ-proxy-utility/id6504287215")],
            [InlineKeyboardButton("🤖 Google Play (Android)", url="https://play.google.com/store/apps/details?id=com.happproxy")],
            [InlineKeyboardButton("◀️ Назад", callback_data="back")],
        ])
        await q.edit_message_text(
            "⚡ *Подключение к Eternal VPN*\n\n"
            "*Шаг 1* — Скачайте приложение *Happ*\n\n"
            "*Шаг 2* — Откройте Happ, затем нажмите кнопку ниже:\n\n"
            f"`{SUB_URL}`\n\n"
            "_Или скопируйте ссылку и добавьте вручную в Happ → \\+ → Добавить подписку_",
            parse_mode="MarkdownV2",
            reply_markup=kb
        )

    elif d == "servers":
        lines = "\n".join(
            f"{flag} *{name}* — {city} \\| {count}"
            for flag, name, city, count in SERVERS
        )
        kb = InlineKeyboardMarkup([[InlineKeyboardButton("◀️ Назад", callback_data="back")]])
        await q.edit_message_text(
            "🌍 *Серверы Eternal VPN*\n\n"
            "Все серверы онлайн 🟢\n\n"
            + lines +
            "\n\n_Серверы обновляются автоматически_",
            parse_mode="MarkdownV2",
            reply_markup=kb
        )

    elif d == "howto":
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("⚡ Подключиться", callback_data="connect")],
            [InlineKeyboardButton("◀️ Назад", callback_data="back")],
        ])
        await q.edit_message_text(
            "📖 *Инструкция по подключению*\n\n"
            "*1\\.* Скачайте приложение *Happ*\n"
            "   └ App Store или Google Play\n\n"
            "*2\\.* Нажмите кнопку *«Подключиться»*\n"
            "   └ Happ откроется автоматически\n\n"
            "*3\\.* Подтвердите добавление подписки\n"
            "   └ Все серверы загрузятся сразу\n\n"
            "*4\\.* Выберите сервер и нажмите подключить\n"
            "   └ Готово\\!\n\n"
            "❓ Если не работает — напишите в поддержку",
            parse_mode="MarkdownV2",
            reply_markup=kb
        )

    elif d == "back":
        await q.edit_message_text(
            "⚡ *Добро пожаловать в Eternal VPN*\n\n"
            "Высокоскоростной VPN с серверами в 5 странах\\.\n"
            "Без логов\\. Без регистрации\\. Бесплатно\\.\n\n"
            "📊 *Статистика:*\n"
            "├ Серверов: 9\n"
            "├ Стран: 5\n"
            "├ Трафик: безлимит\n"
            "└ Логи: отсутствуют\n\n"
            "Выберите действие ниже 👇",
            parse_mode="MarkdownV2",
            reply_markup=main_kb()
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
