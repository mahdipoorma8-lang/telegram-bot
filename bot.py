
print("TOKEN:", TOKEN)
import os
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.getenv("TOKEN")

# آیدی عددی کاربر مورد نظر
TARGET_USER_ID = 7381379030

# جواب ثابت
FIXED_REPLY = "جهانیار سیکتیر کن"

def handle_message(update, context):
    if not update.message:
        return

    user = update.message.from_user
    if user and user.id == TARGET_USER_ID:
        update.message.reply_text(
            FIXED_REPLY,
            reply_to_message_id=update.message.message_id
        )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
