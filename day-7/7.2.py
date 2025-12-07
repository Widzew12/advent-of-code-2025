mani_dict = {"S": 1, "^": -1, ".": 0}

with open("input.txt", "r") as input_file:
    manifold = [[mani_dict[c] for c in line.strip()] for line in input_file.readlines()]

for i in range(1, len(manifold)):
    prev_line = manifold[i - 1]
    curr_line = manifold[i]
    for j in range(len(curr_line)):
        if prev_line[j] > 0:
            if curr_line[j] >= 0:
                curr_line[j] += prev_line[j]
            elif curr_line[j] == -1:
                if j > 0 and curr_line[j - 1] >= 0:
                    curr_line[j - 1] += prev_line[j]
                if j < (len(curr_line) - 1) and curr_line[j + 1] >= 0:
                    curr_line[j + 1] += prev_line[j]

print(sum(manifold[-1]))
