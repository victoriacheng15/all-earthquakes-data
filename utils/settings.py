filename = "earthquakes_data.csv"
header = [
    "code",
    "event_id",
    "place",
    "city",
    "country",
    "magnitude",
    "latitude",
    "longitude",
    "depth",
    "utc_time",
    "url",
    "details",
]


us_states = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming",
}


def set_city_country(place):
    split_place = place.split("of ")

    for abbr, state in us_states.items():
        if abbr in place or state in place:
            split_place[-1] = split_place[-1].replace(abbr, state).strip()

    cleaned_place = "of ".join(split_place)
    location = cleaned_place.split("of ")[-1]

    city = location.split(", ")[0]
    country = location.split(", ")[-1]

    city = f"{city}, {country}" if country in us_states.values() else city
    country = "USA" if country in us_states.values() else country

    return cleaned_place, city, country
