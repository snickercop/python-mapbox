# python-mapbox
A library for using the Mapbox API in Python

<h1>List of Functions</h1>

<b>geocode(place_name)</b>: returns the JSON result of a mapbox geocode call on the given string place_name.

<b>get_coords(place_name)</b>: returns the coordinates of the given place_name as a list of form [longitude, latitude]

<b>distance(start, finish)</b>: returns the distance between two points in the preset preferred units. Optional third parameter is a string that denotes a mode of transit besides driving ('walking' or 'cycling')
