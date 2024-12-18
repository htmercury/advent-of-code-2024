from pathlib import Path
import heapq

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def parse_inputs(lines):
    obstacles = set()
    y_max = len(data_lines)
    x_max = len(data_lines[0].strip())

    for y, line in enumerate(lines):
        line = line.strip()

        for x, char in enumerate(line):
            if char == "#":
                obstacles.add((y, x))
            elif char == "E":
                dst = (y, x)
            elif char == "S":
                src = (y, x)

    return y_max, x_max, obstacles, src, dst


def solution():
    y_max, x_max, obstacles, src, dst = parse_inputs(data_lines)

    visited_scores = {(src, 1): 0}
    path_q = []
    heapq.heappush(path_q, (0, src, 1))

    while len(path_q) != 0:
        score, curr_pos, curr_dir_idx = heapq.heappop(path_q)
        curr_dir = directions[curr_dir_idx]

        if curr_pos == dst:
            return score

        next_pos = (curr_pos[0] + curr_dir[0], curr_pos[1] + curr_dir[1])
        if next_pos not in obstacles and (
            (next_pos, curr_dir_idx) not in visited_scores
            or visited_scores[(next_pos, curr_dir_idx)] > (score + 1)
        ):
            visited_scores[(next_pos, curr_dir_idx)] = score + 1
            heapq.heappush(path_q, (score + 1, next_pos, curr_dir_idx))

        reverse_dir_idx = (curr_dir_idx - 1) % len(directions)
        forward_dir_idx = (curr_dir_idx + 1) % len(directions)

        if (curr_pos, reverse_dir_idx) not in visited_scores or visited_scores[
            (curr_pos, reverse_dir_idx)
        ] > (score + 1000):
            visited_scores[(curr_pos, reverse_dir_idx)] = score + 1000
            heapq.heappush(path_q, (score + 1000, curr_pos, reverse_dir_idx))

        if (curr_pos, forward_dir_idx) not in visited_scores or visited_scores[
            (curr_pos, forward_dir_idx)
        ] > (score + 1000):
            visited_scores[(curr_pos, forward_dir_idx)] = score + 1000
            heapq.heappush(path_q, (score + 1000, curr_pos, forward_dir_idx))

    return -1


print(solution())
