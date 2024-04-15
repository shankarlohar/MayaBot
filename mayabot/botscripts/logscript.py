import pytz
import datetime
import gspread
import os
from dotenv import load_dotenv
load_dotenv()


gc = gspread.service_account(filename='maya-service-key.json')

sheets = gc.open_by_key(os.environ.get('G_LOG_ADDRESS'))

template_worksheet = sheets.get_worksheet(0)


def logThis(task: str):
    try:
        utc_now = datetime.datetime.now(datetime.UTC)
        local_now = utc_now.astimezone(pytz.timezone('Asia/Kolkata'))
        date_str = local_now.strftime("%d/%m/%Y")
        time_str = local_now.strftime("%H:%M:%S")
        new_row = [date_str, time_str, task]
        template_worksheet.append_row(new_row)
        return "Done"

    except Exception as e:
        return e
