from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
pebble_lines = input_file.readlines()


def parse_inputs(lines):
    stone_dict = {}
    stone_list = lines[0].strip().split(" ")
    for s in stone_list:
        stone_dict[int(s)] = 1
    
    return stone_dict

def stone_step(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        cut_off_idx = len(str(stone)) // 2
        return [int(str(stone)[:cut_off_idx]), int(str(stone)[cut_off_idx:])]
    else:
        return [stone * 2024]


def solution():
    stone_dict = parse_inputs(pebble_lines)
    step_count = 75

    for _ in range(step_count):
        new_stone_dict = {}
        for curr_stone in stone_dict.keys():
            new_stones = stone_step(curr_stone)
            
            for new_stone in new_stones:
                if new_stone not in new_stone_dict:
                    new_stone_dict[new_stone] = stone_dict[curr_stone]
                else:
                    new_stone_dict[new_stone] += stone_dict[curr_stone]
                    
        stone_dict = new_stone_dict
        # print(stone_dict)

    return sum(stone_dict.values())


print(solution())
