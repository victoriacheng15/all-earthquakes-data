import requests
from utils.time import utc_starttime, utc_today
from utils.time import get_utc_time
from utils.format_data import to_dict


def fetch_earthquakes_api():
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


def get_earthquakes_data():
    all_data = []
    data = fetch_earthquakes_api()

    for feature in data["features"]:
        id = feature["id"]
        properties = feature["properties"]
        place = properties["place"]
        mag = "{:.1f}".format(properties["mag"])
        latitude = feature["geometry"]["coordinates"][1]
        longitude = feature["geometry"]["coordinates"][0]
        time = properties["time"]
        utc_time = get_utc_time(time)

        event_data = to_dict(id, place, mag, latitude, longitude, utc_time)
        all_data.append(event_data)

    return all_data
