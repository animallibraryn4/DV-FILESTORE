from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Define your token (replace with actual token)
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

def start(update: Update, context):
    user = update.message.from_user
    keyboard = [
        [InlineKeyboardButton("💝 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url='https://t.me/your_support_group'),
         InlineKeyboardButton("🛒 buy now", url='https://your_buy_link.com')],
        [InlineKeyboardButton("🔗 Share", switch_inline_query="")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(f"Hello {user.first_name}, welcome to the bot! Choose an option:", reply_markup=reply_markup)

def about(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("💻 Developers", url="https://t.me/your_developer_profile"),
         InlineKeyboardButton("🔙 Back", callback_data='back_to_start')],
        [InlineKeyboardButton("👥 Join Us", url="https://t.me/your_group_link")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("This is the about page! You can learn more about the bot here:", reply_markup=reply_markup)

def button(update: Update, context):
    query = update.callback_query
    query.answer()
    if query.data == "back_to_start":
        start(update, context)  # Go back to the start page

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('about', about))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
