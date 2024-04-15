import pandas as pd
from datetime import date, datetime, timedelta
from astral.sun import sun
from astral.location import Location
from astral import LocationInfo
import gspread
import os
from dotenv import load_dotenv
load_dotenv()


gc = gspread.service_account(filename='maya-service-key.json')

sheets = gc.open_by_key(os.environ.get('G_SHEET_KEY'))

template_worksheet = sheets.get_worksheet(0)

city = LocationInfo(
    name='Kolkata',
    region='West Bengal, India',
    timezone='Asia/Kolkata',
    latitude=22.572646,
    longitude=88.363895,
)
kolkata = Location(city)
print((
    f"Information for {kolkata.name}/{kolkata.region}\n"
    f"Timezone: {kolkata.timezone}\n"
    f"Latitude: {kolkata.latitude:.02f}; Longitude: {kolkata.longitude:.02f}\n"
))


def extractTime(time):
    return datetime.strftime(time, "%H:%M:%S")


def to_seconds(dtime):
    stime = [int(val) for val in extractTime(dtime).split(':')]
    return 60*60*stime[0] + 60*stime[1] + stime[2]


s = sun(kolkata.observer, date=date(
    year=2024, month=4, day=4), tzinfo=kolkata.timezone)

dawn = s["dawn"]
sunrise = s["sunrise"]
sunset = s["sunset"]
dusk = s["dusk"]


print((
    f'Dawn:    {dawn}\n\n'
    f'Sunrise: {sunrise}\n\n'
    f'Sunset:  {sunset}\n\n'
    f'Dusk:    {dusk}\n\n'
))


dataframe = pd.DataFrame(template_worksheet.get_all_records())


def delta(multiplier):
    if multiplier < 0:
        return sunrise - timedelta(hours=0, minutes=abs(multiplier)*48)
    return sunrise + timedelta(hours=0, minutes=abs(multiplier)*48)


for i, row in enumerate(dataframe.iterrows()):
    row[1][2] = delta(row[1][4])
    row[1][3] = row[1][2] + timedelta(hours=0, minutes=48)
    dataframe.iloc[i, 1] = extractTime(row[1][2])
    dataframe.iloc[i, 2] = extractTime(row[1][3])

template_worksheet.update(
    [dataframe.columns.values.tolist()] + dataframe.values.tolist())

print("DONE!")
