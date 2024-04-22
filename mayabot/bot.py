from telebot import TeleBot, types
import os
from dotenv import load_dotenv
from botscripts import logscript
from datetime import datetime
import pytz

load_dotenv()


BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = TeleBot(BOT_TOKEN)


milestone_list = [
    "Thought", "GATE→IITB", "Understanding Business and Finance", "Bodyweight Fitness Progressions", "Exploring Singing and Music", "Adapting to Kamasutra", "Todo", "To Fix"
]


@bot.message_handler(func=lambda msg: True)
def read_all(message):
    if message.text.startswith(('. ', 'log ', 'Log ')):

        timestamp = datetime.fromtimestamp(
            message.date, tz=pytz.utc).astimezone(pytz.timezone('Asia/Kolkata'))

        user_data = message.text.partition(' ')
        user_data = user_data[2].partition(' ')
        milestone, task = user_data[0], user_data[2]

        print(f"{timestamp}", end=' ')
        logMessage = logscript.logThis(
            str(timestamp), task, milestone_list[int(milestone)]
        )
        print(logMessage)
        bot.reply_to(message, f"{logMessage}")

    elif message.text.startswith(('..', 'milestones', 'Milestones')):
        for index, item in enumerate(milestone_list, start=0):
            bot.send_message(message.chat.id, f"{index}. {item}")
        bot.send_message(message.chat.id, f"done")


if __name__ == '__main__':
    print("Bot Online")
    bot.infinity_polling()
