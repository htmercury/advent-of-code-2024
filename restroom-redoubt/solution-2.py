from pathlib import Path
import re

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()

regex = r"-{0,1}\d+"


def parse_inputs(lines):
    robots_pos = []
    robots_speed = []

    for line in lines:
        line = line.strip()
        matches = re.finditer(regex, line, re.MULTILINE)

        robot = []
        curr_pair = []
        for match in matches:
            if len(curr_pair) == 1:
                curr_pair = [int(match.group())] + curr_pair
                robot.append(tuple(curr_pair))
                curr_pair = []
            else:
                curr_pair = [int(match.group())] + curr_pair

        robots_pos.append(robot[0])
        robots_speed.append(robot[1])

    return robots_pos, robots_speed


def visualize_map(y_max, x_max, robots_pos):
    pos_map = {}
    for pos in robots_pos:
        if pos not in pos_map:
            pos_map[pos] = 1
        else:
            pos_map[pos] += 1

    for y in range(y_max):
        curr_line = ""
        for x in range(x_max):
            if (y, x) in pos_map:
                curr_line += str(pos_map[(y, x)])
            else:
                curr_line += "."
        print(curr_line)

    print("\n")

def calculate_safety_factor(y_max, x_max, robots_pos):
    quadrant_counts = [0, 0, 0, 0]
    for pos in robots_pos:
        # count each quadrant
        y_cutoff = (y_max - 1) // 2
        x_cutoff = (x_max - 1) // 2

        y_pos, x_pos = pos

        if x_pos < x_cutoff:
            if y_pos < y_cutoff:
                # quad 1
                quadrant_counts[0] += 1
            elif y_pos > y_cutoff:
                # quad 3
                quadrant_counts[2] += 1
            else:
                # not in any quadrant
                continue
        elif x_pos > x_cutoff:
            if y_pos < y_cutoff:
                # quad 2
                quadrant_counts[1] += 1
            elif y_pos > y_cutoff:
                # quad 4
                quadrant_counts[3] += 1
            else:
                # not in any quadrant
                continue
        else:
            # not in any quadrant
            continue

    # print(quadrant_counts)

    return (
        quadrant_counts[0]
        * quadrant_counts[1]
        * quadrant_counts[2]
        * quadrant_counts[3]
    )

def solution():
    y_max, x_max = (103, 101)
    robots_pos, robots_speed = parse_inputs(data_lines)
    # visualize_map(y_max, x_max, robots_pos)

    safety_factors = []
    t_max = 10000
    for _ in range(t_max):
        next_robots_pos = []
        for i in range(len(robots_pos)):
            curr_pos = robots_pos[i]
            curr_speed = robots_speed[i]
            next_pos = (
                (curr_pos[0] + curr_speed[0]) % y_max,
                (curr_pos[1] + curr_speed[1]) % x_max,
            )
            next_robots_pos.append(next_pos)
        robots_pos = next_robots_pos
        
        safety_factors.append(calculate_safety_factor(y_max, x_max, robots_pos))
        
        # if _ == 7568 + 1:
            # visualize_map(y_max, x_max, robots_pos)
        
    return safety_factors.index(min(safety_factors)) + 1


print(solution())
