import numpy as np

def main(data, y):
    averages = np.mean(data,axis=0)
    mean_square = np.mean(data**2, axis=0)
    return averages, mean_square