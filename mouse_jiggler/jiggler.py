import time
import pytz
import datetime
import random
import pyautogui
import threading
from .args_ import validate_args


def is_within_working_hours(start_hour, end_hour, timezone):
    tz = pytz.timezone(timezone)
    now = datetime.datetime.now(tz)
    start_time = now.replace(hour=start_hour, minute=0, second=0, microsecond=0)
    end_time = now.replace(hour=end_hour, minute=0, second=0, microsecond=0)
    return start_time <= now <= end_time


def time_until_start_of_working_hours(start_hour, timezone):
    tz = pytz.timezone(timezone)
    now = datetime.datetime.now(tz)
    start_time = now.replace(hour=start_hour, minute=0, second=0, microsecond=0)
    if now < start_time:
        return (start_time - now).total_seconds()
    else:
        next_start_time = start_time + datetime.timedelta(days=1)
        return (next_start_time - now).total_seconds()


def generate_realistic_target(screen_width, screen_height):
    zones = [
        ("center", 0.4, 0.6, 0.4, 0.6),
        ("top_left", 0.0, 0.2, 0.0, 0.2),
        ("top_right", 0.8, 1.0, 0.0, 0.2),
        ("bottom_left", 0.0, 0.2, 0.8, 1.0),
        ("bottom_right", 0.8, 1.0, 0.8, 1.0),
        ("left_edge", 0.0, 0.1, 0.0, 1.0),
        ("right_edge", 0.9, 1.0, 0.0, 1.0),
        ("top_edge", 0.0, 1.0, 0.0, 0.1),
        ("bottom_edge", 0.0, 1.0, 0.9, 1.0),
    ]

    zone = random.choice(zones)
    zone_name, x_min, x_max, y_min, y_max = zone

    target_x = random.randint(int(screen_width * x_min), int(screen_width * x_max) - 1)
    target_y = random.randint(
        int(screen_height * y_min), int(screen_height * y_max) - 1
    )

    return target_x, target_y


def move_cursor_randomly(
    screen_width,
    screen_height,
    min_delay,
    max_delay,
    min_steps,
    max_steps,
    standby_time,
    move_chance,
    interrupt_chance,
    timzezone,
    start_hour,
    end_hour,
):

    while True:
        # if not is_within_working_hours(start_hour, end_hour, timzezone):
        #     sleep_duration = time_until_start_of_working_hours(start_hour, timzezone)
        #     print(f"Outside working hours, sleeping for {sleep_duration} seconds.")
        #     time.sleep(sleep_duration)
        #     continue

        delay = random.randint(min_delay, max_delay)
        chance = random.randint(0, 100)
        if chance < move_chance:
            print(f"Sleeping for {delay} seconds")
            time.sleep(delay)
        print("Moving cursor randomly")

        current_x, current_y = pyautogui.position()
        target_x, target_y = generate_realistic_target(screen_width, screen_height)

        move_steps = random.randint(min_steps, max_steps)

        step_x = (target_x - current_x) / move_steps
        step_y = (target_y - current_y) / move_steps

        for i in range(move_steps):
            current_mouse_x, current_mouse_y = pyautogui.position()

            if (current_mouse_x - current_x) ** 2 + (
                current_mouse_y - current_y
            ) ** 2 > 2:
                print("User moved the mouse, relinquishing control.")
                time.sleep(standby_time)
                break

            trajector_check = random.randint(0, 100)
            if trajector_check < interrupt_chance:
                print("Randomly moving cursor to a different location.")
                break

            current_x += step_x
            current_y += step_y

            pyautogui.moveTo(current_x, current_y, duration=0.01)

            time.sleep(0.01)


def main():

    screen_width, screen_height = pyautogui.size()
    args = validate_args()

    if args is None:
        return

    thread = threading.Thread(
        target=move_cursor_randomly,
        args=(
            screen_width,
            screen_height,
            args.min_delay,
            args.max_delay,
            args.min_steps,
            args.max_steps,
            args.standby_time,
            args.move_chance,
            args.interrupt_chance,
            args.timezone,
            args.start_hour,
            args.end_hour,
        ),
    )
    thread.daemon = True
    thread.start()

    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("Program terminated by user")


if __name__ == "__main__":
    main()
