import math

def get_data(file):
    input = open(file).read().split("\n")
    transposed = transpose(input[:-1])
    operations = remove_whitespace(transpose(input[-1])[0])
    output = [" "]

    for elem in transposed:
        output.append("".join(elem))
    
    return [create_subarrays(output), operations]

def transpose(matrix):
    transposed = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            transposed[j][i] = matrix[i][j]

    return transposed

def remove_whitespace(array):
    output = []

    for elem in array:
        if not elem.isspace():
            output.append(elem)

    return output

def create_subarrays(array):
    length = len(array)
    output = []

    for i in range(0, length):
        if array[i].isspace():
            output.append([])
            for j in range(i+1, length):
                try:
                    output[-1].append(int(array[j]))
                except:
                    break

    return output

def solve(file):
    numbers, operators = get_data(file)
    result = 0

    for i in range(0, len(numbers)):
        if operators[i] == "*":
            result += math.prod(numbers[i])
        if operators[i] == "+":
            result += sum(numbers[i])

    return result

print(solve("input.txt"))