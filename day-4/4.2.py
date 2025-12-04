with open("input.txt", "r") as input_file:
    grid = [[1 if c == "@" else 0 for c in line.strip()] for line in input_file.readlines()]

# i - vertical
# j - horizontal

final_count = 0
mv = len(grid) - 1

while True:
    can_remove = []

    for i in range(len(grid)):
        mh = len(grid[i]) - 1
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                c = 0
                c += grid[i-1][j-1] if i > 0 and j > 0 else 0
                c += grid[i-1][j] if i > 0 else 0
                c += grid[i-1][j+1] if i > 0 and j < mh else 0
                c += grid[i][j-1] if j > 0 else 0
                c += grid[i][j+1] if j < mh else 0
                c += grid[i+1][j-1] if i < mv and j > 0 else 0
                c += grid[i+1][j] if i < mv else 0
                c += grid[i+1][j+1] if i < mv and j < mh else 0

                if c < 4:
                    can_remove.append((i, j))
                    final_count += 1
    
    if len(can_remove) == 0:
        break
    
    for i, j in can_remove:
        grid[i][j] = 0

print(final_count)
