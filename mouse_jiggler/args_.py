import argparse
import pytz

parser = argparse.ArgumentParser(
    prog="Jiggler",
    description="A script to move the cursor randomly to prevent idle detection.",
)

parser.add_argument(
    "--min-delay",
    type=int,
    default=0,
    help="Minimum delay between cursor movements, in seconds (default: 5).",
)
parser.add_argument(
    "--max-delay",
    type=int,
    default=60,
    help="Maximum delay between cursor movements, in seconds (default: 60).",
)
parser.add_argument(
    "--min-steps",
    type=int,
    default=100,
    help="Minimum number of steps for each cursor movement (default: 100).",
)
parser.add_argument(
    "--max-steps",
    type=int,
    default=200,
    help="Maximum number of steps for each cursor movement (default: 200).",
)
parser.add_argument(
    "--standby-time",
    "-s",
    type=int,
    default=5,
    help="Standby time after user moves the mouse, in seconds (default: 300).",
)
parser.add_argument(
    "--move-chance",
    "-m",
    type=int,
    default=50,
    help="Chance (in percentage) to move the cursor after a delay (default: 50%%).",
)
parser.add_argument(
    "--interrupt-chance",
    "-i",
    type=int,
    default=10,
    help="Chance (in percentage) to interrupt the cursor movement and choose a new target (default: 10%%).",
)
parser.add_argument(
    "--wait-time",
    "-w",
    type=int,
    default=60,
    help="Time to wait after user moves the mouse, in seconds (default: 60).",
)
parser.add_argument(
    "--timezone",
    "-tz",
    type=str,
    default="America/Chicago",
    help="Timezone for working hours (default: America/Chicago).",
)
parser.add_argument(
    "--start-hour",
    "-sh",
    type=int,
    default=9,
    help="Start of working hours (default: 9 AM).",
)
parser.add_argument(
    "--end-hour",
    "-eh",
    type=int,
    default=17,
    help="End of working hours (default: 5 PM).",
)


def validate_args():

    args = parser.parse_args()

    if args.min_steps > args.max_steps:
        print("Minimum steps cannot be greater than maximum steps.")
        return
    if args.min_delay > args.max_delay:
        print("Minimum delay cannot be greater than maximum delay.")
        return
    if args.start_hour >= args.end_hour:
        print("Start hour cannot be greater than or equal to end hour.")
        return
    if args.move_chance < 0 or args.move_chance > 100:
        print("Move chance must be between 0 and 100.")
        return
    if args.interrupt_chance < 0 or args.interrupt_chance > 100:
        print("Interrupt chance must be between 0 and 100.")
        return
    if args.standby_time < 0:
        print("Standby time cannot be negative.")
        return
    if args.wait_time < 0:
        print("Wait time cannot be negative.")
        return

    if args.timezone not in pytz.all_timezones:
        print("Invalid timezone.")
        return

    if args.start_hour < 0 or args.start_hour > 23:
        print("Start hour must be between 0 and 23.")
        return

    if args.end_hour < 0 or args.end_hour > 23:
        print("End hour must be between 0 and 23.")
        return

    return args
