#!/usr/bin/env python3
"""Module that concatenates two DataFrames with keys
and indexed on Timestamp."""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """Concatenate df2 rows up to timestamp 1417411920 above df1.

    Args:
        df1: pandas DataFrame (coinbase)
        df2: pandas DataFrame (bitstamp)

    Returns:
        pandas.DataFrame: concatenated DataFrame with keys
    """
    df1 = index(df1)
    df2 = index(df2)
    df2 = df2.loc[:1417411920]
    df_concat = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
    return df_concat
