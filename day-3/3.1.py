with open("input.txt", "r") as input_file:
    banks = [line.strip() for line in input_file.readlines()]

joltage_sum = 0

for bank in banks:
    max_joltage = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            max_joltage = max(joltage, max_joltage)

    joltage_sum += max_joltage

print(joltage_sum)
