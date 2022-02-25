import numpy as np

def main(data, y):
    #Given data and the y column, computes ratio of mean of y column divided by x columns
    averages = np.mean(data, axis=0)
    return averages[y-1]/np.concatenate((averages[0:y-1], averages[y:len(averages)]))
