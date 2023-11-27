import json


def convert_numbers_to_strings(numbers):
    return [str(number) for number in numbers]


# Open the JSON file for reading
with open('product_test.json', 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Convert numbers to strings
lookup_numbers = convert_numbers_to_strings([9, 3, 8, 2])

# Convert the list of strings to a set for faster lookups
lookup_numbers_set = set(lookup_numbers)

# Iterate through the data and print 'productCode' for matching elements
for el in data:
    if any(number in str(el['productCode']) for number in lookup_numbers_set):
        print(el['productCode'])
