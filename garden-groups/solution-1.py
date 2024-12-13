from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def parse_inputs(lines):
    garden_dict = {}
    remaining_plots = set()

    for y, line in enumerate(lines):
        line = line.strip()
        for x, char in enumerate(line):
            garden_dict[(y, x)] = char
            remaining_plots.add((y, x))

    return garden_dict, remaining_plots


def flood_fill(loc, curr_plot, garden_dict, remaining_plots):
    for d in directions:
        next_loc = (loc[0] + d[0], loc[1] + d[1])
        if (
            next_loc in garden_dict
            and garden_dict[next_loc] == garden_dict[loc]
            and next_loc in remaining_plots
        ):
            remaining_plots.remove(next_loc)
            curr_plot.add(next_loc)
            flood_fill(next_loc, curr_plot, garden_dict, remaining_plots)


def solution():
    garden_dict, remaining_plots = parse_inputs(data_lines)
    result = 0

    while len(remaining_plots) != 0:
        curr_plot = set()
        src_loc = remaining_plots.pop()
        curr_plot.add(src_loc)
        flood_fill(src_loc, curr_plot, garden_dict, remaining_plots)
        
        curr_area = len(curr_plot)
        curr_perimeter = 0
        
        for loc in curr_plot:
            for d in directions:
                adj_loc = (loc[0] + d[0], loc[1] + d[1])
                if adj_loc not in curr_plot:
                    curr_perimeter += 1
                    
        # print(curr_area, curr_perimeter)
        result += (curr_area * curr_perimeter)

    return result


print(solution())
