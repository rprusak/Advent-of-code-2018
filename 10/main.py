import sys
from point import Point
from typing import List
from plot import plot
from math import sqrt


def read_file(filename):
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    return content


def parse_file_content(content: List[str]) -> List[Point]:
    points = []

    for line in content:
        points.append(Point(line))

    return points


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: main <input> <start image> <end image>")
        exit()

    start_index = int(sys.argv[2])
    end_index = int(sys.argv[3])

    file_content = read_file(sys.argv[1])
    points = parse_file_content(file_content)

    for p in points:
        p.move(start_index)

    distances = []
    for i in range(start_index, end_index):
        for p in points:
            p.move()

        points_coordinates = [point.get_coordinates() for point in points]
        first_point = points_coordinates[0]
        distance = [sqrt((coordinates[0] - first_point[0]) ** 2 + (coordinates[1] - first_point[1]) ** 2) for coordinates in points_coordinates[1:]]
        distances.append(sum(distance))

    min_distance = min(distances)
    min_distance_index = distances.index(min_distance) + start_index
    print(distances.index(min_distance) + start_index, min_distance)

    points = parse_file_content(file_content)

    for p in points:
        p.move(min_distance_index - 200)

    for i in range(min_distance_index - 200, min_distance_index + 200):
        for p in points:
            p.move()

        points_coordinates = [point.get_coordinates() for point in points]
        axis_coordinates = list(map(list, zip(*points_coordinates)))
        plot(axis_coordinates[0], axis_coordinates[1])