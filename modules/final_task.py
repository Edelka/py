# Create a tool which will calculate straight-line distance between different cities based on coordinates:
#  1. User will provide two city names by console interface
#  2. If tool do not know about city coordinates, it will ask user for input and store it in SQLite database for future use
#  3. Return distance between cities in kilometers

from math import radians, cos, sin, asin, sqrt
from DB_conn import DBConnection

# dbcon = DBConnection()
# # dbcon.create_table_cities()
# # print(DBConnection.select_city(DBConnection(), 'City'))
# input_type = input('Please type the city name: ')
# try:
#     if input_type != dbcon.select_city(dbcon):
#         input_lon = input('Please type lon: ')
#         input_lat = input('Please type lat: ')
#         dbcon.insert_city(input_type, input_lon, input_lat)
#     else:
#
#         print(input_type)
# except Exception as e:
#     print(e)
# print(DBConnection.select_city(DBConnection(), 'city'))

dbcon = DBConnection()
# dbcon.create_table_cities()
input_type = input('Please type the city name: ')
lon1 = float(input('Please type lon: '))
print(type(lon1))
lat1 = float(input('Please type lat: '))
dbcon.insert_city(input_type, lon1, lat1)

input_type2 = input('Please type the destination city name: ')
lon2 = float(input('Please type dest lon: '))
lat2 = float(input('Please type dest lat: '))
dbcon.insert_city(input_type2, lon2, lat2)


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


dist = distance(lat1, lat2, lon1, lon2)

print(f"Distance between {input_type} and {input_type2} is equal to: {dist}km")
print(DBConnection.select_city(DBConnection(), 'city'))
