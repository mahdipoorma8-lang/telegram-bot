from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

# 🔐 توکن بات
BOT_TOKEN = "8568471890:AAEWO_sW0z6pkV9E_6bOp6blD-TGlBJadvo"

# 🆔 آیدی عددی متین
TARGET_USER_ID = 7381379030

# 💬 جواب متن
TEXT_REPLY = "جهانیار سیکتیر کن"

# 🎤 جواب ویس
VOICE_REPLY = "کیرم تو صدات"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    user = update.message.from_user
    if not user or user.id != TARGET_USER_ID:
        return

    # 🧪 موقتی: گرفتن File ID گیف
    if update.message.animation:
        print("GIF FILE ID:", update.message.animation.file_id)

    # 🎤 اگر ویس بود
    if update.message.voice:
        await update.message.reply_text(
            VOICE_REPLY,
            reply_to_message_id=update.message.message_id
        )
        return

    # 💬 اگر متن بود
    if update.message.text:
        await update.message.reply_text(
            TEXT_REPLY,
            reply_to_message_id=update.message.message_id
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(
            (filters.TEXT | filters.VOICE | filters.ANIMATION) & ~filters.COMMAND,
            handle_message
        )
    )

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
