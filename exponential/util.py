from __future__ import division
import matplotlib.pyplot as plt
import math

def calc_rmse(y, yh, n):
    err = 0.0
    for i in range(n):
        delta = yh[i] - y[i]
        delta = delta * delta
        err += delta
    
    rmse = math.sqrt(err/n)
    return rmse

def plot_figs(data, title):
    if len(data) < 1:
        print("Error: empty data for plot.")
        return
    
    for pair in data:
        legend, y = pair
        plt.plot(y, label=legend)
    plt.legend()
    plt.title(title)
    plt.grid(True)
    plt.show()
    return


def float_str(alist):
    result = "["
    for i in alist:
        result += "%.2f, " % (i)
    result += "]"
    return result


def load_series(fname):
    fhd = open(fname, 'r')
    line = fhd.readline()
    print("header:" + line)
    result = []
    for line in fhd:
        items = line.strip().split(",")
        result.append(float(items[1]))

    fhd.close()
    return result