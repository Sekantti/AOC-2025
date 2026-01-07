import re
import math

def get_data(file):
    input = open(file).read().split("\n\n")
    output = input[0].split("\n")

    for x in range(0, len(output)):
        output[x] = output[x].split("-")

    for x in range(0, len(output)):
        for y in range(0, 2):
            output[x][y] = int(output[x][y])

    return output

def order_range(range):
    if range[0] > range[1]:
        return [range[1], range[0]]
    
    return range

def order_ranges(ranges):
    output_ranges = []
    for range in ranges:
        output_ranges.append(order_range(range))

    return output_ranges

def is_value_in_range(range, value):
    if value >= range[0] and value <= range[1]:
        return True
    
    return False

def combine_range(range_1, range_2):
    new_range = [range_1[0], range_1[1]]
    if is_value_in_range(range_1, range_2[0]) and range_2[1] > range_1[1]:
        new_range = [new_range[0], range_2[1]]
    if is_value_in_range(range_1, range_2[1]) and range_2[0] < range_1[0]:
        new_range = [range_2[0], new_range[1]]
    
    return new_range

def combine_ranges(ranges, range_1):
    new_ranges = ranges
    for range in ranges:
        new_range = combine_range(range, range_1)
        if new_range[0] != range[0] or new_range[1] != range[1]:
            new_ranges.remove(range)
            new_ranges.remove(range_1)
            new_ranges.append(new_range)
        
    return new_ranges

def combine_all_ranges(ranges):
    new_ranges = []
    for range in ranges:
        new_ranges = combine_ranges(ranges, range)

    return new_ranges

def solve(file):
    freshness_ranges = combine_all_ranges(order_ranges(get_data(file)))

    fresh_IDs = []

    for freshness_range in freshness_ranges:
        freshness_range = order_range(freshness_range)
        for x in range(freshness_range[0], freshness_range[1]+1):
            if x not in fresh_IDs:
                fresh_IDs.append(x)

    return len(fresh_IDs)

print(solve("input.txt"))