from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
disk_lines = input_file.readlines()


def parse_inputs(lines):
    disk_map = lines[0].strip()

    curr_id = 0
    is_block_size = True

    raw_map = []

    free_space_list = []
    block_size_list = []

    curr_idx = 0
    for char in disk_map:
        if is_block_size:
            raw_map += [str(curr_id)] * int(char)
            curr_id += 1
            is_block_size = False

            block_size_list.append((curr_idx, int(char)))
            curr_idx += int(char)
        else:
            raw_map += list("." * int(char))
            is_block_size = True

            free_space_list.append((curr_idx, int(char)))
            curr_idx += int(char)

    # trailing char case
    if not is_block_size:
        free_space_list.append((curr_idx, 0))

    return raw_map, free_space_list, block_size_list


def solution():
    raw_map, free_space_list, block_size_list = parse_inputs(disk_lines)
    result = 0
    block_ptr = len(block_size_list) - 1

    # print(''.join(raw_map))
    while block_ptr > 0:
        block_idx, block_size = block_size_list[block_ptr]

        for i in range(len(free_space_list)):
            free_space_idx, free_space_size = free_space_list[i]

            if free_space_idx > block_idx:
                break

            if free_space_size >= block_size:
                # perform file movement
                for j in range(free_space_idx, free_space_idx + block_size):
                    raw_map[j] = str(block_ptr)
                for k in range(block_idx, block_idx + block_size):
                    raw_map[k] = "."

                # update table
                free_space_list[i] = (
                    free_space_idx + block_size,
                    free_space_size - block_size,
                )
                break

        block_ptr -= 1

    # print(''.join(raw_map))
    for i in range(len(raw_map)):
        if raw_map[i] == ".":
            continue

        result += i * int(raw_map[i])

    return result


print(solution())
