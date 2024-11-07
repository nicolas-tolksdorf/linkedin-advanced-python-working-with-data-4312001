# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime


# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

# 40 most significant events, ordered by most recent
def getSig(item):
    sig = item['properties']['sig']
    return sig if sig is not None else 0
# most_significant_events = sorted(data['features'], key=getSig, reverse=True)
data['features'].sort(key=getSig, reverse=True)
# print(len(most_significant_events[0:40]))
def getTime(item):
    time = item['properties']['time']
    return time if time is not None else 0
### Method 1: using getTime()
# most_significant_events = sorted(data['features'][:40], key=getTime, reverse=True)
### Method 2: using inline Lambda
most_significant_events = data['features'][:40]
most_significant_events.sort(
    key=lambda e: e['properties']['time'] if e['properties']['time'] is not None else 0, 
    reverse=True)

# print(len(most_significant_events))

header = ['Magnitude', 'Place', 'Felt Reports', 'Date', 'Google Map link']
rows = []

for event in most_significant_events:
    long = event['geometry']['coordinates'][0]
    lat = event['geometry']['coordinates'][1]
    map_link = f"https://www.google.com/maps/search/?api=1&query={lat}%2C{long}"
    rows.append([
        event['properties']['mag'],
        event['properties']['place'],
        event['properties']['felt'] if event['properties']['felt'] != None else 0,
        datetime.date.fromtimestamp(event['properties']['time']/1000),
        map_link,
    ])
with open('Start/Ch_3/significant_events.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)
