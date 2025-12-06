with open("input.txt", "r") as input_file:
    input_data = [line[:-1] for line in input_file.readlines()]

len_line = len(input_data[0])

div_locations = []
for i in range(len_line):
    is_div = True
    for line in input_data:
        if line[i] != " ":
            is_div = False
            break
    
    if is_div:
        div_locations.append(i)

len_loc = len(div_locations)
split_data = []

for i in range(len_loc + 1):
    start = 0 if i == 0 else div_locations[i - 1] + 1
    end = len_line if i == len_loc else div_locations[i]
    new_op = []
    for line in input_data:
        new_op.append(line[start:end])
    
    split_data.append(new_op)

grand_total = 0

for operation in split_data:
    nums, op = operation[:-1], operation[-1].strip()
    new_nums = []
    len_num = len(nums[0])
    for i in range(len_num):
        new_num_str = ""
        for line in nums:
            new_num_str += line[i] if line[i] != " " else ""
        if new_num_str != "":
            new_num = int(new_num_str)
            new_nums.append(new_num)
    
    if op == "+":
        res = 0
        for num in new_nums:
            res += num
    else:
        res = 1
        for num in new_nums:
            res *= num
    
    grand_total += res

print(grand_total)
