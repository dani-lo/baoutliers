def upload_file_to_s3(file, bucket_name, s3client):
    try:
        s3client.upload_fileobj(
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
        print('------------------------------------')
        print(file_list)
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