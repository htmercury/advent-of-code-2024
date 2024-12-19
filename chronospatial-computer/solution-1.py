from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()


def parse_inputs(lines):
    registers = []

    for line in lines:
        line = line.strip()

        if len(registers) < 3:
            registers.append(int(line[12:]))
        elif len(line) == 0:
            continue
        else:
            program = list(map(lambda c: int(c), line[9:].split(",")))

    return registers, program


def get_combo_operand(operand, registers):
    if operand <= 3:
        return operand
    elif operand == 4:
        return registers[0]
    elif operand == 5:
        return registers[1]
    elif operand == 6:
        return registers[2]
    else:
        raise Exception(
            "Combo operand 7 is reserved and will not appear in valid programs."
        )


def adv(param, registers, instruction_pointer):
    registers[0] = registers[0] // 2**param
    return (2 + instruction_pointer, [])


def bxl(param, registers, instruction_pointer):
    registers[1] = registers[1] ^ param
    return (2 + instruction_pointer, [])


def bst(param, registers, instruction_pointer):
    registers[1] = param % 8
    return (2 + instruction_pointer, [])


def jnz(param, registers, instruction_pointer):
    if registers[0] != 0:
        return (param, [])
    else:
        return (2 + instruction_pointer, [])


def bxc(param, registers, instruction_pointer):
    registers[1] = registers[1] ^ registers[2]
    return (2 + instruction_pointer, [])


def out(param, registers, instruction_pointer):
    return (instruction_pointer + 2, [param % 8])


def bdv(param, registers, instruction_pointer):
    registers[1] = registers[0] // 2**param
    return (instruction_pointer + 2, [])


def cdv(param, registers, instruction_pointer):
    registers[2] = registers[0] // 2**param
    return (instruction_pointer + 2, [])


def get_instruction(opcode, registers):
    if opcode == 0:
        return lambda param, ptr: adv(
            get_combo_operand(param, registers), registers, ptr
        )
    elif opcode == 1:
        return lambda param, ptr: bxl(param, registers, ptr)
    elif opcode == 2:
        return lambda param, ptr: bst(
            get_combo_operand(param, registers), registers, ptr
        )
    elif opcode == 3:
        return lambda param, ptr: jnz(param, registers, ptr)
    elif opcode == 4:
        return lambda param, ptr: bxc(param, registers, ptr)
    elif opcode == 5:
        return lambda param, ptr: out(
            get_combo_operand(param, registers), registers, ptr
        )
    elif opcode == 6:
        return lambda param, ptr: bdv(
            get_combo_operand(param, registers), registers, ptr
        )
    elif opcode == 7:
        return lambda param, ptr: cdv(
            get_combo_operand(param, registers), registers, ptr
        )
    else:
        raise Exception("No more opcodes.")


def solution():
    registers, program = parse_inputs(data_lines)
    instruction_pointer = 0
    outputs = []

    # print(registers, program)

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        param = program[instruction_pointer + 1]

        # execute each line of program
        perform_instruction = get_instruction(opcode, registers)
        next_pointer, output = perform_instruction(param, instruction_pointer)

        outputs += output
        instruction_pointer = next_pointer

    # print(registers, outputs)
    outputs = ','.join(map(lambda o: str(o), outputs))
    return outputs


print(solution())
