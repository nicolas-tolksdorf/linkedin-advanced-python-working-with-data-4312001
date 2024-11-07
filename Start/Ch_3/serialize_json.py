# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a JSON file

import json
import datetime


# read in the contents of the JSON file
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# print('data type:', type(data).__name__) # dict

def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 6


# TODO: define a function to transform complex JSON to simpler JSON
def simplequakes(item):
    return {
        'place': item['properties']['place'],
        'mag': item['properties']['mag'],
        'link': item['properties']['url'],
        'date': str(datetime.date.fromtimestamp(
            int(item['properties']['time'])/1000))
    }

# filter the data to only include large quakes
largequakes = list(filter(isbig, data["features"]))
# TODO: transform the data to a JSON format we want to save
largequakes = list(map(simplequakes, largequakes))
# TODO: use the dumps() function to write json to a string
json_str = json.dumps(largequakes, indent=4, sort_keys=True)
# print(json_str)
# TODO: use the dump() function to write json to a file
with open('Start/Ch_3/largequakes.json', 'w', encoding="utf-8") as jsonFile:
    json.dump(largequakes, jsonFile, indent=4, sort_keys=True)
