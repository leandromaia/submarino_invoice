#!/usr/bin/python3

def request_input_file_path():
    return input("Type the raw file path: ")

def read_file_lines():
    try:
        input_path = request_input_file_path()
        with open(input_path, 'r') as reader:
            return reader.readlines()
    except OSError as e:
        print("Error during read input file. Message: {0}".format(e)) 

def start():
    print("-----------Read Submarino Invoice Data------------\n")
    
    list_line_objects = list()

    for line in read_file_lines():
        total_values = len(line.split())
        date = line.split()[0]
        value = line.split()[total_values-2:total_values-1][0]
        raw_description = line.replace(date, "").replace(value, "")
        raw_description = raw_description.strip('D\n').strip()

        obj_line = {
            "date": date,
            "description": raw_description,
            "value": value
        }
        list_line_objects.append(obj_line)

    file_csv_path = 'final_file.csv'

    writer = open(file_csv_path, 'w')

    for obj in list_line_objects:
        writer.writelines("{0};{1};{2}\n".format(
                                        obj.get('date'),
                                        obj.get('description'),
                                        obj.get('value')))

    writer.close()

if __name__ == '__main__':
    start()