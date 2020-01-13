import pandas as pd
import numpy as np
from numpy import cumsum
import matplotlib.pyplot as plt

if __name__ == '__main__':
    gallery_size = 40
    df_matching = pd.read_csv('soccer-dataset/matching.csv')
    x = np.arange(0, gallery_size, 1)
    y = df_matching['query_id_position'].value_counts().sort_index().to_numpy()[1:]
    y = cumsum(y)/sum(y)
    plt.figure()
    plt.plot(x, y)
    plt.title("CDF for positions")  # title
    plt.xlabel('Position')  # X axis label
    plt.ylabel('Probability')  # Y axis label
    plt.savefig('soccer-dataset/cdf.png')

