import PySimpleGUI as sg
import random
import time

from collections import namedtuple

GRID_SIZE = 600
NR_CELLS = 12
CELL_SIZE = GRID_SIZE // NR_CELLS
GRID_COLOR = "white"

DIRECTIONS = {"left": (-1, 0), "right": (1, 0), "up": (0, 1), "down": (0, -1)}

Cell = namedtuple("Cell", ["x", "y"])

ALL_CELLS_IN_GRID = frozenset({Cell(x, y) for x in range(NR_CELLS) for y in range(NR_CELLS)})


def create_window():
    layout = [
        [sg.Graph(
            key="-GRID-",
            canvas_size=(GRID_SIZE, GRID_SIZE),
            graph_bottom_left=(0, 0),
            graph_top_right=(GRID_SIZE, GRID_SIZE),
            background_color=GRID_COLOR)
        ]
    ]

    return sg.Window("Snake game", layout, return_keyboard_events=True, finalize=True)


def cell_to_pixel(cell):
    top_left = (cell.x * CELL_SIZE, cell.y * CELL_SIZE)
    bottom_right = top_left[0] + CELL_SIZE, top_left[1] + CELL_SIZE
    return top_left, bottom_right


def create_target(snake):
    return random.choice(tuple(ALL_CELLS_IN_GRID.difference(snake)))


def is_snake_on_board(snake_head):
    return (0 <= snake_head.x < NR_CELLS) and (0 <= snake_head.y < NR_CELLS)


def update_snake(snake, direction, target_reached=False):
    head = snake[0]
    new_head = Cell(head.x + direction[0], head.y + direction[1])
    snake.insert(0, new_head)
    if not target_reached:
        _ = snake.pop(-1)


def speed_up_game(snake_size):
    if snake_size <= 10:
        return 0.4

    if 10 < snake_size <= 20:
        return 0.3

    return 0.2


def update_snake_on_board(window, snake):
    for ix, body_part in enumerate(snake):
        tl, br = cell_to_pixel(body_part)
        color = "green" if ix != 0 else "yellow"
        window["-GRID-"].DrawRectangle(tl, br, color)


def main():
    window = create_window()
    snake = [Cell(4, 4), Cell(3, 4), Cell(2, 4)]
    snake_size = len(snake)
    target_position = create_target(snake)

    direction = DIRECTIONS["up"]
    start_time = time.time()

    while True:
        event, _ = window.read(timeout=10)

        time_difference = speed_up_game(snake_size)

        if event == sg.WIN_CLOSED or event == "-EXIT-":
            break

        elif event.startswith("Left:") or event.startswith("KP_Left"):
            direction = DIRECTIONS["left"]

        elif event.startswith("Right:") or event.startswith("KP_Right"):
            direction = DIRECTIONS["right"]

        elif event.startswith("Up:") or event.startswith("KP_Up"):
            direction = DIRECTIONS["up"]

        elif event.startswith("Down:") or event.startswith("KP_Down"):
            direction = DIRECTIONS["down"]

        if (time.time() - start_time) >= time_difference:
            start_time = time.time()

            if snake[0] == target_position:
                target_position = create_target(snake)
                snake_size += 1
                update_snake(snake, direction, target_reached=True)
            else:
                update_snake(snake, direction, target_reached=False)

            head = snake[0]
            if not is_snake_on_board(head) or head in snake[1:]:
                sg.popup_ok("Game over!")
                break

            # clear all previous content
            window["-GRID-"].DrawRectangle((0, 0), (GRID_SIZE, GRID_SIZE), GRID_COLOR)

            top_left, bottom_right = cell_to_pixel(target_position)
            window["-GRID-"].DrawRectangle(top_left, bottom_right, "red")
            update_snake_on_board(window, snake)


    window.close()


if __name__ == "__main__":
    main()
