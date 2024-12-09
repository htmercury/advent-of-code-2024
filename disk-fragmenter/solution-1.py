from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
disk_lines = input_file.readlines()


def parse_inputs(lines):
    disk_map = lines[0].strip()

    curr_id = 0
    is_block_size = True

    raw_map = []

    for char in disk_map:
        if is_block_size:
            raw_map += [str(curr_id)] * int(char)
            curr_id += 1
            is_block_size = False
        else:
            raw_map += list("." * int(char))
            is_block_size = True

    return raw_map


def solution():
    raw_map = parse_inputs(disk_lines)
    result = 0
    
    prev_ptr = 0
    next_ptr = len(raw_map) - 1
    
    # print(''.join(raw_map))
    while prev_ptr < next_ptr:
        if raw_map[prev_ptr] != '.':
            prev_ptr += 1
            continue
        elif raw_map[next_ptr] == '.':
            next_ptr -= 1
            continue
        else:
            raw_map[prev_ptr] = raw_map[next_ptr]
            raw_map[next_ptr] = '.'
    
    # print(''.join(raw_map))
    for i in range(len(raw_map)):
        if raw_map[i] == '.':
            break
        
        result += (i * int(raw_map[i]))

    return result


print(solution())
