from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = "8568471890:AAEWO_sW0z6pkV9E_6bOp6blD-TGlBJadvo"

TARGET_USER_ID = 7381379030

TEXT_REPLY = "جهانیار سیکتیر کن"
VOICE_REPLY = "کیرم تو صدات"

# اینجا File ID ذخیره می‌شه
VIDEO_REPLY_ID = None


async def set_gif(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global VIDEO_REPLY_ID

    user = update.message.from_user
    if user.id != TARGET_USER_ID:
        return

    if not update.message.reply_to_message:
        await update.message.reply_text("روی ویدیو ریپلای کن بعد /setgif بزن")
        return

    replied = update.message.reply_to_message

    if not replied.video:
        await update.message.reply_text("این ویدیو نیست")
        return

    VIDEO_REPLY_ID = replied.video.file_id
    await update.message.reply_text("✅ گیف/ویدیو ذخیره شد")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    msg = update.message
    user = msg.from_user

    if not user or user.id != TARGET_USER_ID:
        return

    # 🎬 اگر ویدیو فرستاد → گیف خاص
    if msg.video and VIDEO_REPLY_ID:
        await msg.reply_video(
            video=VIDEO_REPLY_ID,
            reply_to_message_id=msg.message_id
        )
        return

    # 🎤 ویس
    if msg.voice:
        await msg.reply_text(
            VOICE_REPLY,
            reply_to_message_id=msg.message_id
        )
        return

    # 💬 متن
    if msg.text:
        await msg.reply_text(
            TEXT_REPLY,
            reply_to_message_id=msg.message_id
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("setgif", set_gif))
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
