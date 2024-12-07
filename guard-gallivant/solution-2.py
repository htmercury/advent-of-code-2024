from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def parse_inputs(lines):
    obstacles = set()

    y_max = len(lines)
    x_max = len(lines[0].strip())

    for y, line in enumerate(lines):
        line = line.strip()
        for x, char in enumerate(line):
            if char == "#":
                obstacles.add((y, x))
            elif char == "^":
                src = (y, x)

    return y_max, x_max, obstacles, src


def is_in_bounds(loc, y_max, x_max):
    y_loc, x_loc = loc
    return 0 <= y_loc < y_max and 0 <= x_loc < x_max


def explore_alternative_is_looped(
    obstacles, fake_obstacle, src, dir_idx, y_max, x_max
):
    curr_obstacles = obstacles.copy()
    curr_obstacles.add(fake_obstacle)
    curr_visited = set()
    curr_visited.add((src, dir_idx))
    curr_loc = src

    while is_in_bounds(curr_loc, y_max, x_max):
        curr_dir = directions[dir_idx]
        next_loc = (curr_loc[0] + curr_dir[0], curr_loc[1] + curr_dir[1])
        if next_loc not in curr_obstacles:
            curr_loc = next_loc
            if (next_loc, dir_idx) in curr_visited:
                return True
            else:
                curr_visited.add((next_loc, dir_idx))
        else:
            dir_idx = (dir_idx + 1) % len(directions)
            if (curr_loc, dir_idx) in curr_visited:
                return True
            else:
                curr_visited.add((curr_loc, dir_idx))

    return False


def solution():
    y_max, x_max, obstacles, src = parse_inputs(data_lines)

    result = set()
    dir_idx = 0
    curr_loc = src
    
    possible_obstacles = set()

    while is_in_bounds(curr_loc, y_max, x_max):
        curr_dir = directions[dir_idx]
        next_loc = (curr_loc[0] + curr_dir[0], curr_loc[1] + curr_dir[1])
        
        if not is_in_bounds(next_loc, y_max, x_max):
            break
        elif next_loc not in obstacles:
            curr_loc = next_loc
            possible_obstacles.add(next_loc)
        else:
            dir_idx = (dir_idx + 1) % len(directions)
            
    if src in possible_obstacles:
        possible_obstacles.remove(src)
    
    for fake_obstacle in possible_obstacles:
        if explore_alternative_is_looped(obstacles, fake_obstacle, src, 0, y_max, x_max):
            result.add(fake_obstacle)
    
    return len(result)


print(solution())
