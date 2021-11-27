"""
Simple Telegram bot to reply messages

Example taken from:
https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot.py

Bot is enhanced with dialog handler based on state machine custom subclass 

"""

import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from mealbot.machine import PizzaBot
import config


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def response(update: Update, context: CallbackContext) -> None:
    """Conversation with user, using custom state machine."""
    
    # Use chat id to distinguish handler instance
    bot_machine = PizzaBot(bot_id=update.message.chat.id)
    
    # Simple utilize instance method, responses are depends of current state
    response = bot_machine.on_message(update.message.text)
    update.message.reply_text(response)
    

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    
    updater = Updater(config.TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, response))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()