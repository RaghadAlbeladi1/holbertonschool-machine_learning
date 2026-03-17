#!/usr/bin/env python3
"""Load data from a file as a pandas DataFrame"""

import pandas as pd


def from_file(filename, delimiter):
    """Return DataFrame loaded from file"""
    return pd.read_csv(filename, sep=delimiter)
