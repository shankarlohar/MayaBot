import telebot
import os
from dotenv import load_dotenv
from botscripts import logscript
load_dotenv()


BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda msg: True)
def read_all(message):
    if message.text.startswith(('.', 'log', 'Log')):
        print(f"incomming->", end=' ')
        logMessage = logscript.logThis(message.text.partition(' ')[2])
        print(logMessage)
        bot.reply_to(message, logMessage)


if __name__ == '__main__':
    print("Bot Online")
    bot.infinity_polling()
