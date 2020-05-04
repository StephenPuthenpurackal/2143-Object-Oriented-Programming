import json
import os

"""
Cool thing about json is that its syntax is identical to
pythons syntax for a dictionary.
"""


"""
Example 1: Read json as a string and then convert it from json to a dictionary.
"""
# Example 1: Read json from a string
data = '{"width" : 1024,"height" : 768,"sprite_images" : {"white" : "./images/person_white_64x64","yellow" : "./images/person_yellow_64x64","black" : "./images/person_black_64x64","red" : "./images/person_red_64x64","green" : "./images/person_green_64x64"},"social_distancing" : "False","infection_radius" : 10,"infection_rate" : 0.20}'

# convert json into a python dictionary
jdata = json.loads(data)

# print the data out to the screen
for key in jdata:
    print(jdata[key])

#________________________________________________________________________________


"""
Example 2: Read json as a file and then convert it from json file (aka string as well) to a dictionary.
"""
# Example 2: Read json in from a file
# check to see if "config.json" is a valid path
if os.path.isfile("config.json"):

    # open config for reading
    f = open("config.json","r")

    # read the file into a "data" variable
    data = f.read()

    # convert json into a python dictionary
    jdata = json.loads(data)

    # print the data out to the screen
    for key in jdata:
        print(jdata[key])

