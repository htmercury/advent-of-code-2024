from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()

directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def parse_inputs(lines):
    y_max = len(data_lines)
    x_max = len(data_lines[0].strip())
    obstacles = set()
    boxes = set()
    commands = ""
    is_command = False

    for y, line in enumerate(lines):
        line = line.strip()

        if len(line) == 0:
            is_command = True

        if is_command:
            y_max -= 1

        for x, char in enumerate(line):
            if is_command:
                commands += char
            else:
                if char == "#":
                    obstacles.add((y, x))
                elif char == "O":
                    boxes.add((y, x))
                elif char == "@":
                    robot = (y, x)

    return y_max, x_max, commands, obstacles, boxes, robot


def visualize_map(y_max, x_max, obstacles, boxes, robot):
    for y in range(y_max):
        curr_line = ""
        for x in range(x_max):
            if (y, x) in obstacles:
                curr_line += "#"
            elif (y, x) in boxes:
                curr_line += "O"
            elif (y, x) == robot:
                curr_line += "@"
            else:
                curr_line += "."
        print(curr_line)

    print("\n")


def solution():
    y_max, x_max, commands, obstacles, boxes, robot = parse_inputs(data_lines)
    result = 0
    # visualize_map(y_max, x_max, obstacles, boxes, robot)

    for char in commands:
        move = directions[char]
        next_pos = (robot[0] + move[0], robot[1] + move[1])

        if next_pos in obstacles:
            # print('Move ' + char + ':')
            # visualize_map(y_max, x_max, obstacles, boxes, robot)
            continue
        elif next_pos in boxes:
            target_pos = next_pos
            while target_pos in boxes:
                target_pos = (target_pos[0] + move[0], target_pos[1] + move[1])

            # chain move free spot
            if target_pos not in obstacles:
                boxes.remove(next_pos)
                boxes.add(target_pos)
            else:
                # print('Move ' + char + ':', robot)
                # visualize_map(y_max, x_max, obstacles, boxes, robot)
                continue

        robot = next_pos
        # print('Move ' + char + ':', robot)
        # visualize_map(y_max, x_max, obstacles, boxes, robot)

    # visualize_map(y_max, x_max, obstacles, boxes, robot)

    for pos in boxes:
        result += 100 * pos[0] + pos[1]

    return result


print(solution())
