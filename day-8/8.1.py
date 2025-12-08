with open("input.txt", "r") as input_file:
    boxes = [[int(coord) for coord in line.strip().split(",")] for line in input_file.readlines()]

for i in range(len(boxes)):
    boxes[i].append(i)

distances = []

for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        dist_sqr = (boxes[i][0] - boxes[j][0]) ** 2 + (boxes[i][1] - boxes[j][1]) ** 2 + (boxes[i][2] - boxes[j][2]) ** 2
        distances.append((dist_sqr, i, j))

i = 0
while i < 1000:
    min_distance = min(distances)
    dist, box_1, box_2 = min_distance
    box_1_circuit = boxes[box_1][3]
    box_2_circuit = boxes[box_2][3]
    print(min_distance)
    if box_1_circuit != box_2_circuit:
        for box in boxes:
            if box[3] == box_2_circuit:
                box[3] = box_1_circuit
        
    i += 1
    
    distances.remove(min_distance)

circuit_sizes = [0 for _ in range(len(boxes))]

for i in range(len(boxes)):
    circuit = boxes[i][3]
    circuit_sizes[circuit] += 1

circuit_sizes.sort(reverse=True)

circuit_mult = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]

print(circuit_mult)
