import requests
from utils.time import utc_starttime, utc_today


def fetch_earthquakes():
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

    params = {
        "format": "geojson",
        "starttime": utc_starttime,
        "endtime": utc_today,
        "minmagnitude": 1.0,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
