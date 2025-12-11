with open("/home/szymon/Drives/Files/Programowanie/Advent of code/advent-of-code-2025/day-10/input.txt", "r") as input_file:
    machines = [([c == "#" for c in line[0][1:-1]], [[int(num) for num in wiring[1:-1].split(",")] for wiring in line[1:-1]], [int(num) for num in line[-1][1:-1].split(",")]) for line in [line.strip().split(" ") for line in input_file.readlines()]]

def sdfsdf(cur_jol, presses):
    if presses > max_presses:
        return False
    
    presses_list = []
    for button in cur_buttons:
        new_jol = cur_jol.copy()
        for light_but in button:
            new_jol[light_but] += 1
        
        if new_jol == target_jol:
            return presses + 1
        
        prsss = sdfsdf(new_jol, presses + 1)
        if prsss:
            presses_list.append(prsss)
    
    if len(presses_list) > 0:
        return min(presses_list)
    return False

total_presses = 0
for _, cur_buttons, target_jol in machines:
    start_jol = [0 for _ in range(len(target_jol))]
    for max_presses in range(12):
        cur_presses = sdfsdf(start_jol, 0)
        print(cur_presses)
        if cur_presses:
            break
    print(cur_presses)
    if not cur_presses:
        print("OOOOOOO")
    total_presses += cur_presses

print(total_presses)
    