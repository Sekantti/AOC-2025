from itertools import permutations
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

def overlaps(range_1, range_2):
    r1 = range(range_1[0], range_1[1]+1)
    r2 = range(range_2[0], range_2[1]+1)
    if range_1[0] in r2 or range_1[1] in r2 or range_2[0] in r1 or range_2[1] in r1:
        return True

    return False

def merge(range_0, range_1):
    return [min(range_0[0], range_1[0]), max(range_0[1], range_1[1])]

def combine_ranges(ranges):
    new_ranges = []

    for range_1 in ranges:
        temp_ranges = []
        merged = False
        for range_2 in new_ranges:
            if not merged and overlaps(range_1, range_2):
                temp_ranges.append(merge(range_1, range_2))
                merged = True
            else:
                temp_ranges.append(range_2)
        if not merged:
            temp_ranges.append(range_1)
        new_ranges = temp_ranges

    return new_ranges

def combine_all_ranges(ranges):
    new_ranges = ranges[:]
    length = len(new_ranges)

    while True:
        new_ranges = combine_ranges(new_ranges)
        new_length = len(new_ranges)

        if new_length < length:
            length = new_length
        else:
            break

    return new_ranges


def solve(file):
    freshness_ranges = combine_all_ranges(get_data(file))
    fresh_IDs = 0

    for freshness_range in freshness_ranges:
        fresh_IDs += freshness_range[1]+1 - freshness_range[0]

    return fresh_IDs


print(solve("input.txt"))