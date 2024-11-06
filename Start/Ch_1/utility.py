# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates the use of the any, all, and sum functions
import json

values = [0, 1, 2, 3, 4, 5]

# TODO: any() can be used to see if any value in a sequence is True
print(f"Any True values: {any(values)}")

# TODO: all() will detect if all of the values in a sequence are True
print(f"All True values: {all(values)}")

# TODO: sum() can be use to add all of the values in a sequence
print(f"Sum values: {sum(values)}")

# these utility functions don't have callbacks like min or max,
# but we can use a generator for more fine control


# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# TODO: are there any quake reports that were felt by more than 25,000 people?
# print(type(data).__name__) # dict
# print(type(data['features']).__name__) # list
print(any(feature['properties']['felt'] is not None 
          and feature['properties']['felt'] > 25000
          for feature in data['features']
))

# TODO: how many quakes were felt by more than 500 people?
print("Felt by >500 people:", sum(feature['properties']['felt'] is not None
          and feature['properties']['felt'] > 500
          for feature in data['features']
))

# TODO: how many quakes had a magnitude of 6 or larger?
print("Magnitude >6:", sum(feature['properties']['mag'] is not None
          and feature['properties']['mag'] >= 6.0
          for feature in data['features']
))