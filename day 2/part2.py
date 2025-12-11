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

def isNumRepeating(int, mod):
    length = len(str(int))
    if length % mod == 0:
        if get_digits(int, 0, length//mod) == get_digits(int, length//mod, length//mod):
            return True
    return False

""" def isNumRepeating(int):
    length = len(str(int))
    if length % 2 == 0:
        if get_digits(int, 0, length//2) == get_digits(int, length//2, length//2):
            return True

    return False """

def check_ranges(file):
    ranges = getRanges(file)
    invalidIDs = 0
    for IDrange in ranges:
        for x in range(IDrange[0], IDrange[1]):
            if isNumRepeating(x, 2):
                invalidIDs += x

    return invalidIDs

#print(getRanges("example.txt"))
#print(isNumRepeating(2020))
print(check_ranges("input.txt"))