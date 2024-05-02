import requests
from utils.time import get_utc_time, utc_starttime, utc_today
from utils.settings import set_city_country


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
        properties = feature["properties"]
        place = properties["place"]
        cleaned_place, city, country = set_city_country(place)
        time = properties["time"]

        event_data = {
            "code": properties["code"],
            "event_id": feature["id"],
            "place": cleaned_place,
            "city": city,
            "country": country,
            "magnitude": "{:.1f}".format(properties["mag"]),
            "latitude": feature["geometry"]["coordinates"][1],
            "longitude": feature["geometry"]["coordinates"][0],
            "depth": feature["geometry"]["coordinates"][2],
            "utc_time": get_utc_time(time),
            "url": properties["url"],
            "details": properties["detail"],
        }
        all_data.append(event_data)

    return all_data
