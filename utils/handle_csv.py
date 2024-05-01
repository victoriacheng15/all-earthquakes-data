import csv, os
from utils.settings import filename, header


def setup_csv():
    if not os.path.isfile(filename):
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()


def get_existing_csv_codes():
    codes = set()
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            codes.add(row["code"])
    return set(codes)


def append_data_to_csv(data):
    with open(filename, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writerow(data)


def get_all_csv_data():
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        return tuple([row for row in reader])
