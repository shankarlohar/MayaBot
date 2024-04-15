import telebot
import os
from dotenv import load_dotenv
from botscripts import logscript
load_dotenv()


BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda msg: True)
def read_all(message):
    if message.text.startswith('.', 'log', 'Log'):
        logMessage = logscript.logThis(message.text[3:])
        print(logMessage)
        bot.reply_to(message, logMessage)


bot.infinity_polling()
