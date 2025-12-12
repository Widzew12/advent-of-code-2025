with open("/home/szymon/Drives/Files/Programowanie/Advent of code/advent-of-code-2025/day-11/input.txt", "r") as input_file:
    devices_dict = {l[0]: l[1].split(" ") for l in [line.strip().split(": ") for line in input_file.readlines()]}

def check_paths(curr_device, prev_devices):
    if curr_device in prev_devices:
        return 0

    if curr_device in no_out and "dac" not in prev_devices and "fft" not in prev_devices:
        return 0
    
    new_prev_devices = prev_devices.copy()
    new_prev_devices.add(curr_device)
    paths = 0
    for output_device in devices_dict[curr_device]:
        if output_device == "out":
            if "dac" in new_prev_devices and "fft" in new_prev_devices:
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

print(check_paths("svr", set()))
