from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()


def parse_inputs(lines):
    targets = []
    is_pieces = True

    for line in lines:
        line = line.strip()

        if len(line) == 0:
            is_pieces = False
            continue

        if is_pieces:
            pieces = set(line.split(", "))
        else:
            targets.append(line)

    return pieces, targets


def solution():
    pieces, targets = parse_inputs(data_lines)
    result = 0

    max_len = 0
    for piece in pieces:
        max_len = max(len(piece), max_len)

    for target in targets:
        build_q = []
        build_q.append((0, []))
        match = None
        visited = set([0])

        while len(build_q) != 0:
            curr_idx, path = build_q.pop()

            if curr_idx == len(target):
                match = path
                break

            remaining_target = target[curr_idx:]
            # print(remaining_target)

            for i in range(max_len):
                if i > len(remaining_target):
                    break
                towel_token = remaining_target[: i + 1]

                if towel_token in pieces and curr_idx + i + 1 not in visited:
                    visited.add(curr_idx + i + 1)
                    new_path = path.copy()
                    new_path.append(towel_token)
                    build_q.append((curr_idx + i + 1, new_path))

        if match != None:
            # print(match)
            result += 1

    return result


print(solution())
