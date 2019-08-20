from subprocess import call, DEVNULL
from sys import argv
import re
from time import sleep


def start_timer(length: int, unit: str):
    time = calculate_time(length, unit)
    sleep(time)
    timer_end_sound()


def calculate_time(length: int, unit: str) -> int:
    if unit == "s" or unit == "S":
        return length
    elif unit == "m" or unit == "M":
        return length * 60
    elif unit == "h" or unit == "H":
        return length * 3600
    else:
        raise ValueError("Invalid input!")

def timer_end_sound():
    call(["ffplay", "-nodisp", "-autoexit", "ding.mp3"], stdout=DEVNULL, stderr=DEVNULL)


def check_valid_duration(arg: str) -> bool:
    pattern = "[0-9]+[smhSMH]{1}"
    if re.match(pattern, arg) is not None:
        return True
    return False


def parse_duration(arg: str) -> (int, str):
    pattern = "([0-9]+)([smhSMH]{1})"
    res = re.match(pattern, arg)
    return int(res.group(1)), res.group(2)

if __name__ == "__main__":
    duration = argv[1]
    if check_valid_duration(duration):
        amount, scale = parse_duration(duration)
        start_timer(amount, scale)
