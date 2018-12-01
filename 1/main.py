# Advent of Code 2018 day 1
import sys


def read_frequency_changes(filename):
    with open(filename) as f:
        content = f.readlines()

    content = [int(x.strip()) for x in content]
    return content


def calculate_frequency(frequency_changes):
    frequency = 0

    for f in frequency_changes:
        frequency += f

    return frequency


def get_duplicated_frequency(frequency_changes):
    encountered_frequencies = set()
    frequency = 0

    encountered_frequencies.add(frequency)

    while 1:
        for f in frequency_changes:
            frequency += f
            if frequency in encountered_frequencies:
                return frequency
            else:
                encountered_frequencies.add(frequency)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input filename>")
        exit()

    frequency_changes = read_frequency_changes(sys.argv[1])
    frequency = calculate_frequency(frequency_changes)
    duplicated_frequency = get_duplicated_frequency(frequency_changes)

    print("Frequency: %d", frequency)
    print("First duplicated frequency %d", duplicated_frequency)
