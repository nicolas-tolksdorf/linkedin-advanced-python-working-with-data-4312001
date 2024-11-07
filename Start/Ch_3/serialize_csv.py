# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a CSV file

import csv
import json
import datetime

# Instructions: write events with a magnitude of at least 5 to a csv file named largequakes.cvs.
#               The csv rows must have four columns: Place, Magnitude, Link, Date









# read file
with open('30DayQuakes.json') as dataFile:
    data = json.load(dataFile)
# fetch events with magnitude larger than 5
def largerThanMag5(item):
    magnitude = item['properties']['mag']
    # if magnitude == None:
    #     return False
    # if magnitude > 5:
    #     return True
    # return False
    return magnitude is not None and magnitude > 5

large_events = list(filter(largerThanMag5, data['features'])) # converting to list is not required


# def isbig(x):
#     mag = x["properties"]["mag"]
#     return mag is not None and mag > 5


# Filter the data by quakes that are larger than 5 magnitude
# largequakes = list(filter(isbig, data["features"]))

# Create the header and row structures for the data
header = ['Place', 'Magnitude', 'Link', 'Date']
rows = []
# Fill row by iterating over big events
for event in large_events:
    # event_date = datetime.date.fromtimestamp(event['properties']['time']) # ValueError: year 52183 is out of range
    event_date = datetime.date.fromtimestamp(
        int(event['properties']['time'])/1000)
    rows.append([event['properties']['place'],
        event['properties']['mag'],
        event['properties']['url'],
        event_date])

# Write to largequakes.csv file 
with open('Start/Ch_3/largequakes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    ### writer.writerow(csvfile) # io.UnsupportedOperation: not readable
    writer.writerow(header)
    writer.writerows(rows)
    ### writer.writerows means no need to iterate over rows:
    # for row in rows:
    #     writer.writerow(row)










# TODO: Create the header and row structures for the data

# TODO: populate the rows with the resulting quake data

# TODO: write the results to the CSV file







# read in the contents of the JSON file
# with open("../../30DayQuakes.json", "r") as datafile:
#     data = json.load(datafile)


# def isbig(x):
#     mag = x["properties"]["mag"]
#     return mag is not None and mag > 5


# # Filter the data by quakes that are larger than 5 magnitude
# largequakes = list(filter(isbig, data["features"]))

# TODO: Create the header and row structures for the data

# TODO: populate the rows with the resulting quake data

# TODO: write the results to the CSV file
