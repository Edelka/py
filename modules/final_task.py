# Create a tool which will calculate straight-line distance between different cities based on coordinates:
#  1. User will provide two city names by console interface
#  2. If tool do not know about city coordinates, it will ask user for input and store it in SQLite database for future use
#  3. Return distance between cities in kilometers

from math import radians, cos, sin, asin, sqrt
from DB_conn import DBConnection

dbcon = DBConnection()

# dbcon.create_table_cities()
# print(DBConnection.select_city(DBConnection(), 'City'))
lon = 0
lat = 0


def get_city_data(dest):
    input_city = input(f'Please type the{dest} city name: ')
    try:
        city_tuple = dbcon.select_city(input_city)
        if len(city_tuple) == 0:
            # (input_type)
            lon = float(input('Please type lon: '))
            lat = float(input('Please type lat: '))
            dbcon.insert_city(input_city, lon, lat)
            return lon, lat, input_city
        elif len(city_tuple) > 0:
            lon = city_tuple[0][1]
            lat = city_tuple[0][2]
            # print(lon, lat)
            return lon, lat, input_city
    except Exception as e:
        print(e)
    dbcon.close_cursor()


a = get_city_data('')
b = get_city_data(' destination')
# print(a)
# print(b)

def distance(lat1, lat2, lon1, lon2):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers.
    r = 6371

    # calculate the result
    return c * r


dist = distance(a[0], b[0], a[1], b[1])

# %.3f trim for 3 signs after comma
print(f"Distance between {a[2]} and {b[2]} is equal to: %.3fkm" % dist)

