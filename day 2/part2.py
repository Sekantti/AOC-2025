import re
import math

def getProdId(file):
    return open(file).read().split(",")

def getRanges(file):
    ids = getProdId(file)
    rangeArray = []
    for range in ids:
        strings = range.split("-")
        ints = [int(strings[0]), int(strings[1])]
        rangeArray.append(ints)

    return rangeArray

def get_digits(number, n, pow):
    return number // 10**n % 10**pow

def isNumRepeating(int, repeats):
    length = len(str(int))
    if length % repeats == 0:
        repeated_length = length//repeats
        pattern = get_digits(int, 0, repeated_length)
        for x in range(1,repeats):
            new_pattern = get_digits(int, repeated_length*x, repeated_length)
            if pattern != new_pattern:
                return False
        return True
    return False

def check_ranges(file):
    ranges = getRanges(file)
    invalidIDs = 0
    for IDrange in ranges:
        for x in range(IDrange[0], IDrange[1]+1):
            length = len(str(x))
            seen = False
            for y in range(2, length+1):
                if seen == False:
                    if isNumRepeating(x, y):
                        invalidIDs+=x
                        seen = True

    return invalidIDs

print(check_ranges("input.txt"))