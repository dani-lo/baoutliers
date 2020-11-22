import numpy as np

def boxplot_csv_column (data, iqr_multi = 1.5) :
    clean_data = np.array(data).astype(np.float)

    q1 = np.percentile(clean_data, 25)
    q3 = np.percentile(clean_data, 75)

    iqr = q3 - q1

    outliers_list = [y for y in clean_data if ((y > q3 + float(iqr_multi) * iqr) or (y < q1 - float(iqr_multi) * iqr))]

    if len(outliers_list) > 0:
        return (outliers_list)

    else :
        return []

def boxplot_json(data, iqr_multi = 1.5):

    list_data = [value for [key, value] in data]
    clean_data = np.array(list_data).astype(np.float)

    q1 = np.percentile(clean_data, 25)
    q3 = np.percentile(clean_data, 75)

    iqr = q3 - q1

    outliers_list = [[key, val] for [key, val] in data if ((float(val) > q3 + float(iqr_multi) * iqr) or (float(val) < q1 - float(iqr_multi) * iqr))]

    if len(outliers_list) > 0:
        return (outliers_list)
    else:
        return []
