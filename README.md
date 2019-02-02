# python-mapbox
A library for using the Mapbox API in Python

<h1>List of Functions</h1>

<h2>points</h2>
<b>geocode(place_name)</b>: returns the JSON result of a mapbox geocode call on the given string place_name.

<b>get_coords(place_name)</b>: returns the coordinates of the given place_name as a list of form [longitude, latitude]

<h2>routing</h2>
All routing functions will take either list coordinate pairs (e.g. from distance.get_coords) or string place names.


<b>distance(start, finish)</b>: returns the distance between two points in the preset preferred units. Optional third parameter is a string that denotes a mode of transit besides driving ('walking' or 'cycling')

<b>multiDistance(pointA, pointC, pointD, pointB, profile='driving')</b>: similar to distance. returns a list containing 0: the distance added to the A->B trip by adding the C->D trip and 1: the total distance of the multi-leg trip.
