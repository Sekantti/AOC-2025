import math
import re

def get_data(file):
    input = open(file).read().split("\n")
    transposed = transpose(input)
    output = []

    for elem in transposed:
        output.append("".join(elem))

    return create_subarrays(to_int(remove_whitespace(output)))

def transpose(matrix):
    transposed = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            transposed[j][i] = matrix[i][j]

    return transposed

def contains_operator(string):
    return re.search('\*', string) != None or re.search('\+', string) != None

def extract_operator(string):
    operator = string[-1]
    output = string[:-1]

    return [operator, output]

def remove_whitespace(array):
    output = array[:]

    for elem in output:
        if elem.isspace():
            output.remove(elem)

    return output

def to_int(array):
    output = []

    for elem in array:
        if contains_operator(elem):
            operation = extract_operator(elem)
            output.append(operation[0])
            output.append(int(operation[1]))
        else:
            output.append(int(elem))

    return output

def create_subarrays(array):
    length = len(array)
    output = []

    for i in range(0, length):
        elem = array[i]
        if isinstance(elem, str):
            output.append([])
            output[-1].append(elem)
            for j in range(i+1, length):
                elem = array[j]
                if isinstance(elem, int):
                    output[-1].append(elem)
                if isinstance(elem, str):
                    break

    return output

def do_some_math(calc):
    if calc[0] == "*":
        calc[0] = 1
        result = math.prod(calc)

    if calc[0] == "+":
        calc[0] = 0
        result = sum(calc)
    
    return result

def total(calcs):
    result = 0

    for calc in calcs:
        result += do_some_math(calc)

    return result

def solve(data):
    return total(get_data(data))

print(solve("input.txt"))