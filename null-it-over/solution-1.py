from pathlib import Path
import re
current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + '/input.txt', 'r')
data_lines = input_file.readlines()

regex = r"mul\(\d{1,3},\d{1,3}\)"

def parse_inputs(lines):
    full_str = ''
    for line in lines:
        line = line.strip()
        full_str += line

    matches = re.finditer(regex, full_str, re.MULTILINE)

    return matches

def solution():
    commands = parse_inputs(data_lines)

    result = 0
    
    for c in commands:
        mul_command = c.group()
        mul_args = mul_command[4:-1].split(',')
        result += (int(mul_args[0]) * int(mul_args[1]))

    return result

print(solution())
