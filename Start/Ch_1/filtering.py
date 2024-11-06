# Example file for Advanced Python: Working With Data by Joe Marini
# using the filter() function to filter a data set

import json

# Task:
# create filterEvens(x) function that filters out even numbers and keeps odd numbers
# create filterUppers(x) function that filters out upper-case letters and keeps lower case letters
# print result that uses filter to remove items from nums
# print result that uses filter to remove items from chars 
# 
# Filter out all seismic events that were *not* quakes from 30DayQuakes.json







# file
with open('30DayQuakes.json') as dataFile:
    data = json.load(dataFile)
# function
def notAQuake(item):
    if "earthquake" == item['properties']['type']:
        return False
    elif item['properties']['type'] is None:
        return False
    return True
# filter
notQuakes = list(filter(notAQuake, data['features']))
# a = filter(notAQuake, data['features'])
# print(type(a).__name__) # filter

for i in range(0, 10):
    print(notQuakes[i]['properties']['type'])



def filterEvens(x):
    # filters out even numbers and keeps odd numbers
    if x % 2 == 0:
        return False
    return True


def filterUppers(x):
    # filters out upper-case letters and keeps lower case letters
    if x.isupper():
        return False
    return True


# define some sample sequences to operate on
nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
chars = "abcDeFGHiJklmnoP"

# TODO: use filter to remove items from a list
print(list(filter(filterEvens, nums)))

# TODO: use filter on non-numeric sequence
print(list(filter(filterUppers, chars)))

# Use the filter on our data - let's filter out all seismic events that were *not* quakes
# open the data file and load the JSON
# with open("../../30DayQuakes.json", "r") as datafile:
#     data = json.load(datafile)
