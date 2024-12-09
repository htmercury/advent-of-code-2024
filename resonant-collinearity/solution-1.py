from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()


def parse_inputs(lines):
    antenna_dict = {}
    y_max = len(lines)
    x_max = len(lines[0].strip())

    for y, line in enumerate(lines):
        line = line.strip()
        for x, char in enumerate(line):
            if char != ".":
                if char not in antenna_dict:
                    antenna_dict[char] = []
                antenna_dict[char].append((y, x))

    return y_max, x_max, antenna_dict


def visualize_result(lines, result):
    for y, line in enumerate(lines):
        curr_line = ""
        line = line.strip()
        for x, char in enumerate(line):
            if (y, x) in result:
                curr_line += "#"
            else:
                curr_line += char

        print(curr_line)


def is_in_range(loc, y_max, x_max):
    curr_y, curr_x = loc
    return 0 <= curr_y < y_max and 0 <= curr_x < x_max


def solution():
    y_max, x_max, antenna_dict = parse_inputs(data_lines)
    result = set()

    for signal in antenna_dict.keys():
        # compute anti-nodes for each unique pair between antennas
        for i in range(len(antenna_dict[signal])):
            for j in range(i + 1, len(antenna_dict[signal])):
                antenna_one = antenna_dict[signal][i]
                antenna_two = antenna_dict[signal][j]
                dir_vector = (
                    antenna_one[0] - antenna_two[0],
                    antenna_one[1] - antenna_two[1],
                )

                # record anti-node locations
                anti_node_one = (
                    antenna_one[0] + dir_vector[0],
                    antenna_one[1] + dir_vector[1],
                )
                anti_node_two = (
                    antenna_two[0] - dir_vector[0],
                    antenna_two[1] - dir_vector[1],
                )

                if is_in_range(
                    anti_node_one, y_max, x_max
                ) and anti_node_one not in set(antenna_dict[signal]):
                    result.add(anti_node_one)

                if is_in_range(
                    anti_node_two, y_max, x_max
                ) and anti_node_two not in set(antenna_dict[signal]):
                    result.add(anti_node_two)

    # visualize_result(data_lines, result)

    return len(result)


print(solution())
