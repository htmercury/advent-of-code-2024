from pathlib import Path
current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + '/input.txt', 'r')
pebble_lines = input_file.readlines()

def parse_inputs(lines):
    return lines[0].strip().split(' ')

def stone_step(stone):
    if stone == '0':
        return ['1']
    elif len(stone) % 2 == 0:
        cut_off_idx = len(stone) // 2
        return [str(int(stone[:cut_off_idx])), str(int(stone[cut_off_idx:]))]
    else:
        return [str(int(stone) * 2024)]

def solution():
    stone_list = parse_inputs(pebble_lines)
    step_count = 25
    
    for _ in range(step_count):
        next_stone_list = []
        for curr_stone in stone_list:
            new_stones = stone_step(curr_stone)
            next_stone_list += new_stones
        
        # print(next_stone_list)
        stone_list = next_stone_list
        
    return len(stone_list)

print(solution())
