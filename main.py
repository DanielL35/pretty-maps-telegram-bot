import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import os
from generate_maps import generate_png

load_dotenv()
# get environment variables
PORT = int(os.environ.get('PORT', 8443))
TOKEN = os.environ.get('TOKEN')

RUN_LOCAL = True

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def make_map(update, context):
    """send the map"""
    msg_in = update.message
    x = msg_in.location.longitude
    y = msg_in.location.latitude
    msg = "Your location is {}, {}".format(x, y)
    update.message.reply_text(msg)
    print("generating map..")
    filename = generate_png((x,y))
    print("map generated and saved under {}".format(filename))
    img = open(filename + ".png", 'rb')
    update.message.reply_photo(img)
    #os.chdir("cache")
    #[os.remove(f) for f in os.listdir()]
    logger.warning('Update "%s" hit /map ', update)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on location get the geo coordinates
    dp.add_handler(MessageHandler(Filters.location,
                              make_map,
                              pass_user_data=True))
       
    # log all errors
    dp.add_error_handler(error)
   
    if RUN_LOCAL:
        updater.start_polling()
    else:
        updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN,
                      webhook_url='https://telbot-polling.onrender.com/' + TOKEN)
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
