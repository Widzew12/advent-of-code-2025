with open("/home/szymon/Drives/Files/Programowanie/Advent of code/advent-of-code-2025/day-11/input.txt", "r") as input_file:
    devices_dict_old = {l[0]: l[1].split(" ") for l in [line.strip().split(": ") for line in input_file.readlines()]}

devices_indexes = ["svr", "out", "dac", "fft"]

devices_dict = dict()

for dev in devices_dict_old:
    if dev not in devices_indexes:
        devices_indexes.append(dev)
    dev_new = devices_indexes.index(dev)
    
    out = devices_dict_old[dev]
    out_new = []
    for o in out:
        if o not in devices_indexes:
            devices_indexes.append(o)
        out_new.append(devices_indexes.index(o))
    
    devices_dict[dev_new] = out_new

def check_paths(curr_device, prev_devices):
    if curr_device in prev_devices:
        return 0

    if curr_device in no_out and 2 not in prev_devices and 3 not in prev_devices:
        return 0
    
    new_prev_devices = prev_devices.copy()
    new_prev_devices.add(curr_device)
    paths = 0
    for output_device in devices_dict[curr_device]:
        if output_device == 1:
            if 2 in new_prev_devices and 3 in new_prev_devices:
                paths += 1
        else:
            paths += check_paths(output_device, new_prev_devices)
    
    if paths == 0:
        if curr_device not in no_out:
            no_out.add(curr_device)
            print(curr_device)
    if paths > 10000:
        print(paths)
    return paths

no_out = set()

result = check_paths(0, set())

print()
print("success!!!!")
print(result)
