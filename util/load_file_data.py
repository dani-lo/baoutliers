import csv
import json

def read_csv_column(fname, metric_name):

    with open(fname,'rt')as f:
        data = csv.reader(f)

        headers = next(data)
        metric_idx = headers.index(metric_name)

        csv_col = []

        for row in data:
            csv_col.append(row[metric_idx])

        return csv_col

def read_json_file(fname, metric_name, label_name):

    with open(fname) as f:
        data = json.load(f)

    nested_data = []

    for row in data:
        nested_data.append([row[label_name], row[metric_name]])

    return nested_data

