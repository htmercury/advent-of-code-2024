from pathlib import Path

current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + "/input.txt", "r")
data_lines = input_file.readlines()

directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def parse_inputs(lines):
    y_max = len(data_lines)
    x_max = len(data_lines[0].strip() * 2)
    obstacles = set()
    boxes = set()
    commands = ""
    is_command = False

    for y, line in enumerate(lines):
        line = line.strip()

        if len(line) == 0:
            is_command = True

        if is_command:
            y_max -= 1

        for x, char in enumerate(line):
            curr_x = x * 2
            if is_command:
                commands += char
            else:
                if char == "#":
                    obstacles.add((y, curr_x))
                    obstacles.add((y, curr_x + 1))
                elif char == "O":
                    boxes.add(((y, curr_x), (y, curr_x + 1)))
                elif char == "@":
                    robot = (y, curr_x)

    return y_max, x_max, commands, obstacles, boxes, robot


def visualize_map(y_max, x_max, obstacles, boxes, robot):
    box_half_skip = False
    for y in range(y_max):
        curr_line = ""
        for x in range(x_max):
            if box_half_skip:
                box_half_skip = False
                continue
            if (y, x) in obstacles:
                curr_line += "#"
            elif (y, x) in set(map(lambda b: b[0], boxes)):
                curr_line += "[]"
                box_half_skip = True
            elif (y, x) == robot:
                curr_line += "@"
            else:
                curr_line += "."
        print(curr_line)

    print("\n")


def flatten(xss):
    return [x for xs in xss for x in xs]


def move_pos(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])


def solution():
    y_max, x_max, commands, obstacles, boxes, robot = parse_inputs(data_lines)
    result = 0
    # visualize_map(y_max, x_max, obstacles, boxes, robot)

    for char in commands:
        move = directions[char]
        next_pos = (robot[0] + move[0], robot[1] + move[1])

        flattened_boxes = set(flatten(boxes))
        chained_boxes = []
        is_valid_move = True

        if next_pos in obstacles:
            # print("Move " + char + ":")
            # visualize_map(y_max, x_max, obstacles, boxes, robot)
            continue
        elif next_pos in flattened_boxes:
            remaining_boxes = boxes.copy()
            for box in remaining_boxes:
                if next_pos == box[0] or next_pos == box[1]:
                    target_box = box
                    remaining_boxes.remove(box)
                    break

            curr_boxes = [target_box]
            target_moves = list(
                map(lambda b: (move_pos(b[0], move), move_pos(b[1], move)), curr_boxes)
            )
            chained_boxes.append((curr_boxes, target_moves))
            flattened_target_moves = flatten(target_moves)

            if any(map(lambda tp: tp in obstacles, flattened_target_moves)):
                is_valid_move = False

            while any(
                map(
                    lambda tp: tp in set(flatten(remaining_boxes)),
                    flattened_target_moves,
                )
            ):
                curr_boxes = []
                for target_pos in flattened_target_moves:
                    for box in remaining_boxes:
                        if target_pos == box[0] or target_pos == box[1]:
                            curr_boxes.append(box)
                            remaining_boxes.remove(box)
                            break
                target_moves = list(
                    map(
                        lambda b: (move_pos(b[0], move), move_pos(b[1], move)),
                        curr_boxes,
                    )
                )
                chained_boxes.append((curr_boxes, target_moves))
                flattened_target_moves = flatten(target_moves)

                if any(map(lambda tp: tp in obstacles, flattened_target_moves)):
                    is_valid_move = False

            # chain move free spot
            if is_valid_move:
                for curr_boxes, target_moves in reversed(chained_boxes):
                    for prev_box, new_box in zip(curr_boxes, target_moves):
                        boxes.remove(prev_box)
                        boxes.add(new_box)
                # update this tracker
                flattened_boxes = set(flatten(boxes))
            else:
                # print("Move " + char + ":", robot, "not valid")
                # visualize_map(y_max, x_max, obstacles, boxes, robot)
                continue

        robot = next_pos
        # print("Move " + char + ":", robot)
        # visualize_map(y_max, x_max, obstacles, boxes, robot)

    # visualize_map(y_max, x_max, obstacles, boxes, robot)

    for pos, _ in boxes:
        result += 100 * pos[0] + pos[1]

    return result


print(solution())
