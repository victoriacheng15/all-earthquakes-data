import logging
from sys import argv
from utils.actions import csv_action, db_action

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(action):
    if action == "csv":
        csv_action()
    elif action == "db":
        db_action()
    else:
        logger.error(f" Unknown {action}, please enter 'csv' or 'db'")
        exit(1)


if __name__ == "__main__":
    if len(argv) < 2:
        logger.error("Usage: python3 main.py <csv|db>")
        exit(1)

    action = argv[1]

    main(action)
