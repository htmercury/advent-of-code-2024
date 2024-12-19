from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def parse_inputs(lines):
    byte_positions = []
    for line in lines:
        line = line.strip().split(",")
        byte_positions.append((int(line[1]), int(line[0])))

    return byte_positions


def visualize(y_max, x_max, obstacles, path):
    for y in range(y_max):
        curr_line = ""
        for x in range(x_max):
            if (y, x) in obstacles:
                curr_line += "#"
            elif (y, x) in path:
                curr_line += "O"
            else:
                curr_line += "."
        print(curr_line)

    print("\n")


def is_in_bounds(y_max, x_max, pos):
    curr_y, curr_x = pos

    return 0 <= curr_y < y_max and 0 <= curr_x < x_max


def solution():
    byte_positions = parse_inputs(data_lines)
    obstacles = set()
    src = (0, 0)
    dst = (70, 70)
    y_max, x_max = (dst[0] + 1, dst[1] + 1)
    t = 1024

    for i in range(t):
        obstacles.add(byte_positions[i])

    # visualize(y_max, x_max, obstacles, set())

    path_q = []
    path_q.append((src, set([src])))
    visited = set()

    while len(path_q) != 0:
        curr_pos, path = path_q.pop(0)

        if curr_pos == dst:
            best_path = path
            break

        for dir in directions:
            next_pos = (curr_pos[0] + dir[0], curr_pos[1] + dir[1])

            if (
                is_in_bounds(y_max, x_max, next_pos)
                and next_pos not in obstacles
                and next_pos not in visited
            ):
                visited.add(next_pos)
                next_path = path.copy()
                next_path.add(next_pos)
                path_q.append((next_pos, next_path))

    # visualize(y_max, x_max, obstacles, best_path)

    return len(best_path) - 1


print(solution())
