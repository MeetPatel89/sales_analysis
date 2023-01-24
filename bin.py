import pandas as pd
import numpy as np

def get_bins(df, col, n):
    max_val = df[col].max()
    min_val = df[col].min()
    bin_size = (max_val - min_val) / n
    bounds = (1, min_val, min_val + bin_size)
    bins = [bounds]
    for i in np.arange(n - 1):
        bounds = (bounds[0] + 1, bounds[2], bounds[2] + bin_size)
        bins.append(bounds)
    df = pd.DataFrame(np.array(bins, dtype=[("bin_num", "i4"), ("lower_bound", "f8"),("upper_bound", "f8")]))
    return df.round({"lower_bound": 2, "upper_bound": 2})
    
