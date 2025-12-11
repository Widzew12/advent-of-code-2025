with open("input.txt", "r") as input_file:
    red_positions = [(int(x), int(y)) for x, y in [line.strip().split(",") for line in input_file.readlines()]]

max_area = 0
for i in range(len(red_positions)):
    x1, y1 = red_positions[i]
    for j in range(i + 1, i + 3):
        if j >= len(red_positions):
            j -= len(red_positions)

        x2, y2 = red_positions[j]
        area = abs((x1 - x2 + 1) * (y1 - y2 + 1))
        max_area = max(area, max_area)

print(max_area)
