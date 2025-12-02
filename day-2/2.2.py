with open("input.txt", "r") as input_file:
    ranges = [(int(num1), int(num2)) for num1, num2 in [rang.split("-") for rang in input_file.read().strip().split(",")]]

s = 0

for min_r, max_r in ranges:
    for num in range(min_r, max_r + 1):
        num_str = str(num)
        for i in range(1, len(num_str)):
            num_split_check = [len(item) == 0 for item in num_str.split(num_str[:i])]
            if all(num_split_check):
                s += num
                break

print(s)
