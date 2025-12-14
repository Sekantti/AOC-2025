import re
import math


def get_banks(file):
    banks = open(file).read().split("\n")
    joltages = []
    for bank in banks:
        batteries = list(bank)
        joltages.append(batteries)

    return joltages

def get_highest_and_index(bank):
    max = [bank[0], 0]
    size = len(bank)
    for x in range(1, size):
        if bank[x] > max[0]:
            max = [bank[x], x]
    
    return max

def get_next_sig(bank, index):
    size = len(bank)
    bank_2 = bank[0:size-index+1]

    return get_highest_and_index(bank_2)

def get_next_bank(bank, index):
    return bank[index+1:len(bank)]

def get_max_joltage(bank):
    next_bank = bank
    max = ""
    for x in range(0, 12):
        next_sig = get_next_sig(next_bank, 12-x)
        max += next_sig[0]
        next_bank = get_next_bank(next_bank, next_sig[1])

    return int(max)

def solve(file):
    banks = get_banks(file)
    max = 0
    for bank in banks:
        max += get_max_joltage(bank)

    return max


print(solve("input.txt"))