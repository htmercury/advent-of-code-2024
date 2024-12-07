from pathlib import Path
current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + '/input.txt', 'r')
data_lines = input_file.readlines()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def parse_inputs(lines):
    obstacles = set()
    
    y_max = len(lines)
    x_max = len(lines[0])
    
    for y, line in enumerate(lines):
        line = line.strip()
        for x, char in enumerate(line):
            if char == '#':
                obstacles.add((y, x))
            elif char == '^':
                src = (y, x)
        
    return y_max, x_max, obstacles, src

def is_in_bounds(loc, y_max, x_max):
    y_loc, x_loc = loc
    return 0 <= y_loc < y_max and 0 <= x_loc < x_max

def solution():
    y_max, x_max, obstacles, src = parse_inputs(data_lines)
    visited = set()
    
    dir_idx = 0
    curr_loc = src
    
    while is_in_bounds(curr_loc, y_max, x_max):
        curr_dir = directions[dir_idx]
        next_loc = (curr_loc[0] + curr_dir[0], curr_loc[1] + curr_dir[1])
        if next_loc not in obstacles:
            curr_loc = next_loc
            visited.add(next_loc)
        else:
            dir_idx = (dir_idx + 1) % len(directions)
        
    return len(visited) - 1

print(solution())
