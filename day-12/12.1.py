with open("input.txt", "r") as input_file:
    input_data = [line.strip() for line in input_file.readlines()]

shapes = []
i = 1
while i < 29:
    shape = []
    for line in input_data[i:i + 3]:
        shape.append([c == "#" for c in line])
    
    shapes.append(shape)
    i += 5

regions = []
for line in input_data[30:]:
    reg, pres = line.split(": ")
    reg = [int(num) for num in reg.split("x")]
    reg_map = [[0 for _ in range(reg[0])] for _ in range(reg[1])]
    presents = [int(num) for num in pres.split(" ")]
    regions.append((reg_map, presents))
    
for region, presents in regions:
    ...
