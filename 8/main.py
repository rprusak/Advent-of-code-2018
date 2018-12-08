import sys
from typing import List


def read_file(filename):
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    return content


def calculate_metadata(data_list: List[int]) -> int:
    return sum(read_node(1, data_list))


def read_node(nodes_count: int, data_list: List[int]) -> List[int]:
    metadata = []

    if nodes_count == 1:
        child_nodes_count = data_list.pop(0)
        meta_data_nodes_count = data_list.pop(0)

        if child_nodes_count > 0:
            child_metadata = read_node(child_nodes_count, data_list)
            metadata.extend(child_metadata)

        for i in range(0, meta_data_nodes_count):
            metadata.append(data_list.pop(0))
    else:
        for i in range(0, nodes_count):
            metadata.extend(read_node(1, data_list))

    return metadata


def calculate_node_value(data_list: List[int]):

    child_nodes_count = data_list.pop(0)
    meta_data_nodes_count = data_list.pop(0)

    if child_nodes_count == 0:
        value = 0
        for i in range(0, meta_data_nodes_count):
            value += data_list.pop(0)

        return value
    else:
        child_nodes_values = []
        metadata_nodes = []
        value = 0

        for i in range(0, child_nodes_count):
            child_nodes_values.append(calculate_node_value(data_list))

        for i in range(0, meta_data_nodes_count):
            metadata_nodes.append(data_list.pop(0))

        for metadata in metadata_nodes:
            if metadata != 0 and metadata <= len(child_nodes_values):
                value += child_nodes_values[metadata - 1]

        return value


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input file>")
        exit()

    file_content = read_file(sys.argv[1])
    program_input = [int(x) for x in file_content[0].split(" ")]

    print(calculate_metadata(program_input))

    file_content = read_file(sys.argv[1])
    program_input = [int(x) for x in file_content[0].split(" ")]
    print(calculate_node_value(program_input))
