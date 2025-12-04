import time

with open("/home/szymon/Drives/Files/Programowanie/Advent of code/advent-of-code-2025/day-3/input.txt", "r") as input_file:
    banks = [[int(dig) for dig in line.strip()] for line in input_file.readlines()]

print(banks)

joltage_sum = 0

time_0 = time.time()

for bank in banks:
    max_joltage = 0
    
    # curr_joltage = [0 for _ in range(len(bank))]
    curr_joltage = []
    dig_count = 0
    is_end = False

    new_bank = bank

    while True:
        if len(new_bank) <= 12:
            break
        test_bank = new_bank[:-11]
        max_dig = max(test_bank)
        max_dig_index = new_bank.index(max_dig)
        curr_joltage.append(max_dig)
        new_bank = new_bank[max_dig_index + 1:]

    curr_joltage += new_bank[:12-len(curr_joltage)]
    print(curr_joltage)
    
    # new_joltage = [str(dig) for dig in curr_joltage if dig > 0]
    # max_joltage = int("".join(new_joltage))

    print(max_joltage)
    joltage_sum += max_joltage

print(joltage_sum)
print(time.time() - time_0)
