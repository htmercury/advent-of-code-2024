from pathlib import Path
import functools

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
            pieces = tuple(line.split(", "))
        else:
            targets.append(line)

    return pieces, targets


def convert_path_to_hash(path):
    hash = ""
    for i in range(len(path)):
        hash += path[i] + str(i)

    return hash

@functools.cache
def get_alternatives(pieces, target):
    if len(target) == 0:
        return 1

    result = 0
    for p in pieces:
        if target.startswith(p):
            result += get_alternatives(pieces, target[len(p):])

    return result


def solution():
    pieces, targets = parse_inputs(data_lines)
    result = 0

    for target in targets:
        counter = get_alternatives(pieces, target)
        # print(counter, target)
        result += counter

    return result


print(solution())
