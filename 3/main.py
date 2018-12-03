import re
import sys
from typing import List, Tuple

rectangle_pattern = re.compile("#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)")


class Rectangle:
    def __init__(self, rec_id, x, y, width, height):
        self.rec_id = rec_id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return "#" + str(self.rec_id) + ": (" + str(self.x) + "," + str(self.y) + ") " + str(self.width) + "x" + str(self.height)

    def get_points(self) -> List[Tuple[int, int]]:
        result = []

        for i in range(0, self.width):
            for j in range(0, self.height):
                result.append((self.x + i, self.y + j))

        return result


def create_rectangle(description: str) -> Rectangle:
    match = rectangle_pattern.search(description)

    if match:
        rec_id = int(match.group(1))
        x = int(match.group(2))
        y = int(match.group(3))
        width = int(match.group(4))
        height = int(match.group(5))

        return Rectangle(rec_id, x, y, width, height)
    else:
        raise RuntimeError("Could not parse description " + description)


def get_rectangles(descriptions: List[str]) -> List[Rectangle]:
    result = []

    for desc in descriptions:
        result.append(create_rectangle(desc))

    return result


def get_common_area(rectangles: List[str]) -> int:
    rectangles_list = get_rectangles(rectangles)

    area = {}

    for rectangle in rectangles_list:
        points = rectangle.get_points()
        for point in points:
            if point in area.keys():
                area[point].append(rectangle.rec_id)
            else:
                area[point] = []
                area[point].append(rectangle.rec_id)

    common_fields_count = 0
    for field in area.values():
        if len(field) >= 2:
            common_fields_count += 1

    return common_fields_count


def get_intact_area_id(rectangles: List[str]) -> int:
    rectangles_list = get_rectangles(rectangles)

    area = {}
    all_rectangles = set()
    overlap_rectangles = set()

    for rectangle in rectangles_list:
        all_rectangles.add(rectangle.rec_id)

        points = rectangle.get_points()
        for point in points:
            if point in area.keys():
                area[point].append(rectangle.rec_id)
                for i in area[point]:
                    overlap_rectangles.add(i)
            else:
                area[point] = []
                area[point].append(rectangle.rec_id)

    return list(all_rectangles.difference(overlap_rectangles))[0]


def read_file(filename):
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    return content


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input file>")
        exit()

    try:
        file_content = read_file(sys.argv[1])
        print(len(file_content))
        print(get_common_area(file_content))
        print(get_intact_area_id(file_content))
    except RuntimeError as e:
        print(e.args)