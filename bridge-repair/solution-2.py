from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()


def parse_inputs(lines):
    outputs = []
    inputs_list = []

    for line in lines:
        line = line.strip()
        components = line.split(": ")
        outputs.append(int(components[0]))
        inputs_list.append(list(map(lambda n: int(n), components[1].split(" "))))

    return outputs, inputs_list


def get_next_value(a, b, operator):
    if operator == "MULT":
        return a * b
    elif operator == "ADD":
        return a + b
    elif operator == "CONCAT":
        return int(str(a) + str(b))


def compute_result(inputs, output, input_idx, curr_value):

    if input_idx == len(inputs):
        return curr_value == output

    return (
        compute_result(
            inputs,
            output,
            input_idx + 1,
            get_next_value(curr_value, inputs[input_idx], "MULT"),
        )
        or compute_result(
            inputs,
            output,
            input_idx + 1,
            get_next_value(curr_value, inputs[input_idx], "ADD"),
        )
        or compute_result(
            inputs,
            output,
            input_idx + 1,
            get_next_value(curr_value, inputs[input_idx], "CONCAT"),
        )
    )


def solution():
    outputs, inputs_list = parse_inputs(data_lines)
    result = 0

    for i in range(len(outputs)):
        output = outputs[i]
        inputs = inputs_list[i]
        if compute_result(inputs, output, 1, inputs[0]):
            result += output

    return result


print(solution())
