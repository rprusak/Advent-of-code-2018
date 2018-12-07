import sys
import re
from typing import List, Tuple, Dict


def read_file(filename):
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    return content


pattern = re.compile("Step (\w) must be finished before step (\w) can begin.")


def parse_input(file_input: List[str]) -> List[Tuple[str, str]]:
    steps = []

    for line in file_input:
        match = pattern.match(line)

        if match:
            steps.append((match[1], match[2]))
        else:
            raise RuntimeError("Could not parse input")

    return steps


def find_start_steps(steps_connections: List[Tuple[str, str]]) -> List[str]:
    start_steps = set([x for t in steps_connections for x in t])

    for step in steps_connections:
        if step[1] in start_steps:
            start_steps.remove(step[1])

    start_steps = list(start_steps)
    start_steps.sort()

    return start_steps


def find_path(start_steps: List[str], steps_connections: List[Tuple[str, str]]):
    done_steps = [start_steps.pop(0)]

    while len(steps_connections) > 0:
        available_steps = find_available_steps(done_steps, steps_connections)
        available_steps.extend(start_steps)
        available_steps.sort()

        new_step = available_steps[0]

        if new_step in start_steps:
            start_steps.remove(new_step)

        done_steps.append(new_step)
        steps_connections = remove_visited_steps(done_steps, steps_connections)

    return ''.join(done_steps)


def find_available_steps(done_steps: List[str], steps: List[Tuple[str, str]]):
    tmp = []

    for step in steps:
        if step[0] in done_steps:
            if not step[1] in done_steps:
                tmp.append(step[1])

    available_steps = set(tmp)
    tmp = set()

    for available_step in available_steps:
        prerequisites = find_prerequisites(available_step, steps)

        if all_prerequisites_have_been_visited(prerequisites, done_steps):
            tmp.add(available_step)

    return list(tmp)


def find_prerequisites(step: str, steps: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    result = []

    for s in steps:
        if s[1] == step:
            result.append(s)
    return result


def all_prerequisites_have_been_visited(prerequisites: List[Tuple[str, str]], done_steps: List[str]) -> bool:
    for prerequisite in prerequisites:
        if not prerequisite[0] in done_steps:
            return False

    return True


def remove_visited_steps(done_steps: List[str], steps_connections: List[Tuple[str, str]]):
    result = []

    for step in steps_connections:
        if not (step[0] in done_steps and step[1] in done_steps):
            result.append(step)

    return result


def calculate_work_time(path: str, steps_connections: List[Tuple[str, str]], workers: int) -> int:
    path = list(path)
    path = [str(p) for p in path]

    start_steps = find_start_steps(steps_connections)

    done_steps = []
    workers_jobs = {}
    for step in start_steps:
        workers_jobs[step] = 0

    start_steps.remove(path[0])

    work_time = 0

    while len(workers_jobs.keys()) > 0:

        # increase work time
        for worker in workers_jobs.keys():
            workers_jobs[worker] += 1

        work_time += 1
        print(work_time, workers_jobs)
        remove_completed_works(done_steps, workers_jobs)

        available_steps = find_available_steps(done_steps, steps_connections)
        available_steps.sort()

        for worker in workers_jobs.keys():
            if worker in available_steps:
                available_steps.remove(worker)

        for available_step in available_steps:
            if len(workers_jobs.keys()) < workers:
                workers_jobs[available_step] = 0
                if available_step in start_steps:
                    start_steps.remove(available_step)
                # if available_step in path:
                #     path.remove(available_step)

    return work_time


def get_step_work_time(step: str):
    return ord(step) - 4


def remove_completed_works(done_steps: List[str], workers_jobs: Dict[str, int]):
    keys_to_remove = []

    for worker in workers_jobs.keys():
        if workers_jobs[worker] == get_step_work_time(worker):
            keys_to_remove.append(worker)
            done_steps.append(worker)

    for k in keys_to_remove:
        del workers_jobs[k]

    return len(keys_to_remove)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: main.py <input file> <workers>")
        exit()

    file_content = read_file(sys.argv[1])
    steps_connections = parse_input(file_content)
    print(steps_connections)
    start_step = find_start_steps(steps_connections)

    path = find_path(start_step, steps_connections)
    print(path)
    print(calculate_work_time(path, steps_connections, int(sys.argv[2])))

