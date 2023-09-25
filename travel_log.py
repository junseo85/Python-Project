travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, index, cities):
    travel_dic = {}
    travel_dic["country"] = country
    travel_dic["visits"] = index
    travel_dic["cities"] = cities
    travel_log.append(travel_dic)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
