from pathlib import Path
import heapq

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def parse_inputs(lines):
    obstacles = set()

    for y, line in enumerate(lines):
        line = line.strip()

        for x, char in enumerate(line):
            if char == "#":
                obstacles.add((y, x))
            elif char == "E":
                dst = (y, x)
            elif char == "S":
                src = (y, x)

    return obstacles, src, dst


def solution():
    obstacles, src, dst = parse_inputs(data_lines)

    visited_scores = {(src, 1): 0}
    path_q = []
    heapq.heappush(path_q, (0, src, 1, set([src])))

    best_score = None
    best_paths = []

    while len(path_q) != 0:
        score, curr_pos, curr_dir_idx, path = heapq.heappop(path_q)
        curr_dir = directions[curr_dir_idx]

        if curr_pos == dst:
            if best_score == None:
                best_score = score
            else:
                if score > best_score:
                    break

            best_paths.append(path)

        next_pos = (curr_pos[0] + curr_dir[0], curr_pos[1] + curr_dir[1])
        if next_pos not in obstacles and (
            (next_pos, curr_dir_idx) not in visited_scores
            or visited_scores[(next_pos, curr_dir_idx)] >= (score + 1)
        ):
            visited_scores[(next_pos, curr_dir_idx)] = score + 1
            new_path = path.copy()
            new_path.add(next_pos)
            heapq.heappush(path_q, (score + 1, next_pos, curr_dir_idx, new_path))

        reverse_dir_idx = (curr_dir_idx - 1) % len(directions)
        forward_dir_idx = (curr_dir_idx + 1) % len(directions)

        if (curr_pos, reverse_dir_idx) not in visited_scores or visited_scores[
            (curr_pos, reverse_dir_idx)
        ] >= (score + 1000):
            visited_scores[(curr_pos, reverse_dir_idx)] = score + 1000
            heapq.heappush(path_q, (score + 1000, curr_pos, reverse_dir_idx, path))

        if (curr_pos, forward_dir_idx) not in visited_scores or visited_scores[
            (curr_pos, forward_dir_idx)
        ] >= (score + 1000):
            visited_scores[(curr_pos, forward_dir_idx)] = score + 1000
            heapq.heappush(path_q, (score + 1000, curr_pos, forward_dir_idx, path))

    best_tiles_set = best_paths[0]

    for i in range(1, len(best_paths)):
        best_tiles_set = best_tiles_set | best_paths[i]

    return len(best_tiles_set)


print(solution())
