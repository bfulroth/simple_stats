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


def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat

    # Check it the two arguments are np arrays
    if not isinstance(np.ndarray, x):
        raise TypeError("x passed in argument must be a 1d numpy array.")

    if not isinstance(np.ndarray, y):
        raise TypeError("y passed in argument must be a 1d numpy array.")

    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1]
    return corr_mat[0,1]


