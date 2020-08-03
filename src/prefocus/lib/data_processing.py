import csv

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
