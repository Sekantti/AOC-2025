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

def get_digit(number, n):
    return number // 10**n % 10

def isNumRepeating(int):
    length = len(str(int))
    if length % 2 == 0:
        for x in range(length//2):
            if get_digit(int, x) != get_digit(int, x+length//2):
                return False
        return True

    return False


def check_ranges(file):
    ranges = getRanges(file)
    invalidIDs = 0
    for IDrange in ranges:
        for x in range(IDrange[0], IDrange[1]):
            if isNumRepeating(x):
                invalidIDs += x

    return invalidIDs

#print(getRanges("example.txt"))
#print(isNumRepeating(2020))
print(check_ranges("input.txt"))