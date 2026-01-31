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
VOICE_REPLY = "ویس نده بابا تایپ کن 😐"

# 🎬 جواب گیف/ویدیو (File ID که گرفتی)
VIDEO_REPLY_ID = "FILE_ID_ویدیو_اینجا"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    user = update.message.from_user
    if not user or user.id != TARGET_USER_ID:
        return

    msg = update.message

    # 🎬 اگر ویدیو (گیف تلگرامی)
    if msg.video:
        await msg.reply_video(
            video=VIDEO_REPLY_ID,
            reply_to_message_id=msg.message_id
        )
        return

    # 🎤 اگر ویس
    if msg.voice:
        await msg.reply_text(
            VOICE_REPLY,
            reply_to_message_id=msg.message_id
        )
        return

    # 💬 اگر متن
    if msg.text:
        await msg.reply_text(
            TEXT_REPLY,
            reply_to_message_id=msg.message_id
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(
            (filters.TEXT | filters.VOICE | filters.VIDEO) & ~filters.COMMAND,
            handle_message
        )
    )

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
