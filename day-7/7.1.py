with open("input.txt", "r") as input_file:
    manifold = [[c for c in line.strip()] for line in input_file.readlines()]

manifold[0][manifold[0].index("S")] = "|"

split_count = 0

for i in range(1, len(manifold)):
    prev_line = manifold[i - 1]
    curr_line = manifold[i]
    for j in range(len(curr_line)):
        if prev_line[j] == "|":
            if curr_line[j] == ".":
                curr_line[j] = "|"
            elif curr_line[j] == "^":
                if j > 0 and curr_line[j - 1] == ".":
                    curr_line[j - 1] = "|"
                if j < len(curr_line) - 1 and curr_line[j + 1] == ".":
                    curr_line[j + 1] = "|"
                
                split_count += 1

print(split_count)
