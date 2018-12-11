import sys
from typing import Dict, Tuple


def find_square_of_any_size_with_biggest_power(grid_serial_number: int) -> Tuple[int, int, int]:
    biggest_power = 0
    biggest_square = (0, 0)
    biggest_square_size = 0

    for square_size in range(1, 301):
        print(square_size)
        x, y, power = find_square_with_biggest_power(square_size, grid_serial_number)
        if power > biggest_power:
            biggest_power = power
            biggest_square = (x, y)
            biggest_square_size = square_size

    return biggest_square[0], biggest_square[1], biggest_square_size


def find_square_with_biggest_power(square_size: int, grid_serial_number: int) -> Tuple[int, int, int]:
    area = create_area(grid_serial_number)
    biggest_power = 0
    biggest_square = (0, 0)

    for i in range(1, 300 - square_size + 2):
        for j in range(1, 300 - square_size + 2):
            power = calculate_square_power(square_size, i, j, area)
            if power > biggest_power:
                biggest_power = power
                biggest_square = (i, j)

    return biggest_square[0], biggest_square[1], biggest_power


def calculate_cell_power_level(x: int, y: int, grid_serial_number: int) -> int:
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial_number
    power_level *= rack_id
    power_level = get_hundreds_digit(power_level)
    power_level -= 5

    return power_level


def get_hundreds_digit(value: int) -> int:
    if value < 100:
        return 0

    return int(str(value)[-3])


def create_area(grid_serial_number) -> Dict[Tuple[int, int], int]:
    area = {}

    for i in range(1, 301):
        for j in range(1, 301):
            area[(i, j)] = calculate_cell_power_level(i, j, grid_serial_number)

    return area


def calculate_square_power(square_size: int, x_start, y_start, area: Dict[Tuple[int, int], int]) -> int:
    square_power = 0

    for i in range(x_start, x_start + square_size):
        for j in range(y_start, y_start + square_size):
            square_power += area[(i, j)]

    return square_power


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <grid serial number>")
        exit()

    grind_serial_number = int(sys.argv[1])
    print(find_square_with_biggest_power(3, grind_serial_number))
    print(find_square_of_any_size_with_biggest_power(grind_serial_number))