from pathlib import Path
current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + '/input.txt', 'r')
data_lines = input_file.readlines()

def parse_inputs(lines):
    list_one = []
    table_two = {}
    
    for line in lines:
        line = line.strip().split('   ')
        value_one = int(line[0])
        value_two = int(line[1])
        list_one.append(value_one)
        if value_two in table_two:
            table_two[value_two] += 1
        else:
            table_two[value_two] = 1

    return list_one, table_two

def solution():
    list_one, table_two = parse_inputs(data_lines)
    result  = 0
    for val in list_one:
        if val in table_two:
            result += (val * table_two[val])
            
    return result

print(solution())
