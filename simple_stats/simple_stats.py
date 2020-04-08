"""Main module."""
import numpy as np


def ecdf(data):
    """Compute Empirical Cumulative Distribution Function (ECDF) for a one-dimensional array of measurements.
    :return Two 1D arrays for plotting the ECDF
    """

    # Check that the passed in parameter is a 1D array
    if not isinstance(data, np.ndarray):
        raise TypeError('The passed in parameter must be a 1D numpy array or DataFrame series.')

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n

    return x, y
