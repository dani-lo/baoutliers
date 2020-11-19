import csv
import json
import codecs

def upload_file_to_s3(file, bucket_name, s3_client):
    try:
        s3_client.upload_fileobj(
            file,
            bucket_name,
            file.filename
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e


def list_files_from_s3(bucket_name, s3_client):

    try:
        file_list = s3_client.list_objects(Bucket=bucket_name)

        return file_list

    except Exception as e:
        print("Something Happened: ", e)
        return e

def get_s3_file (key, data_path, bucket_name, s3_client) :
    local_file = data_path + key

    try:
        s3_client.download_file(Bucket=bucket_name, Key = key, Filename = local_file)
    except Exception as e:
        print("Something Happened: ", e)
        return e

def read_s3_csv_column (key, bucket_name, s3_client, metric_name) :

    try:
        data = s3_client.get_object(Bucket=bucket_name, Key = key)

        csv_col = []

        for row in csv.DictReader(codecs.getreader("utf-8")(data["Body"])):
            csv_col.append((row[metric_name]))

        return csv_col

    except Exception as e:
        print("Something Happened: ", e)
        return e

def read_s3_json_column (key, bucket_name, s3_client, metric_name, label_name) :

    try:
        data = s3_client.get_object(Bucket=bucket_name, Key = key)
        file_content = data['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)

        csv_col = []

        for row in json_content:
            csv_col.append([row[label_name], row[metric_name]])

        return csv_col

    except Exception as e:
        print("Something Happened: ", e)
        return e