import re
import math

def get_data(file):
    input = open(file).read().split("\n\n")
    output = [input[0].split("\n"), input[1].split("\n")]

    for x in range(0, len(output[0])):
        output[0][x] = output[0][x].split("-")

    for x in range(0, len(output[0])):
        for y in range(0, 2):
            output[0][x][y] = int(output[0][x][y])

    for x in range(0, len(output[1])):
        output[1][x] = int(output[1][x])

    return output


def is_ingredient_fresh(fresh, ingredient):
    largest = max(fresh[0], fresh[1])
    smallest = min(fresh[0], fresh[1])
    if ingredient >= smallest and ingredient <= largest:
        return True
    
    return False

def check_all_ranges(freshness_ranges, ingredient):
    for fresh in freshness_ranges:
        if is_ingredient_fresh(fresh, ingredient) == True:
            return True
    
    return False

def solve(file):
    data = get_data(file)
    fresh = data[0]
    ingredients = data[1]
    fresh_ingredients = 0

    for ingredient in ingredients:
        if check_all_ranges(fresh, ingredient) == True:
            fresh_ingredients += 1

    return fresh_ingredients

print(solve("input.txt"))