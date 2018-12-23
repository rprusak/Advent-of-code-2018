import sys
import re
from random import randint
from typing import List, Tuple
from collections import defaultdict


def read_file(filename: str) -> List[str]:
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.rstrip() for x in content]
    result = [list(x) for x in content]
    return content


nanobot_pattern = re.compile("pos=<(-?\d+),(-?\d+),(-?\d+)>,\sr=(\d+)")


def parse_nanobot_description(desc: str) -> Tuple[Tuple[int, int, int], int]:
    match = nanobot_pattern.match(desc)
    if match:
        return (int(match[1]), int(match[2]), int(match[3])), int(match[4])
    else:
        raise RuntimeError("Could not parse nanobot description " + desc)


def calculate_distance(first_point: Tuple[int, int, int], second_point: Tuple[int, int, int]) -> int:
    distance = 0

    for i in range(0, 3):
        distance += abs(first_point[i] - second_point[i])

    return distance


def calculate_close_nanobots_count(nanobots, point):
    result = 0

    for nanobot in nanobots:
        if calculate_distance(point, nanobot[0]) <= nanobot[1]:
            result += 1

    return result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input file>")
        exit()

    file_input = read_file(sys.argv[1])
    nanobots = list(map(parse_nanobot_description, file_input))
    biggest_radius_nanobot = max(nanobots, key=lambda n: n[1])
    biggest_radius = biggest_radius_nanobot[1]

    nanobots_in_range_count = 0
    for nanobot in nanobots:
        if calculate_distance(biggest_radius_nanobot[0], nanobot[0]) <= biggest_radius:
            nanobots_in_range_count += 1

    print("Part 1:", nanobots_in_range_count)

    # x_min = min(nanobots, key=lambda n: n[0][0])[0][0]
    # x_max = max(nanobots, key=lambda n: n[0][0])[0][0]
    # y_min = min(nanobots, key=lambda n: n[0][1])[0][1]
    # y_max = max(nanobots, key=lambda n: n[0][1])[0][1]
    # z_min = min(nanobots, key=lambda n: n[0][2])[0][2]
    # z_max = max(nanobots, key=lambda n: n[0][2])[0][2]

    # x_min = 57642828 - 30000000
    # x_max = 57642828 + 10000000
    # y_min = 48078828 - 30000000
    # y_max = 48078828 + 10000000
    # z_min = 38802400 - 30000000
    # z_max = 38802400 + 10000000

    x_min = 59110500 - 100
    x_max = 59110500 + 100
    y_min = 46561200 - 100
    y_max = 46561200 + 100
    z_min = 36801700 - 100
    z_max = 36801700 + 100

    step = 1

    points = defaultdict(int)

    for x in range(x_min, x_max, step):
        for y in range(y_min, y_max, step):
            for z in range(z_min, z_max, step):
                points[(x, y, z)] = calculate_close_nanobots_count(nanobots, (x, y, z))

    sorted_points = sorted(points.items(), key=lambda kv: kv[1])
    for p in sorted_points:
        print(p)
