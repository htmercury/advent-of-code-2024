from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()

target_set = set({"M", "S"})

checks = [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]


def parse_inputs(lines):
    all_locations = {}
    a_locations = []

    y_max = len(lines)
    x_max = len(lines[0])

    for y, line in enumerate(lines):
        line = line.strip()
        for x, char in enumerate(line):
            all_locations[(y, x)] = char
            if char == "A":
                a_locations.append((y, x))

    return all_locations, a_locations, y_max, x_max


def is_in_bounds(coord, y_max, x_max):
    curr_y, curr_x = coord
    return 0 <= curr_y < y_max and 0 <= curr_x < x_max


def solution():
    all_locations, a_locations, y_max, x_max = parse_inputs(data_lines)

    result = 0

    for a_loc in a_locations:
        is_valid = True
        for directions in checks:
            stored_chars = set()
            for dir in directions:
                next_loc = (a_loc[0] + dir[0], a_loc[1] + dir[1])
                if next_loc in all_locations:
                    stored_chars.add(all_locations[next_loc])

            if stored_chars != target_set:
                is_valid = False

        if is_valid:
            result += 1

    return result


print(solution())
