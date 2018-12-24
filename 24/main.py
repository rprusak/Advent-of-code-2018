import sys
from typing import List, Tuple
from units_group_parser import UnitsGroupParser
from units_group import UnitsGroup
from simulator import ImmuneSystemSimulator


def read_file(filename: str) -> List[str]:
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.rstrip() for x in content]
    result = [list(x) for x in content]
    return content


def get_units_groups(file_content: List[str]) -> Tuple[List[UnitsGroup], List[UnitsGroup]]:
    immune_system_units = []
    infection_units = []
    parser = UnitsGroupParser()

    # remove "Immune System" header
    file_content = file_content[1:]

    infection_index = file_content.index("Infection:")
    i = 0

    for line in file_content[0:infection_index]:
        i += 1
        group = parser.get_group(line)
        group.id = i
        immune_system_units.append(group)

    i = 0
    for line in file_content[infection_index + 1:]:
        i += 1
        group = parser.get_group(line)
        group.id = i
        group.is_infection = True
        infection_units.append(group)

    return immune_system_units, infection_units


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input file>")
        exit()

    file_content = read_file(sys.argv[1])
    file_content = list(filter(lambda l: len(l) > 0, file_content))

    immune_system_units, infection_units = get_units_groups(file_content)

    # for unit in immune_system_units:
    #     print(unit)
    #
    # for unit in infection_units:
    #     print(unit)

    simulator = ImmuneSystemSimulator(immune_system_units, infection_units)
    simulator.set_boost(38)
    result = simulator.run()

    if result:
        print("Infection won")
        winning_side = simulator.infection
    else:
        print("Immune system won")
        winning_side = simulator.immune_system

    r = 0

    for u in winning_side:
        r += u.units_count

    print(r)
