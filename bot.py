import os
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = "8568471890:AAEWO_sW0z6pkV9E_6bOp6blD-TGlBJadvo"


TARGET_USER_ID = 7381379030
FIXED_REPLY = "جهانیار سیکتیر کن"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    user = update.message.from_user
    if user and user.id == TARGET_USER_ID:
        await update.message.reply_text(
            FIXED_REPLY,
            reply_to_message_id=update.message.message_id
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    app.run_polling()

if __name__ == "__main__":
    main()
