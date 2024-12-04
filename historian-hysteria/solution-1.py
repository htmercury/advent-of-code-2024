from pathlib import Path
current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + '/input.txt', 'r')
data_lines = input_file.readlines()

def parse_inputs(lines):
    list_one = []
    list_two = []
    
    for line in lines:
        line = line.strip().split('   ')
        list_one.append(int(line[0]))
        list_two.append(int(line[1]))

    list_one.sort()
    list_two.sort()
    return list_one, list_two

def solution():
    list_one, list_two = parse_inputs(data_lines)
    result  = 0
    for i in range(len(data_lines)):
        result += abs(list_one[i] - list_two[i])
        
    return result

print(solution())
