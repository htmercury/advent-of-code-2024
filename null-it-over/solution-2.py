from pathlib import Path
import re
current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + '/input.txt', 'r')
data_lines = input_file.readlines()

mul_regex = r"mul\(\d{1,3},\d{1,3}\)"
do_dont_regex = r"do\(\)|don't\(\)"

def parse_inputs(lines):
    full_str = ''
    for line in lines:
        line = line.strip()
        full_str += line

    mul_matches = re.finditer(mul_regex, full_str, re.MULTILINE)
    do_dont_matches = re.finditer(do_dont_regex, full_str, re.MULTILINE)

    return mul_matches, do_dont_matches, len(full_str)

def solution():
    mul_commands, do_dont_commands, len_str = parse_inputs(data_lines)

    result = 0

    last_allowed = 0
    allowed_locs = []
    
    curr_allowed = True
    for c in do_dont_commands:
        if c.group() == 'don\'t()':
            if curr_allowed:
                curr_allowed = False
                allowed_locs.append((last_allowed, c.span()[0]))
        else:
            if not curr_allowed:
                curr_allowed = True
                last_allowed = c.span()[0]

    ## if loops stop while allowed, add last additional range
    if curr_allowed:
        allowed_locs.append((last_allowed, len_str))

    for c in mul_commands:
        mul_command = c.group()
        curr_loc = c.span()[0]

        is_valid = False
        # confirm if in do-able
        for locs in allowed_locs:
            if curr_loc >= locs[0] and curr_loc < locs[1]:
                is_valid = True

        if is_valid:
            mul_args = mul_command[4:-1].split(',')
            result += (int(mul_args[0]) * int(mul_args[1]))

    return result

print(solution())
