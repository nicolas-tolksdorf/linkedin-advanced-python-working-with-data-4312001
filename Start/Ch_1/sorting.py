# Example file for Advanced Python: Working With Data by Joe Marini
# sorting data with the sorted() and sort() functions

import json


numbers = [42, 54, 19, 17, 23, 31, 16, 4]
names = ["Jeff", "Bill", "Addie", "Stephanie", "Zach", "Lukas", "Joe", "Stacy"]

# TODO: the sorted() function can be used to return a new list with sorted data
result1 = sorted(numbers)
print(result1) # [4, 16, 17, 19, 23, 31, 42, 54]
print(id(numbers), id(result1)) # 124335993751168 124335993633792

# TODO: alternately, you can use the list object's sort() method, which sorts the list in-place
names.sort(reverse=True)
print(names) # ['Zach', 'Stephanie', 'Stacy', 'Lukas', 'Joe', 'Jeff', 'Bill', 'Addie']

# TODO: To sort custom objects, we can tell the sort function which property to use
# by specifying a key function

# fetch json from file
# create getMag() function to get magnitude from each earthquake
# sort data by "mag" key using the getMag() function and order in reverse
# print the place of the first 10 entries

# My answer:
# fetch json from file
with open('30DayQuakes.json', 'r') as dataFile :
    data = json.load(dataFile)
# create getMag() function to get magnitude from each earthquake
def getMag(dataItem) :
    magnitude = dataItem['properties']['mag']
    if (magnitude is None):
        magnitude = 0
    return float(magnitude)
# sort data by "mag" key using the getMag() function and order in reverse
# data.sort(key=getMag, reverse=True) # Error: no sort function for dict Objects
data['features'].sort(key=getMag, reverse=True) # 
# print the place of the first 10 entries
for i in range(0, 10) :
    print(data['features'][i]['properties']['place'])













# open the data file and load the JSON
# with open("../../30DayQuakes.json", "r") as datafile:
#     data = json.load(datafile)


# def getmag(dataitem):
#     magnitude = dataitem["properties"]["mag"]
#     if (magnitude is None):
#         magnitude = 0
#     return float(magnitude)
