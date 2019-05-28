#!/usr/bin/python3
print("-----------Read Submarino Invoice Data------------\n")

path = input("Type the raw file path: ")

reader = open(path, 'r')

list_line_objects = list()

for line in reader.readlines():
    total_values = len(line.split())
    date = line.split()[0]
    value = line.split()[total_values-2:total_values-1][0]
    raw_description = line.replace(date, "").replace(value, "")

    obj_line = {
        "date": date,
        "description": raw_description,
        "value": value
    }
    list_line_objects.append(obj_line)

reader.close()

file_csv_path = 'final_file.csv'

writer = open(file_csv_path, 'w')

for obj in list_line_objects:
    writer.write("{0};{1};{2}".format(
                                    obj.get('date'),
                                    obj.get('description'),
                                    obj.get('value')))

writer.close()
