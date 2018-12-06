import sys
from typing import Dict, List, Tuple
from main import Point
from main import read_file, parse_input, get_arena_size, create_area, display_area


def mark_points_with_desired_total_distance(area: Dict[Tuple[int, int], str], points: List[Point], distance):
    for area_point in area.keys():
        point_distance = get_total_distance_to_points(area_point, points)
        if point_distance < distance:
            area[area_point] = "#"


def get_total_distance_to_points(p: Tuple[int, int], points: List[Point]):
    distance = 0

    for destination_point in points:
        distance += destination_point.distance(p[0], p[1])

    return distance


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: main.py <input file> <distance>")
        exit()

    file_content = read_file(sys.argv[1])
    input_points = parse_input(file_content)

    area_size = get_arena_size(input_points)
    area = create_area(area_size)
    mark_points_with_desired_total_distance(area, input_points, int(sys.argv[2]))
    # display_area(area, area_size)

    print(list(area.values()).count("#"))
