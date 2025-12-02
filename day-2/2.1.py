with open("input.txt", "r") as input_file:
    ranges = [(int(num1), int(num2)) for num1, num2 in [rang.split("-") for rang in input_file.read().strip().split(",")]]

s = 0

for min_r, max_r in ranges:
    for num in range(min_r, max_r + 1):
        num_str = str(num)
        l2 = len(num_str) // 2 if len(num_str) % 2 == 0 else 0
        if l2 and num_str[:l2] == num_str[l2:]:
            s += num

print(s)
