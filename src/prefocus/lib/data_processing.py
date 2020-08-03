import csv
from datetime import datetime

import pandas as pd


def write_csv(fields, rows, filename):
    with open(filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        # writing the fields
        csvwriter.writerow(fields)
        # writing the data rows
        csvwriter.writerows(rows)


def dry(csv_path):
    """converts a CSV file into a two dimensional array.
    :param csv_path: path to the CSV file.
    :return: a two dimension array
    """
    return pd.read_csv(csv_path).values.tolist()


def format_day_or_month(target):
    if not isinstance(target, str):
        target = str(int(target))
    if len(target) == 2:
        return target
    else:
        try:
            assert len(target) == 1
            return "0{}".format(target)
        except AssertionError:
            return "--"


def now():
    got = datetime.now()
    return "{dd}{mm}{yyyy}".format(
        dd=format_day_or_month(got.day),
        mm=format_day_or_month(got.month),
        yyyy=str(got.year),
    )
