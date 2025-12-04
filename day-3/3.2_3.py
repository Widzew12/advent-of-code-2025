import time

with open("input.txt", "r") as input_file:
    banks = [line.strip() for line in input_file.readlines()]

joltage_sum = 0

time_0 = time.time()

for bank in banks:
    max_joltage = 0
    
    curr_joltage = [0 for _ in range(len(bank))]
    dig_count = 0
    is_end = False

    for curr_dig in range(9, 0, -1):
        for i in range(len(bank) - 1, -1, -1):
            if int(bank[i]) == curr_dig:
                curr_joltage[i] = curr_dig
                dig_count += 1
                if dig_count == 12:
                    is_end = True
                    break
        if is_end:
            break
    
    new_joltage = [str(dig) for dig in curr_joltage if dig > 0]
    max_joltage = int("".join(new_joltage))

    print(max_joltage)
    joltage_sum += max_joltage

print(joltage_sum)
print(time.time() - time_0)
