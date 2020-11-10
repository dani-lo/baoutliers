import numpy as np

def three_sigma_csv_column(data, n_std):

    clean_data = np.array(data).astype(np.float)
    data_mean = np.mean(clean_data)
    threshold = np.std(clean_data) * n_std

    outliers_list = [y for y in clean_data if (np.abs(y - data_mean) > threshold)]

    if len(outliers_list) > 0:
        return (outliers_list)
    else :
        return []

def three_sigma_json(data, n_std):

    list_data = [value for [key, value] in data]

    clean_data = np.array(list_data).astype(np.float)
    data_mean = np.mean(clean_data)
    threshold = np.std(clean_data) * n_std

    outliers_list = [[key, value] for [key, value] in data if (np.abs( int(float(value)) - data_mean) > threshold)]

    if len(outliers_list) > 0:

        return (outliers_list)
    else :
        return []