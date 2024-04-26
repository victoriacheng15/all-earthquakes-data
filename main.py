import json
from utils.get_api_data import fetch_earthquakes
from utils.time import get_utc_time
from utils.format_data import to_dict


def get_earthquake_data():
    all_data = []
    data = fetch_earthquakes()
    # print(json.dumps(data["features"][0], indent=2))

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

    print(all_data[0])
    return all_data


get_earthquake_data()
