# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import Counter, defaultdict


# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# def get_type(features):
#     types = []
#     for feature in features:
#         # return feature['properties']['type']
#         t = Counter(feature['properties']['type'])
#         t.update

# print(get_type(data['features']))

# event_type = Counter(get_type(data['features']))
event_types = defaultdict(int)
for feature in data['features']:
    # type = str(feature['properties']['type'])
    event_types[feature['properties']['type']] += 1

print(event_types)
