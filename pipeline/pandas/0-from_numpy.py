#!/usr/bin/env python3
"""Creates a pandas DataFrame from a numpy ndarray"""

import pandas as pd


def from_numpy(array):
    """Return a DataFrame with alphabetical column labels"""
    cols = array.shape[1]
    labels = [chr(65 + i) for i in range(cols)]
    return pd.DataFrame(array, columns=labels)
