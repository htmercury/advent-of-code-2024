from pathlib import Path
import re

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()

regex = r"\d+"
prize_offset = 10000000000000


def parse_inputs(lines):
    machines = []

    curr_machine = []
    for line in lines:
        line = line.strip()

        if len(line) == 0:
            machines.append(curr_machine)
            curr_machine = []
        else:
            # parse offsets
            matches = re.finditer(regex, line, re.MULTILINE)

            offsets = []
            for offset in matches:
                offsets.append(int(offset.group()))
            curr_machine.append(offsets)

    if curr_machine != []:
        machines.append(curr_machine)

    return machines


def solution():
    machines = parse_inputs(data_lines)
    result = 0

    for machine in machines:
        button_a, button_b, prize = machine
        prize = (prize[0] + prize_offset, prize[1] + prize_offset)
        # construct linear equations and solve for intersection
        # a_presses = (8400 - 22(5400) / 67) / (94 - 22(34) / 67)
        a_presses = (prize[0] * button_b[1] - button_b[0] * prize[1]) / (
            button_a[0] * button_b[1] - (button_b[0] * button_a[1])
        )

        # b_presses = (5400 - 34a) / 67
        b_presses = (prize[1] - button_a[1] * a_presses) / button_b[1]

        if not a_presses.is_integer() or not b_presses.is_integer():
            continue

        # print(a_presses, b_presses)

        result += (int(a_presses) * 3) + int(b_presses)

    # print(machines)

    return result


print(solution())
