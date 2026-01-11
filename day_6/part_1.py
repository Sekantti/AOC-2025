import math

def get_data(file):
    input = open(file).read().split("\n")
    output = []

    for line in input:
        output.append(line.split())

    return transpose(output)

def transpose(matrix):
    transposed = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            try:
                transposed[j][i] = int(matrix[i][j])
            except:
                transposed[j][i] = matrix[i][j]

    return transposed

def do_some_math(calc):
    if calc[-1] == "*":
        calc[-1] = 1
        result = math.prod(calc)

    if calc[-1] == "+":
        calc[-1] = 0
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