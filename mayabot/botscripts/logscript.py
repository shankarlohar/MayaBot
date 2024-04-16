import gspread
import os
from dotenv import load_dotenv
load_dotenv()


gc = gspread.service_account(filename='maya-service-key.json')

sheets = gc.open_by_key(os.environ.get('G_LOG_ADDRESS'))

template_worksheet = sheets.get_worksheet(0)


def logThis(timestamp: str, task: str):
    try:
        date_str, time_str = timestamp.split(' ')
        new_row = [date_str, time_str, task]
        template_worksheet.append_row(new_row)
        return "Logged"

    except Exception as e:
        return e
