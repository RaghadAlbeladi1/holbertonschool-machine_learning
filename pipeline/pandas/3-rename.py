#!/usr/bin/env python3
"""Rename Timestamp column and convert to datetime"""

import pandas as pd


def rename(df):
    """Rename Timestamp to Datetime and keep Datetime and Close"""

    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")
    df = df[["Datetime", "Close"]]

    return df
