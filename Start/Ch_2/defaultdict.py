# Demonstrate the usage of defaultdict objects

from collections import defaultdict


# define a list of items that we want to count
fruits = ['apple', 'pear', 'orange', 'banana',
          'apple', 'grape', 'banana', 'banana']

# TODO: use a dictionary to count each element
fruitCounter = dict()

# TODO: Count the elements in the list
for fruit in fruits:
    # fruitCounter[fruit] += 1 # KeyError: 'apple' because dict doesn't define default key
    if fruit not in fruitCounter.keys():
        fruitCounter[fruit] = 0
    fruitCounter[fruit] += 1

# TODO: print the result
print(fruitCounter)


###############################################
# Use defaultdict to reduce required code

# fruitCounter = defaultdict(int) # assign a default key as an integer
fruitCounter = defaultdict(lambda: 100) # start counter from 100
for fruit in fruits:
    fruitCounter[fruit] += 1

print(fruitCounter)

