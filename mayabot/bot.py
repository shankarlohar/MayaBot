import telebot
import os
from dotenv import load_dotenv
from botscripts import logscript
from datetime import datetime
import pytz

load_dotenv()


BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda msg: True)
def read_all(message):
    if message.text.startswith(('.', 'log', 'Log')):

        timestamp = datetime.fromtimestamp(
            message.date, tz=pytz.utc).astimezone(pytz.timezone('Asia/Kolkata'))

        print(f"{timestamp}", end=' ')
        logMessage = logscript.logThis(
            str(timestamp), message.text.partition(' ')[2])
        print(logMessage)
        bot.reply_to(message, f"{logMessage}")


if __name__ == '__main__':
    print("Bot Online")
    bot.infinity_polling()
