with open("input.txt", "r") as input_file:
    input_data = [line.strip() for line in input_file.readlines()]

split_index = input_data.index("")
fresh_ranges = [(int(min_r), int(max_r)) for min_r, max_r in [line.split("-") for line in input_data[:split_index]]]
ingredients = [int(line) for line in input_data[split_index + 1:]]

fresh_count = 0

for ingredient in ingredients:
    for min_r, max_r in fresh_ranges:
        if min_r <= ingredient and max_r >= ingredient:
            fresh_count += 1
            break

print(fresh_count)
