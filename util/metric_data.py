from outliers.testrun.util.load_file_data import read_csv_column

def get_metric_data (csv_name, metric_name) :

    csv_data = read_csv_column(csv_name, metric_name)

    return csv_data