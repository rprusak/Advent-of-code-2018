from datetime import datetime
from typing import Tuple, List, Dict
import re
import sys
import functools

pattern = re.compile("\[(\d+)-(\d+)-(\d+)\s+(\d+):(\d+)\]\s+(.+)")
guard_begin_shift_pattern = re.compile("Guard #(\d+) begins shift")


def parse_event(event: str) -> Tuple[datetime, str]:
    match = pattern.match(event)

    if match:
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        hour = int(match.group(4))
        minute = int(match.group(5))
        event_action = match.group(6)
        event_datetime = datetime(year, month, day, hour, minute)
        return event_datetime, event_action
    else:
        raise RuntimeError("Could not parse event " + event)


def read_file(filename):
    content = []

    with open(filename) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    return content


def compare_entries(first_entry, second_entry):
    if first_entry[0] < second_entry[0]:
        return -1
    elif second_entry[0] > first_entry[0]:
        return 1
    else:
        return 0


def get_guards_sleep_periods(log_entries: List[Tuple[datetime, str]]) -> Dict[int, List[Tuple[int, int]]]:
    guards_slip_periods = {}

    quard_id = 0
    asleep_time = 0

    for entry in log_entries:
        event_test = entry[1]

        if guard_begin_shift_pattern.match(event_test):
            quard_id = guard_begin_shift_pattern.match(event_test)[1]
        elif event_test == "falls asleep":
            asleep_time = entry[0].minute
        elif event_test == "wakes up":
            wake_up_time = entry[0].minute

            if quard_id in guards_slip_periods.keys():
                guards_slip_periods[quard_id].append((asleep_time, wake_up_time))
            else:
                guards_slip_periods[quard_id] = []
                guards_slip_periods[quard_id].append((asleep_time, wake_up_time))
        else:
            raise RuntimeError("invalid event text")

    return guards_slip_periods


def get_guards_total_sleep_time(guards_sleep_periods: Dict[int, List[Tuple[int, int]]]) -> Dict[int, int]:
    result = {}

    for guard in guards_sleep_periods.keys():
        result[guard] = 0
        sleep_periods = guards_sleep_periods[guard]
        for sleep_period in sleep_periods:
            result[guard] += sleep_period[1] - sleep_period[0]

    return result


def get_best_minute(sleep_periods: List[Tuple[int, int]]) -> Tuple[int, int]:
    minutes_stats = {}

    for period in sleep_periods:
        for minute in range(period[0], period[1]):
            if minute in minutes_stats:
                minutes_stats[minute] += 1
            else:
                minutes_stats[minute] = 1

    best_minute = int(max(minutes_stats, key=minutes_stats.get))
    best_minute_count = int(minutes_stats[best_minute])

    return best_minute, best_minute_count


def get_guard_with_most_minutes_asleep_and_best_minute(text_entries: List[str]) -> Tuple[int, int]:
    log_entries = [parse_event(event) for event in text_entries]
    log_entries.sort(key=functools.cmp_to_key(compare_entries))

    guards_sleep_periods = get_guards_sleep_periods(log_entries)
    guards_total_sleep_time = get_guards_total_sleep_time(guards_sleep_periods)

    # find top sleeping guard
    top_guard = max(guards_total_sleep_time, key=guards_total_sleep_time.get)
    best_minute, _ = get_best_minute(guards_sleep_periods[top_guard])

    return int(top_guard), best_minute


def get_guards_most_popular_sleep_minute(guards_sleep_periods: Dict[int, List[Tuple[int, int]]]) -> Dict[int, Tuple[int, int]]:
    result = {}

    for guard in guards_sleep_periods:
        result[guard] = get_best_minute(guards_sleep_periods[guard])

    return result


def get_minute_count(minute_stat: Tuple[int, int]) -> int:
    return minute_stat[1]


def get_guard_most_frequently_asleep_on_the_same_minute(text_entries: List[str]) -> Tuple[int, int]:
    log_entries = [parse_event(event) for event in text_entries]
    log_entries.sort(key=functools.cmp_to_key(compare_entries))

    guards_sleep_periods = get_guards_sleep_periods(log_entries)
    guards_most_popular_sleep_minutes = get_guards_most_popular_sleep_minute(guards_sleep_periods)

    guard_most_often_asleep = max(guards_most_popular_sleep_minutes, key=lambda k: guards_most_popular_sleep_minutes[k][1])

    return int(guard_most_often_asleep), guards_most_popular_sleep_minutes[guard_most_often_asleep][0]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <input file>")
        exit()

    content = read_file(sys.argv[1])
    guard_id, best_minute = get_guard_with_most_minutes_asleep_and_best_minute(content)

    print("guard id: ", guard_id)
    print("best minute: ", best_minute)
    print(guard_id * best_minute)
    guard_most_often_asleep, his_best_minute = get_guard_most_frequently_asleep_on_the_same_minute(content)
    print("guard_most_often_asleep: ", guard_most_often_asleep)
    print("his_best_minute: ", his_best_minute)
    print(guard_most_often_asleep * his_best_minute)