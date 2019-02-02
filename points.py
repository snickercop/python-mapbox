import requests
import re
import ast

# all coordinates in this package are in the form of LONGITUDE FIRST lists
# the API gives distances in meters
API_KEY = ''
PREFFERED_UNITS_D = 'miles'

distanceCFactor = {'miles':1/1609.344}

def geocode(place_name):
    place_name = place_name.replace(" ", "%20")
    return requests.get(f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json?access_token=" + API_KEY).content

def get_coords(place_name): # returns a list [<longitude>, <latitude>]
    json = geocode(place_name).decode("utf-8")
    coord_index = json.find('"coordinates"') + 14
    # use regex to retrieve coordinates as list
    p = re.compile(r'\[.*\]')
    coordMatch = p.match(json[coord_index:coord_index+50])
    coordList = ast.literal_eval(coordMatch.group())
    return coordList
