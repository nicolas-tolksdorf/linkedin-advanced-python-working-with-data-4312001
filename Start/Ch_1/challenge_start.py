# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each


def summary():

    # open the data file and load the JSON
    with open("30DayQuakes.json", "r") as datafile:
        data = json.load(datafile)

    # Method 1.1:
    #print(f"TotalEvents: {len(data['features'])}") # 11745
    # Method 1.2:
    #print(f"TotalEvents: {data['features']['metadata']['count']}") # 11745
    # Method 1.3:
    TotalEvents = sum(bool(feature['properties'])
        for feature in data['features'])
    # print(f"TotalEvents: {TotalEvents}") # 11745

    # Method 1.1:
    # TotalFelt = list(filter(isFeltBy, data['features']))
    # print("TotalFelt", len(TotalFelt)) # 28
    # Method 1.2:
    TotalFelt = sum(feature['properties']['felt'] is not None and feature['properties']['felt'] >= 100 for feature in data['features'])
    print("TotalFelt", TotalFelt) # 28        


    most_felt = max(data['features'], key=get_felt)
    MostFeltEvent = most_felt['properties']['title']
    # print(f"MostFeltEvent: {MostFeltEvent}") # M 5.7 - 6km NNE of Magna, Utah
    MostFeltCount = most_felt['properties']['felt']
    # print(f"MostFeltCount: {MostFeltCount}") # 33091

    # Correct! Marvelous work.
    # Your code returned:
    # TotalEvents: 11745
    # TotalFelt: 28
    # MostFeltEvent: M 5.7 - 6km NNE of Magna, Utah
    # MostFeltCount: 33091
    # --- -- -- -- -- -- -- -- -- -- -- --

def get_felt(item):
    # return item['properties']['felt'] if item['properties']['felt'] == None else 0
    felt = item['properties']['felt']
    if felt == None:
        return 0
    return felt

def isFeltBy(item):
    # Method 1: more concise
    f = item['properties']['felt']
    return (f is not None and f >= 100)

    # Method 2: less concise
    # total = 100
    # if item['properties']['felt'] == None:
    #     return False
    # return True if total <= item['properties']['felt'] else False

summary()
