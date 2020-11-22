import matplotlib.pyplot as plt
import numpy as np
import pathlib
import time

def boxplot_plotter_image (metric_data) :
    img_path = pathlib.Path('.').parent.absolute()
    ts = time.time()
    img_location = "{base_path}/static/{uid}.png".format(base_path= img_path, uid = ts)
    img_name = "{uid}.png".format(uid=ts)

    flierprops = dict(markerfacecolor='r', marker='s')
    boxprops = dict(linestyle='-', linewidth=1, color='black')
    medianprops = dict(linestyle='-', linewidth=1, color='firebrick')

    clean_data = np.array(metric_data).astype(np.float)

    fig, ax = plt.subplots(figsize=(15,2))
    ax.boxplot(clean_data, medianprops=medianprops, vert=False, boxprops=boxprops, flierprops=flierprops)
    fig.savefig(img_location, bbox_inches='tight')

    return img_name