import gspread
import os
from dotenv import load_dotenv
load_dotenv()


gc = gspread.service_account(filename='maya-service-key.json')

sheets = gc.open_by_key(os.environ.get('G_LOG_ADDRESS'))

template_worksheet = sheets.get_worksheet(0)


def logThis(timestamp: str, task: str, milestone: str):
    try:
        date, time = timestamp.split(' ')
        category, _, work = task.partition(' ')
        new_row = [date, time, milestone, category.upper(), work]
        template_worksheet.append_row(new_row)
        return f"{category} for {milestone} is Logged"

    except Exception as e:
        return e
