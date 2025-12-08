import re
import math

def turnDial(position, turn):
    click = 0
    if abs(turn) > 100:
        click = abs(turn) // 100
        if turn < 0:
            turn = turn % 100 - 100
        else:
            turn = turn % 100
        if turn == 0:
            return [0, click]
    
    newPosition = position + turn

    if newPosition <0:
        if position > 0:
            click += 1
        return [100 + newPosition, click]
    if newPosition > 100:
        if position < 100:
            click += 1
        return [newPosition - 100, click]
    if newPosition == 100 or newPosition == 0:
        return [newPosition, 1+click]
    
    return [newPosition, click]

def getTurns(file):
    turnsArray = []
    with open(file) as turns:
        for x in turns:
            if x[0] == "L":
                turnsArray.append(-int(re.findall(r'\d+', x)[0]))
            if x[0] == "R":
                turnsArray.append(int(re.findall(r'\d+', x)[0]))
    
    return turnsArray

def getZeroes(file, position):
    turns = getTurns(file)
    newPosition = [position, 0]
    zeroes = 0
    print(newPosition)
    for x in turns:
        newPosition = turnDial(newPosition[0], x)
        if newPosition[1] > 0:
            zeroes += newPosition[1]
        print(newPosition)

    return zeroes


print(getZeroes("input.txt", 50))
#print(turnDial(50, -68))

"""
I want a function that takes in a number and add l or r whatever to the number

then I want a function that checks

I need a function that takes each line of the txt file


"""
"""
[50, 0]
[82, 1]
[52, 0]
[0, 1]
[95, 0]
[55, 1]
[0, 1]
[99, 0]
[0, 1]
[14, 0]
[32, 1]
"""