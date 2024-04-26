def to_dict(id, place, mag, latitude, longitude, utc_time):
    return {
        "id": id,
        "place": place,
        "magnitude": mag,
        "latitude": latitude,
        "longitude": longitude,
        "utc_time": utc_time,
    }
