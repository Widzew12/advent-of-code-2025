with open("input.txt", "r") as input_file:
    boxes = [[int(coord) for coord in line.strip().split(",")] for line in input_file.readlines()]

for i in range(len(boxes)):
    boxes[i].append(i)

distances = []

for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        dist_sqr = (boxes[i][0] - boxes[j][0]) ** 2 + (boxes[i][1] - boxes[j][1]) ** 2 + (boxes[i][2] - boxes[j][2]) ** 2
        distances.append((dist_sqr, i, j))

while True:
    min_distance = min(distances)
    dist, box_1, box_2 = min_distance
    box_1_circuit = boxes[box_1][3]
    box_2_circuit = boxes[box_2][3]
    print(min_distance)
    if box_1_circuit != box_2_circuit:
        for box in boxes:
            if box[3] == box_2_circuit:
                box[3] = box_1_circuit

    are_connected = True
    curr_circuit = boxes[0][3]
    for box in boxes:
        if box[3] != curr_circuit:
            are_connected = False
            break
    
    if are_connected:
        break
    
    distances.remove(min_distance)


coord_mult = boxes[box_1][0] * boxes[box_2][0]

print(coord_mult)
