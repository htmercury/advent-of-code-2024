from pathlib import Path
from functools import cmp_to_key

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()


def parse_inputs(lines):
    page_lists = []
    greater_than_table = {}
    less_than_table = {}
    is_rule = True
    for line in lines:
        line = line.strip()

        if len(line) == 0:
            is_rule = False
            continue

        if is_rule:
            arg_one, arg_two = line.split("|")
            if arg_one not in less_than_table:
                less_than_table[arg_one] = set()
            less_than_table[arg_one].add(arg_two)

            if arg_two not in greater_than_table:
                greater_than_table[arg_two] = set()
            greater_than_table[arg_two].add(arg_one)
        else:
            page_lists.append(line.split(","))

    return greater_than_table, less_than_table, page_lists


def compare(a, b, less_than_table, greater_than_table):
    if a in less_than_table:
        if b in less_than_table[a]:
            return -1
        else:
            return 1

    if b in greater_than_table:
        if a in greater_than_table[b]:
            return -1
        else:
            return 1

    return 0

def solution():
    greater_than_table, less_than_table, page_lists = parse_inputs(data_lines)
    result = 0

    for page_list in page_lists:
        is_valid = True

        for i in range(1, len(page_list)):
            prev_page = page_list[i - 1]
            curr_page = page_list[i]

            if (
                prev_page in less_than_table
                and curr_page not in less_than_table[prev_page]
            ):
                is_valid = False
                break

            if (
                curr_page in greater_than_table
                and prev_page not in greater_than_table[curr_page]
            ):
                is_valid = False
                break

        if not is_valid:
            altered_page_list = sorted(
                page_list,
                key=cmp_to_key(lambda a, b: compare(a, b, less_than_table, greater_than_table)),
            )
            result += int(altered_page_list[((len(page_list) + 1) // 2) - 1])

    return result


print(solution())
