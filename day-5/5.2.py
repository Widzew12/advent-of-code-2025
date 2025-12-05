with open("input.txt", "r") as input_file:
    input_data = [line.strip() for line in input_file.readlines()]

split_index = input_data.index("")
fresh_ranges = [(int(min_r), int(max_r)) for min_r, max_r in [line.split("-") for line in input_data[:split_index]]]

fresh_count = 0

new_fresh_ranges = []

while len(fresh_ranges) > 0:
    min_r, max_r = fresh_ranges[0]
    j = 0
    while j < len(fresh_ranges):
        check_min_r, check_max_r = fresh_ranges[j]
        if (check_min_r <= min_r and check_max_r >= min_r) or (check_min_r >= min_r and check_min_r <= max_r):
            min_r = min(min_r, check_min_r)
            max_r = max(max_r, check_max_r)
            del fresh_ranges[j]
            j = 0
        else:
            j += 1
    
    new_fresh_ranges.append((min_r, max_r))

for min_r, max_r in new_fresh_ranges:
    fresh = max_r - min_r + 1
    fresh_count += fresh

print(fresh_count)

