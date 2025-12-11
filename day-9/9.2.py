with open("/home/szymon/Drives/Files/Programowanie/Advent of code/advent-of-code-2025/day-9/input.txt", "r") as input_file:
    red_positions = [(int(x), int(y)) for x, y in [line.strip().split(",") for line in input_file.readlines()]]
# 0 - other, 1 - red, 2 - green
max_x = max(red_positions)[0]
max_y = max(red_positions, key=lambda e: e[1])[1]
print(max_x, max_y)

max_x = 20
max_y = 20


floor = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

# x - horizontal
# y - vertical

for i in range(len(red_positions)):
    cur_x, cur_y = red_positions[i]
    floor[cur_y][cur_x] = 1

    prev_x, prev_y = red_positions[i - 1]
    if prev_x == cur_x:
        for y in range(min(cur_y, prev_y) + 1, max(cur_y, prev_y)):
            floor[y][cur_x] = 1
    else:
        for x in range(min(cur_x, prev_x) + 1, max(cur_x, prev_x)):
            floor[cur_y][x] = 1

# for i in range(len(floor)):
#     line = floor[i]
#     is_filling = False
#     is_horizontal = False
#     was_filling = False
#     for j in range(len(line)):
#         if not is_filling and line[j] == 1:
#             is_filling = True
#         elif is_filling and line[j] == 1:
#             if j <= len(line) - 2 and line[j + 1] == 0:
#                 is_horizontal = True
#             if not is_horizontal:
#                 is_filling = False
#         elif is_filling:
#             line[j] = 1

# 0 - not checked
# 1 - can fill
# 2 - checking
# -2 - cannot fill

def try_fill(x, y):
    if x < 0 or x >= len(floor):
        return False
    if y < 0 or y >= len(floor[x]):
        return False
    if floor[y][x] == 1 or floor[y][x] == 2:
        return True
    if floor[y][x] == -2:
        return False
    floor[y][x] = 2
    if try_fill(x + 1, y) and try_fill(x - 1, y) and try_fill(x, y + 1) and try_fill(x, y - 1):
        floor[y][x] = 1
        return True
    else:
        floor[y][x] = -2
        return False

x, y = red_positions[0]
print(x, y)

if ((floor[y + 1][x] == 0 and try_fill(x, y + 1)) or (floor[y - 1][x] == 0 and try_fill(x, y - 1))
    or (floor[y][x + 1] == 0 and try_fill(x + 1, y)) or (floor[y + 1][x + 1] == 0 and try_fill(x + 1, y + 1)) or (floor[y - 1][x + 1] == 0 and try_fill(x + 1, y - 1))
    or (floor[y][x - 1] == 0 and try_fill(x - 1, y)) or (floor[y + 1][x - 1] == 0 and try_fill(x - 1, y + 1)) or (floor[y - 1][x - 1] == 0 and try_fill(x - 1, y - 1))):
    print("success!")

for line in floor:
    print(line)

# max_area = 0
# for i in range(len(red_positions)):
#     x1, y1 = red_positions[i]
#     for j in range(i + 1, len(red_positions)):
#         x2, y2 = red_positions[j]
#         area = abs((x1 - x2 + 1) * (y1 - y2 + 1))
#         max_area = max(area, max_area)

# print(max_area)
