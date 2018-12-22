from inputs import challlenge_input, test_input_1, test_input_3, test_input_2
from graph import Graph, dijsktra


def push(obj, l, depth):
    while depth:
        l = l[-1]
        depth -= 1

    l.append(obj)


def parse_parentheses(s):
    groups = [()]
    depth = 0

    try:
        for char in s:
            if char == '(':
                push([[]], groups, depth)
                depth += 2
            elif char == ')':
                depth -= 2
            elif char == "|":
                push([], groups, depth - 1)
            else:
                push(char, groups, depth)
    except IndexError:
        raise Exception('Parentheses mismatch')

    if depth > 0:
        raise Exception('Parentheses mismatch')
    else:
        return groups


start_position = (0, 0)
doors = set()
rooms = set()


def handle_next_position(position, w: str):
    if w == "N":
        new_doors = (position[0], position[1] + 1)
        new_room = (position[0], position[1] + 2)
        doors.add(new_doors)
        rooms.add(new_room)
        return new_room
    elif w == "E":
        new_doors = (position[0] + 1, position[1])
        new_room = (position[0] + 2, position[1])
        doors.add(new_doors)
        rooms.add(new_room)
        return new_room
    if w == "W":
        new_doors = (position[0] - 1, position[1])
        new_room = (position[0] - 2, position[1])
        doors.add(new_doors)
        rooms.add(new_room)
        return new_room
    elif w == "S":
        new_doors = (position[0], position[1] - 1)
        new_room = (position[0], position[1] - 2)
        doors.add(new_doors)
        rooms.add(new_room)
        return new_room


def print_area():
    min_x = min(min([d[0] for d in doors]), min([r[0] for r in rooms])) - 1
    max_x = max(max([d[0] for d in doors]), max([r[0] for r in rooms])) + 1

    min_y = min(min([d[1] for d in doors]), min([r[1] for r in rooms])) - 1
    max_y = max(max([d[1] for d in doors]), max([r[1] for r in rooms])) + 1

    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if (x, y) == (0, 0):
                print("X", end="")
            elif (x, y) in doors:
                print("|", end="")
            elif (x, y) in rooms:
                print(".", end="")
            else:
                print("#", end="")
        print()


def fill_area(parsed, positons):
    while len(parsed) > 0:
        elem = parsed.pop(0)
        if type(elem) is not list:
            for i in range(0, len(positons)):
                positons[i] = handle_next_position(positons[i], elem)
        else:
            sublists = []
            for e in elem:
                sublists.extend(fill_area(e, positons.copy()))

            positons = sublists

    return positons


print("parsing...")
parsed_input = parse_parentheses(challlenge_input)
print("filling area...")
positions = [(0, 0)]
fill_area(parsed_input, positions)
print("crating graph")
g = Graph()

for room in rooms:

    place_north = (room[0], room[1] + 1)
    room_north = (room[0], room[1] + 2)
    place_south = (room[0], room[1] - 1)
    room_south = (room[0], room[1] - 2)
    place_east = (room[0] + 1, room[1])
    room_east = (room[0] + 2, room[1])
    place_west = (room[0] - 1, room[1])
    room_west = (room[0] - 2, room[1])

    if place_north in doors and room_north in rooms:
        g.add_edge(room, room_north, 1)

    if place_south in doors and room_south in rooms:
        g.add_edge(room, room_south, 1)

    if place_east in doors and room_east in rooms:
        g.add_edge(room, room_east, 1)

    if place_west in doors and room_west in rooms:
        g.add_edge(room, room_west, 1)


start_north = (0, 1)
start_east = (1, 0)
start_south = (0, -1)
start_west = (-1, 0)

if start_north in doors:
    g.add_edge((0, 0), (0, 2), 1)

if start_east in doors:
    g.add_edge((0, 0), (2, 0), 1)

if start_south in doors:
    g.add_edge((0, 0), (0, -2), 1)

if start_west in doors:
    g.add_edge((0, 0), (-2, 0), 1)

paths = {}
for room in rooms:
    paths[room] = len(dijsktra(g, (0, 0), room))

print("calculating distance")

m = max(paths, key=paths.get)
print(m, paths[m] - 1)

print_area()

