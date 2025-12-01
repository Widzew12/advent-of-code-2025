with open("input.txt", "r") as input_file:
    sequences = [(line[0], int(line[1:])) for line in input_file.readlines()]

curr_num = 50
count = 0

for dir, val in sequences:
    while val > 0:
        curr_num += 1 if dir == "R" else -1
        val -= 1
        if curr_num < 0:
            curr_num += 100
        elif curr_num >= 100:
            curr_num -= 100
        
        if curr_num == 0:
            count += 1

print(count)
