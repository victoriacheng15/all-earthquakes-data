from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

utc_today = datetime.now(timezone.utc)
utc_starttime = utc_today - relativedelta(days=5)

def get_utc_time(time):
    timestamp_seconds = time / 1000
    utc_time = datetime.fromtimestamp(timestamp_seconds, tz=timezone.utc)
    return utc_time.strftime("%Y-%m-%d %H:%M:%S")
