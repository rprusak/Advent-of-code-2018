import re
from typing import Tuple


class Point:
    point_pattern = re.compile("position=<([-\s]?\d+),\s+([-\s]?\d+)>\s+velocity=<([-\s]?\d+),\s([-\s]?\d+)>")

    def __init__(self, description: str) -> None:
        match = Point.point_pattern.match(description)

        if match:
            self.x = int(match[1])
            self.y = int(match[2])
            self.x_velocity = int(match[3])
            self.y_velocity = int(match[4])
        else:
            raise RuntimeError("Could not parse point description " + description)

    def get_coordinates(self) -> Tuple[int, int]:
        return self.x, self.y

    def get_velocity(self) -> Tuple[int, int]:
        return self.x_velocity, self.y_velocity

    def move(self, times : int = 1):
        self.x = self.x + times * self.x_velocity
        self.y = self.y + times * self.y_velocity
