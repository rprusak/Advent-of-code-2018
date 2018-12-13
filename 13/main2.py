import sys
import functools
from typing import List
from cart import Cart
from main import read_file, find_carts, compare_carts, remove_carts


def move_carts(paths_map: List[str], carts: List[Cart]) -> List[Cart]:
    tmp: List[Cart] = []

    for i in range(0, len(carts)):
        cart = carts[i]
        if cart.crashed:
            continue

        cart.move()
        x, y = cart.get_position()

        for c in tmp:
            if c.crashed:
                continue

            if c.get_position() == cart.get_position():
                print("Collision at ", c.get_position())
                c.crashed = True
                cart.crashed = True

        for c in carts[i+1:]:
            if c.crashed:
                continue
            if c.get_position() == cart.get_position():
                print("Collision at ", c.get_position())
                c.crashed = True
                cart.crashed = True

        if cart.crashed:
            continue

        cart.on_next_field(paths_map[y][x])
        tmp.append(cart)

        tmp = [x for x in tmp if not x.crashed]

    return tmp


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input file>")
        exit()

    paths_map = read_file(sys.argv[1])
    carts = find_carts(paths_map)
    carts = sorted(carts, key=functools.cmp_to_key(compare_carts))

    paths_map = remove_carts(paths_map)

    while len(carts) > 1:
        for c in carts:
            print(c.get_position(), end=" ")

        print()

        carts = move_carts(paths_map, carts)
        carts = sorted(carts, key=functools.cmp_to_key(compare_carts))

    print(carts[0].get_position())
