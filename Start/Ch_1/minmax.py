# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# TODO: The min() function finds the minimum value
print(f"The minimum value is {min(values)}") # uses numeric order
print(f"The minimum string is {min(strings)}") # uses alphabetic order, starting with first letter of each word

# TODO: The max() function finds the maximum value
print(f"The maximum value is {max(values)}")
print(f"The maximum string is {max(strings)}") # uses alphabetic order


# TODO: define a custom "key" function to extract a data field
print(f"The minimum string is {min(strings, key=len)}") # ordered by character length
print(f"The maximum string is {max(strings, key=len)}") # order by character length


# TODO: open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
     data = json.load(datafile)

print(data["metadata"]["title"])
print(len(data["features"]))

def getMag(data_item) :
    magnitude = data_item['properties']['mag']
    if magnitude == None :
        magnitude = 0
    return magnitude

print(min(data["features"], key=getMag))
print(max(data["features"], key=getMag))
