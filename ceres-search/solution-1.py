from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()

target_match = "XMAS"

directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def parse_inputs(lines):
    all_locations = {}
    x_locations = []

    for y, line in enumerate(lines):
        line = line.strip()
        for x, char in enumerate(line):
            all_locations[(y, x)] = char
            if char == "X":
                x_locations.append((y, x))

    return all_locations, x_locations


def solution():
    all_locations, x_locations = parse_inputs(data_lines)

    result = 0

    for x_loc in x_locations:
        for dir in directions:
            is_found = True
            next_loc = x_loc
            for remaining_char in target_match[1:]:
                next_loc = (next_loc[0] + dir[0], next_loc[1] + dir[1])
                if (
                    next_loc not in all_locations
                    or all_locations[next_loc] != remaining_char
                ):
                    is_found = False
                    break

            if is_found:
                result += 1

    return result


print(solution())
