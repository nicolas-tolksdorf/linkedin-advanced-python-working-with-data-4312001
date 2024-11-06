# Example file for Advanced Python: Working With Data by Joe Marini
# using the map() function to transform data to another form

import json
import pprint
import datetime


def squareFunc(x):
    return x**2


def toGrade(x):
    if (x >= 90):
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"


# define some sample sequences to operate on
nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
grades = (81, 89, 94, 78, 61, 66, 99, 74)

# TODO: use map to create a new sequence of values
squares = list(map(squareFunc, nums))
print(squares)
# TODO: use sorted and map to change numbers to grades
letters = list(map(toGrade, sorted(grades)))
print(letters)

# Use the filter on our data - let's filter out all seismic events that were *not* quakes
# open the data file and load the JSON
# with open("../../30DayQuakes.json", "r") as datafile:
#     data = json.load(datafile)


# filter the data down to the largest events
# def bigmag(q):
#     return q['properties']['mag'] is not None and q['properties']['mag'] >= 6


# results = list(filter(bigmag, data['features']))

# TODO: transform the largest events into a simpler structure







# Filter the data down to the largest events where magnitude >= 6
# Return a json containing place, magnitude, date
# Import date and pprint modules to convert timestamp to date and print json output

# data
with open('30DayQuakes.json') as dataFile:
    data = json.load(dataFile)
# largest()
def largest(item):
    if (item['properties']['mag'] is not None 
        and item['properties']['mag'] >= 6):
        return True
    return False
# createJson()
def create_json(prop):
    ### print(type(prop).__name__) # dict
    return {
        'place': prop['properties']['place'],
        'magnitude': prop['properties']['mag'],
        'date': datetime.date.fromtimestamp(prop['properties']['time'] / 1000) # convert ms to seconds
    }
# filter & output
largest_events = list(filter(largest, data['features']))
### print(len(largest_events)) # 5
### print(type(data).__name__) # dict
### print(type(data['features']).__name__) # list
### print(largest_events['properties']) # TypeError: list indices must be integers or slices, not str
### print(type(largest_events).__name__) # list
output = list(map(create_json, largest_events))
pprint.pp(output)
### [{'place': '246km S of Kangin, Indonesia',
###   'magnitude': 6.2,
###   'date': datetime.date(2020, 3, 18)},
### ...
