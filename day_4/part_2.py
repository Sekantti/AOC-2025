import re
import math

def get_grid(file):
    grid = open(file).read().split("\n")
    size = len(grid)
    for x in range(0, size):
        grid[x] = list(grid[x])

    return grid

def get_directions():
    return [[0, 1],[0, -1], [1, 0], [-1, 0],[1, 1], [1, -1], [-1, 1], [-1, -1]]

def get_new_position(position, direction):
    return [position[0]+direction[0], position[1]+direction[1]]

def get_surrounding_rolls(grid, position):
    how_many = 0
    directions = get_directions()
    for direction in directions:
        new_position = get_new_position(position, direction)
        if new_position[0] < 0 or new_position[1] < 0:
            continue
        try:
            grid[new_position[0]][new_position[1]] == '@'
        except:
            continue
        else:
            if grid[new_position[0]][new_position[1]] == '@':
                how_many += 1

    return how_many

def get_movable(grid):
    size_x = len(grid)
    size_y = len(grid[0])
    movable = 0

    for x in range(0, size_x):
        for y in range(0, size_y):
            if grid[x][y] == '@' and get_surrounding_rolls(grid, [x, y]) < 4:
                movable += 1
                grid[x][y] = '.'

    return [grid, movable]

def solve(file):
    grid = get_grid(file)
    movable = get_movable(grid)
    solution = 0

    while movable[1] > 0:
        grid = movable[0]
        solution += movable[1]
        movable = get_movable(grid)

    return solution

print(solve("input.txt"))


"""
The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight a
djacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less 
time looking and more time breaking down the wall to the cafeteria.
"""