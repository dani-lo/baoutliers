import numpy as np
import statistics

def mad_csv_column(data, ntsd):

    clean_data = np.array(data).astype(np.float)
    data_median = np.median(clean_data)
    absolute_diff = np.absolute(clean_data - data_median)
    mad_value = np.median(absolute_diff)

    mad_rule_threshold = mad_value * ntsd / 0.6745

    outliers_list = [y for y in clean_data if (np.abs(y - data_median) > mad_rule_threshold)]

    if len(outliers_list) > 0:
        return (outliers_list)

    else :
        return []

def mad_json(data, ntsd):

    list_data = [value for [key, value] in data]

    clean_data = np.array(list_data).astype(np.float)
    data_median = np.median(clean_data)
    absolute_diff = np.absolute(clean_data - data_median)
    mad_value = np.median(absolute_diff)

    mad_rule_threshold = mad_value * ntsd / 0.6745

    outliers_list = [[key, value] for [key, value] in data if (np.abs(int(float(value)) - data_median) > mad_rule_threshold)]

    if len(outliers_list) > 0:
        return (outliers_list)

    else :
        return []