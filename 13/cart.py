from __future__ import annotations
import enum


class Direction(enum.Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    @staticmethod
    def string_to_direction(val: str) -> 'Direction':
        if val == "^":
            return Direction.UP
        elif val == "v":
            return Direction.DOWN
        elif val == "<":
            return Direction.LEFT
        elif val == ">":
            return Direction.RIGHT
        else:
            raise RuntimeError("Received invalid direction string " + val)

    def __str__(self):
        if self == Direction.UP:
            return "^"
        elif self == Direction.DOWN:
            return "v"
        elif self == Direction.LEFT:
            return "<"
        else:
            return ">"


class Turn(enum.Enum):
    UNKNOWN = 1
    LEFT = 2
    STRAIGHT = 3
    RIGHT = 4

    @staticmethod
    def get_next_turn(t : 'Turn') -> 'Turn':
        if t == Turn.UNKNOWN:
            return t.LEFT
        elif t == Turn.LEFT:
            return Turn.STRAIGHT
        elif t == Turn.STRAIGHT:
            return Turn.RIGHT
        elif t == Turn.RIGHT:
            return Turn.LEFT

    @staticmethod
    def get_next_direction(t: 'Turn', d: 'Direction'):
        if t == Turn.STRAIGHT:
            return d
        elif t == Turn.LEFT:
            if d == Direction.LEFT:
                return Direction.DOWN
            elif d == Direction.UP:
                return Direction.LEFT
            elif d == Direction.RIGHT:
                return Direction.UP
            elif d == Direction.DOWN:
                return Direction.RIGHT
        elif t == Turn.RIGHT:
            if d == Direction.LEFT:
                return Direction.UP
            elif d == Direction.UP:
                return Direction.RIGHT
            elif d == Direction.RIGHT:
                return Direction.DOWN
            elif d == Direction.DOWN:
                return Direction.LEFT


class Cart:
    def __init__(self, x: int, y: int, direction: str) -> None:
        self.x = x
        self.y = y
        self.direction = Direction.string_to_direction(direction)
        self.turn = Turn.UNKNOWN
        self.crashed = False

    def __str__(self) -> str:
        return str(self.direction)

    def get_position(self):
        return self.x, self.y

    def move(self):
        if self.direction == Direction.UP:
            self.y -= 1
        elif self.direction == Direction.DOWN:
            self.y += 1
        elif self.direction == Direction.LEFT:
            self.x -= 1
        elif self.direction == Direction.RIGHT:
            self.x += 1

    def on_next_field(self, next_field):
        if next_field in "|-":
            pass
        elif next_field in "/\\":
            self.__turn_on_edge(next_field)
        elif next_field == "+":
            self.turn = Turn.get_next_turn(self.turn)
            self.direction = Turn.get_next_direction(self.turn, self.direction)

    def __turn_on_edge(self, edge: str):
        if edge == "\\":
            if self.direction == Direction.RIGHT:
                self.direction = Direction.DOWN
            elif self.direction == Direction.LEFT:
                self.direction = Direction.UP
            elif self.direction == Direction.UP:
                self.direction = Direction.LEFT
            elif self.direction == Direction.DOWN:
                self.direction = Direction.RIGHT
        else: # /
            if self.direction == Direction.RIGHT:
                self.direction = Direction.UP
            elif self.direction == Direction.LEFT:
                self.direction = Direction.DOWN
            elif self.direction == Direction.UP:
                self.direction = Direction.RIGHT
            elif self.direction == Direction.DOWN:
                self.direction = Direction.LEFT