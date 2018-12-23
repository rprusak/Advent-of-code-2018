import sys
from typing import List, Tuple, Dict


def read_file(filename: str) -> List[str]:
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.rstrip() for x in content]
    result = [list(x) for x in content]
    return content


def get_area(file_content: List[str]) -> Tuple[int, int, Dict[Tuple[int, int], str]]:
    height = len(file_content)
    width = len(file_content[0])
    area = dict()

    for y in range(0, height):
        for x in range(0, width):
            area[(x, y)] = file_content[y][x]

    return width, height, area


def display_area(area: Dict[Tuple[int, int], str], width: int, height: int):
    for y in range(0, height):
        for x in range(0, width):
            print(area[(x, y)], end="")
        print()


def get_new_point(area: Dict[Tuple[int, int], str], x: int, y: int) -> str:
    acre = area[(x, y)]
    adjacent_fields = [(x, y - 1), (x, y + 1), (x - 1, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1),
                       (x - 1, y), (x + 1, y)]

    if acre == ".":
        trees = 0
        for field in adjacent_fields:
            if field in area.keys() and area[field] == "|":
                trees += 1

        if trees >= 3:
            return "|"
        else:
            return "."
    elif acre == "|":
        lumberyards = 0
        for field in adjacent_fields:
            if field in area.keys() and area[field] == "#":
                lumberyards += 1

        if lumberyards >= 3:
            return "#"
        else:
            return "|"
    elif acre == "#":
        lumberyards = 0
        trees = 0

        for field in adjacent_fields:
            if field in area.keys():
                if area[field] == "#":
                    lumberyards += 1
                elif area[field] == "|":
                    trees += 1

        if lumberyards >= 1 and trees >= 1:
            return "#"
        else:
            return "."
    else:
        raise RuntimeError("Invalid acre value")


def are_area_equal(first_area, second_area):
    result = True

    for k in first_area:
        if second_area[k] != first_area[k]:
            result = False
            break

    return result


def get_area_result(area):
    lumberyards = 0
    trees = 0
    for acre in area.values():
        if acre == "#":
            lumberyards += 1
        elif acre == "|":
            trees += 1

    return lumberyards * trees


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input file>")
        exit()

    file_input = read_file(sys.argv[1])
    width, height, area = get_area(file_input)
    areas = []

    for i in range(0, 1000):
        new_area = {}

        for x in range(0, width):
            for y in range(0, height):
                new_area[(x, y)] = get_new_point(area, x, y)

        for j in range(0, len(areas)):
            if are_area_equal(new_area, areas[j]):
                print("equal found", j, i)
                break

        area = new_area
        areas.append(area)

        if i == 915:
            print(get_area_result(area))
            exit()




