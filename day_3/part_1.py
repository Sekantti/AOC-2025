import re
import math

def get_banks(file):
    banks = open(file).read().split("\n")
    joltages = []
    for bank in banks:
        batteries = list(bank)
        joltages.append(batteries)

    return joltages

def get_largest_joltage(bank):
    bank_size = len(bank)
    largest_joltage = int(bank[0])
    for x in range(0, bank_size):
        for y in range(x+1, bank_size):
            new_joltage = int(bank[x]+bank[y])
            if new_joltage > largest_joltage:
                largest_joltage = new_joltage

    return largest_joltage

def solve(file):
    banks = get_banks(file)
    max = 0
    for bank in banks:
        max += get_largest_joltage(bank)

    return max


print(solve("input.txt"))