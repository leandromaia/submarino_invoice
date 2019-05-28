#!/usr/bin/python3
print("-----------Read Submarino Invoice Data------------\n")

path = input("Type the raw file path: ")

reader = open(path, 'r')

list_line_objects = list()

for line in reader.readlines():
    total_values = len(line.split())
    obj_line = {
        "date": line.split()[0],
        "description":
        "value": line.split()[total_values-2:total_values-1]
    }
    import pdb; pdb.set_trace()