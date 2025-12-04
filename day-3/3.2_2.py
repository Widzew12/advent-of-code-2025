import itertools
import time

with open("input.txt", "r") as input_file:
    banks = [line.strip() for line in input_file.readlines()]

joltage_sum = 0

time_0 = time.time()

for bank in banks:
    max_joltage = 0
    
    index_combinations = itertools.combinations(range(len(bank)), 12)

    u = 0

    for comb in index_combinations:
        joltage = 0
        mult = 10**12
        for i in comb:
            joltage += int(bank[i]) * mult
            mult //= 10
        max_joltage = max(max_joltage, joltage)

        u += 1
        if u % 1000000 == 0:
            print(u)

    print(max_joltage)
    joltage_sum += max_joltage

print(joltage_sum)
print(time.time() - time_0)
