from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def parse_inputs(lines):
    src_list = []
    topo_map = {}

    for y, line in enumerate(lines):
        line = line.strip()
        for x, char in enumerate(line):
            if not char.isnumeric():
                continue
            height = int(char)
            if height == 0:
                src_list.append((y, x))
            topo_map[(y, x)] = height

    return topo_map, src_list


def solution():
    topo_map, src_list = parse_inputs(data_lines)

    total_trail_score = 0

    for src in src_list:
        result_count = 0
        q = []
        q.append(src)

        while len(q) > 0:
            curr_pos = q.pop(0)
            curr_level = topo_map[curr_pos]

            if curr_level == 9:
                result_count += 1
                continue

            for d in directions:
                next_pos = (curr_pos[0] + d[0], curr_pos[1] + d[1])
                if next_pos not in topo_map:
                    continue
                next_level = topo_map[next_pos]
                if next_level == curr_level + 1:
                    q.append(next_pos)

        total_trail_score += result_count
        # print(result_list, len(result_list), src)

    return total_trail_score


print(solution())
