import sys
import functools
from typing import List
from cart import Cart


def read_file(filename):
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.rstrip() for x in content]
    result = [list(x) for x in content]
    return content


def find_carts(paths_map: List[str]) -> List[Cart]:
    carts = []

    for y in range(0, len(paths_map)):
        for x in range(0, len(paths_map[y])):
            if is_cart(paths_map[y][x]):
                carts.append(Cart(x, y, paths_map[y][x]))

    return carts


def is_cart(field: str) -> bool:
    return field == ">" or field == "<" or field == "^" or field == "v"


def remove_carts(paths_map: List[str]) -> List[str]:
    result = []
    for line in paths_map:
        line = line.replace(">", "-")
        line = line.replace("<", "-")
        line = line.replace("^", "|")
        line = line.replace("v", "|")
        result.append(line)

    return result


def print_carts(paths_map: List[str], carts: List[Cart]):
    carts_positions = [c.get_position() for c in carts]

    for y in range(0, len(paths_map)):
        for x in range(0, len(paths_map[y])):
            if (x, y) in carts_positions:
                print(carts[carts_positions.index((x, y))], end="")
            else:
                print(paths_map[y][x], end="")

        print()


def move_carts(paths_map: List[str], carts: List[Cart]) -> List[Cart]:
    tmp: List[Cart] = []

    for i in range(0, len(carts)):
        cart = carts[i]
        cart.move()
        x, y = cart.get_position()

        for c in tmp:
            if c.get_position() == cart.get_position():
                print("Collision at ", c.get_position())
                exit()

        for c in carts[i+1:]:
            if c.get_position() == cart.get_position():
                print("Collision at ", c.get_position())
                exit()

        cart.on_next_field(paths_map[y][x])
        tmp.append(cart)

    return tmp


def compare_carts(cart1: Cart, cart2: Cart) -> int:
    p1 = cart1.get_position()
    p2 = cart2.get_position()

    if p1[1] == p2[1]:
        return p1[0] - p2[0]
    else:
        return p1[1] - p2[1]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input file>")
        exit()

    paths_map = read_file(sys.argv[1])
    carts = find_carts(paths_map)
    carts = sorted(carts,  key=functools.cmp_to_key(compare_carts))

    paths_map = remove_carts(paths_map)

    while 1:
        carts = move_carts(paths_map, carts)
        carts = sorted(carts, key=functools.cmp_to_key(compare_carts))
