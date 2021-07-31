import datetime
import pytz

def get_status_contest(time_start, time_end):
    now = datetime.datetime.now(pytz.utc)
    if time_start > now:
        return 'upcoming'
    elif time_start < now < time_end:
        return "ongoing"
    else:
        return "expired"