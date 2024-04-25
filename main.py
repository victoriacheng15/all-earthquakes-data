import requests, json, datetime
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

def get_day_time(time):
    timestamp_seconds = time / 1000
    utc_time = datetime.fromtimestamp(timestamp_seconds)
    return utc_time.strftime("%Y-%m-%d %H:%M:%S")


def to_dict(id, place, mag, latitude, longitude, utc_time):
    return {
        "id": id,
        "place": place,
        "magnitude": mag,
        "latitude": latitude,
        "longitude": longitude,
        "utc_time": utc_time,
    }


def get_earthquake_data():
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    utc_today = datetime.now(timezone.utc)
    utc_starttime = utc_today - relativedelta(days=5)

    params = {
        "format": "geojson",
        "starttime": utc_starttime,
        "endtime": utc_today,
        "minmagnitude": 1.0,
    }

    response = requests.get(url, params=params)
    # print(json.dumps(response.json()["features"][0], indent=2))
    all_data = []

    if response.status_code == 200:
        data = response.json()

        for feature in data["features"]:
            id = feature["id"]
            properties = feature["properties"]
            place = properties["place"]
            mag = "{:.1f}".format(properties["mag"])
            latitude = feature["geometry"]["coordinates"][1]
            longitude = feature["geometry"]["coordinates"][0]
            time = properties["time"]
            utc_time = get_day_time(time)

            event_data = to_dict(id, place, mag, latitude, longitude, utc_time)
            all_data.append(event_data)

        return all_data
    else:
        print("Error:", response.status_code, response.text)


get_earthquake_data()
