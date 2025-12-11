with open("input.txt", "r") as input_file:
    devices_dict = {l[0]: l[1].split(" ") for l in [line.strip().split(": ") for line in input_file.readlines()]}

def check_paths(curr_device, prev_devices):
    if curr_device in prev_devices:
        return 0
    
    new_prev_devices = prev_devices.copy()
    new_prev_devices.add(curr_device)
    paths = 0
    for output_device in devices_dict[curr_device]:
        if output_device == "out":
            paths += 1
        else:
            paths += check_paths(output_device, new_prev_devices)
    
    return paths

print(check_paths("you", set()))
