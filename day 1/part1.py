import re

def turnDial(position, turn):
    if abs(turn) > 100:
        turn = turn % 100
        #print(turn)

    newPosition = position + turn

    if newPosition <0:
        return 100 + newPosition
    if newPosition > 100:
        return newPosition - 100
    if newPosition == 100:
        newPosition = 0
    
    return newPosition

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
    newPosition = position
    zeroes = 0
    print(newPosition)
    for x in turns:
        newPosition = turnDial(newPosition, x)
        if newPosition == 0 or newPosition == 100:
            zeroes += 1
        print(newPosition)

    return zeroes


print(getZeroes("input.txt", 50))
#print(turnDial(50, -68))

"""
I want a function that takes in a number and add l or r whatever to the number

then I want a function that checks

I need a function that takes each line of the txt file


"""
