from subprocess import call, DEVNULL
from sys import argv
import re
from time import sleep


def start_timer(length: int, unit: str):
    """
    Basically stops the program by using time.sleep for the specified duration
    :param length: int - the integer part of the specified time
    :param unit: str - the s/m/h part of the specified time
    :return: None
    """
    time = calculate_time(length, unit)
    if time == None:
        raise ValueError("Invalid input...try again!")
    sleep(time)
    timer_end_sound()


def calculate_time(length: int, unit: str) -> int:
    """
    Takes in the amount of time and the unit and converts the time to seconds
    :param length: int - the amount of time
    :param unit: str - the unit of time used
    :return: the desired time in seconds
    """
    if unit == "s" or unit == "S":
        return length
    elif unit == "m" or unit == "M":
        return length * 60
    elif unit == "h" or unit == "H":
        return length * 3600
    else:
        return None


def timer_end_sound():
    """
    Plays the ding sound using ffmpeg's ffplay withe every output setting disabled
    :return: None
    """
    call(["ffplay", "-nodisp", "-autoexit", "ding.mp3"], stdout=DEVNULL, stderr=DEVNULL)


def check_valid_duration(arg: str) -> bool:
    """
    Using a regular expression, checks if the given string is of the desired shape
    :param arg: str - the input argument (the amount of time)
    :return: True if the input is valid, else False
    """
    pattern = "[0-9]+[smhSMH]{1}"
    if re.match(pattern, arg) is not None:
        return True
    return False


def parse_duration(arg: str) -> (int, str):
    """
    Similar to the check function, as it performs a regex match but it returns the relevant fragments
    in a tuple
    :param arg: str - the input duration
    :return: (int, str) first part being the amount of time from the input and the second being the unit used
    """
    pattern = "([0-9]+)([smhSMH]{1})"
    res = re.match(pattern, arg)
    return int(res.group(1)), res.group(2)


if __name__ == "__main__":
    duration = argv[1]  # get the input argument from the command line
    if check_valid_duration(duration):  # if the duration passes the regex match
        amount, scale = parse_duration(duration)  # get the components from the input
        start_timer(amount, scale)  # start the timer and play the 'ding' at the end
