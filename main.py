import scipy.stats as stats
import numpy as np
import statsmodels.stats.multicomp as multi
import pandas as pd
import matplotlib.pyplot as plt


def example_summary_stats():
    # list your data directly
    data1 = [93, 98, 133, 128, 95, 98, 131, 118, 108, 122]
    data2 = [107, 342, 328, 118, 477, 270, 283, 176, 399, 97]
    data3 = [167, 199, 261, 135, 113, 246, 159, 225, 157, 229]
    # Put data into dataframe
    df = pd.DataFrame()
    df['Chrome'] = data1
    df['Explorer'] = data2
    df['Firefox'] = data3

    print(df.mean())

    print(df.std())


example_summary_stats()


