from points import *

# implement multiDistance function that returns 1. the total distance for trip ACDB and 2. the additional distance added by routing through CD
def distance(start, finish, profile="driving"): # set to driving by default; start and finish are coordinate lists
    if(isinstance(start, str)):
        start = get_coords(start)
    if(isinstance(finish, str)):
        finish = get_coords(start)
    url = f"https://api.mapbox.com/directions/v5/mapbox/{profile}/{start[0]},{start[1]};{finish[0]},{finish[1]}?geometries=geojson&access_token={API_KEY}"
    json = requests.get(url).content.decode("utf-8")
    distanceInMeters = ast.literal_eval(re.compile(r'\"(?:distance)\"\:(\d+\.\d*)').search(json).group(1)) # regex to find first "distance" in meters
    distanceC = distanceInMeters * distanceCFactor[PREFFERED_UNITS_D]
    return distanceC

def multiDistance(pointA, pointC, pointD, pointB, profile='driving'): #A, C, D, B are coordinate lists
    AC = distance(pointA, pointC, 'driving')
    CD = distance(pointC, pointD, 'driving')
    DB = distance(pointD, pointB, 'driving')
    totalDistance = AC + CD + DB
    additionalDistance = totalDistance-CD
    return [additionalDistance, totalDistance]
