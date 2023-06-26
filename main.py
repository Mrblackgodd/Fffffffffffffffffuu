import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Define your bot token
TOKEN = 6158242764:AAH7Ynhh-_Vartl_5NZksXFPI_9QSYzfw-w

# Define the directory where files will be stored
FILES_DIR = 'files'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Welcome to the File Store Bot! Send me any file and I'll store it for you.")

def store_file(update, context):
    file = update.message.document
    file_name = os.path.join(FILES_DIR, file.file_name)
    file.get_file().download(file_name)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="File stored successfully!")

def main():
    # Create the files directory if it doesn't exist
    os.makedirs(FILES_DIR, exist_ok=True)

    # Create the Telegram Updater and dispatcher
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register the handlers
    start_handler = CommandHandler('start', start)
    store_file_handler = MessageHandler(Filters.document, store_file)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(store_file_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
