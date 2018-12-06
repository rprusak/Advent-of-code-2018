import sys
import re
from typing import List, Dict, Tuple

def read_file(filename):
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    return content


class Point:
    points_count = 0

    def __init__(self, x: int, y: int) -> None:
        Point.points_count += 1
        self.x = x
        self.y = y
        self.point_id = Point.points_count

    def __str__(self) -> str:
        return str(self.point_id) + " : (" + str(self.x) + ", " + str(self.y) + ")"

    def coordinates(self) -> Tuple[int, int]:
        return self.x, self.y

    def distance(self, x, y):
        return abs(self.x - x) + abs(self.y - y)


point_patter = re.compile("(\d+),\s+(\d+)")


def parse_input(file_input: List[str]) -> List[Point]:
    points = []

    for line in file_input:
        match = point_patter.match(line)

        if match:
            x = int(match[1])
            y = int(match[2])
            points.append(Point(x, y))
        else:
            raise RuntimeError("Could not parse input")

    return points


def get_arena_size(points: List[Point]) -> int:
    width = max(point.x for point in points)
    height = max(point.y for point in points)
    return max(width, height) + 1


def create_area(size: int) -> Dict[Tuple[int, int], str]:
    area = {}

    for i in range(0, size):
        for j in range(0, size):
            area[(i, j)] = "x"

    return area


def display_area(area: Dict[Tuple[int, int], str], size: int):
    for j in range(size - 1, -1, -1):
        for i in range(0, size):
            print("%3s" % area[(i, j)], end="")
        print()


def mark_points(area: Dict[Tuple[int, int], str], points: List[Point]):

    for p in points:
        area[p.coordinates()] = str(p.point_id)


def mark_closes_points(area: Dict[Tuple[int, int], str], points: List[Point]):
    input_points_coordinates = [p.coordinates() for p in points]

    for area_point in area.keys():
        if not area_point in input_points_coordinates:
            area[area_point] = get_clothes_point_mark(area_point, points)


def calculate_distances_to_other_points(source_point: Tuple[int, int], points: List[Point]) -> Dict[int, int]:
    d = {}
    for destination_point in points:
        d[destination_point.point_id] = destination_point.distance(source_point[0], source_point[1])

    return d


def get_clothes_point_mark(source_point: Tuple[int, int], points: List[Point]) -> str:
    distances = calculate_distances_to_other_points(source_point, points)
    clothes_point = min(distances, key=distances.get)
    clothes_distance = distances[clothes_point]

    if list(distances.values()).count(clothes_distance) > 1:
        return "."
    else:
        return str(clothes_point)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input file>")
        exit()

    file_content = read_file(sys.argv[1])
    input_points = parse_input(file_content)

    area_size = get_arena_size(input_points)
    area = create_area(area_size)
    mark_points(area, input_points)
    mark_closes_points(area, input_points)

    # display_area(area, area_size)

    area_values = set(area.values())
    area_values.remove(".")

    for i in range(0, area_size):
        if area[(i, 0)] in area_values:
            area_values.remove(area[(i, 0)])

        if area[(0, i)] in area_values:
            area_values.remove(area[(0, i)])

        if area[(area_size - i - 1, area_size - 1)] in area_values:
            area_values.remove(area[(area_size - i - 1, area_size - 1)])

        if area[(area_size - 1, area_size - i - 1)] in area_values:
            area_values.remove(area[(area_size - 1, area_size - i - 1)])

    values_stats = {}
    for v in area_values:
        values_stats[v] = list(area.values()).count(v)

    print(values_stats[max(values_stats, key=values_stats.get)])
