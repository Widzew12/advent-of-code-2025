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

output_string = ""
lines = 0
for dev in devices_dict:
    output_string += str(dev) + " "
    out_devices = devices_dict[dev]
    output_string += str(len(out_devices)) + " "
    for out_dev in out_devices:
        output_string += str(out_dev) + " "
    output_string += "\n"
    lines += 1

output_string = str(lines) + "\n" + output_string

with open("output.txt", "w") as output_file:
    output_file.write(output_string)
