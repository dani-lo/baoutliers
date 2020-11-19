import csv
import json
import codecs


# def read_csv_metric(s3_client, filename, metricname):
#     data = s3_client.get_object(Bucket=, Key=key)
#
#     for row in csv.DictReader(codecs.getreader("utf-8")(data["Body"])):
#         print(row[column])

def read_csv_column(fname, metric_name):


    with open(fname,'rt')as f:
        print('============================== read_csv_column(fname, metric_name)', fname, metric_name)
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

