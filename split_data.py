from cgi import test
import sys
import pandas as pd
import math
from random import sample
import csv


def read_csv_file(filename):
    line_count = 0
    full_data_list = []
    with open(filename, "r") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        for row in csv_reader:
            line_count += 1
            full_data_list.append(row)
    return line_count, full_data_list


def write_to_file(data_list, is_training_set, percentage):
    filename = ""
    if is_training_set:
        filename = "training_dataset_" + str(percentage) + ".csv"
        print("Training dataset filename: " + filename)
    else:
        filename = "test_dataset_" + str(percentage) + ".csv"
        print("Test dataset filename: " + filename)
    with open(filename, mode="w") as training_file:
        training_writer = csv.writer(
            training_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        for row in data_list:
            training_writer.writerow(row)


def split_data(full_data_list, percentage, rows):
    list_indices = [x for x in range(1, rows - 1)]
    split_samples = math.floor(rows * percentage)
    test_set_indices = sample(list_indices, split_samples)
    training_set_list = []
    test_set_list = []
    training_set_list.append(full_data_list[0])
    test_set_list.append(full_data_list[0])
    for idx in range(1, len(full_data_list)):
        row_index = int(full_data_list[idx][0])
        if row_index in test_set_indices:
            test_set_list.append(full_data_list[idx])
        else:
            training_set_list.append(full_data_list[idx])
    write_to_file(training_set_list, True, percentage)
    print(
        str((1 - percentage) * 100)
        + "% training data containing "
        + str(len(training_set_list) - 1)
        + " samples"
    )
    write_to_file(test_set_list, False, percentage)
    print(
        str((percentage) * 100)
        + "% test data containing "
        + str(len(test_set_list) - 1)
        + " samples"
    )


if __name__ == "__main__":
    filename = './data/cleaned_data.csv'
    # percentage = float(sys.argv[2])
    rows, full_data_list = read_csv_file(filename)
    split_data(full_data_list, 0.25, rows)
