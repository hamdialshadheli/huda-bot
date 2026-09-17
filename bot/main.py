print("A - Python started", flush=True)
import os

from dotenv import load_dotenv
from telegram import (
    Update,
    InlineKeyboardButton,
١    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "📖 القرآن والثقافة",
                callback_data="quran"
            ),
            InlineKeyboardButton(
                "📚 الملازم",
                callback_data="malzam"
            ),
        ],
        [
            InlineKeyboardButton(
                "🎧 المحاضرات",
                callback_data="lectures"
            ),
            InlineKeyboardButton(
                "ℹ️ عن البوت",
                callback_data="about"
            ),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🌿 أهلاً بك في بوت هدى للناس\n\n"
        "اختر من القائمة:",
        reply_markup=reply_markup,
    )


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()

    if query.data == "quran":
        text = "📖 قسم القرآن والثقافة\n\nسيتم إضافة المحتوى هنا."

    elif query.data == "malzam":
        text = "📚 قسم الملازم\n\nسيتم إضافة الملازم هنا."

    elif query.data == "lectures":
        text = "🎧 قسم المحاضرات\n\nسيتم إضافة المحاضرات هنا."

    elif query.data == "about":
        text = (
            "ℹ️ عن بوت هدى للناس\n\n"
            "منصة ثقافية قيد التطوير."
        )

    else:
        text = "❌ خيار غير معروف."

    await query.edit_message_text(text=text)


def main():
    print("B - Entered main", flush=True)

    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN غير موجود")

    print("C - Token found", flush=True)

    app = Application.builder().token(BOT_TOKEN).build()

    print("D - Application created", flush=True)

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("E - Starting polling", flush=True)

    app.run_polling()

        print("F - Bot stopped", flush=True)


if __name__ == "__main__":
    main()
