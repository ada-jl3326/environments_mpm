import numpy as np
from scipy.ndimage import gaussian_filter
from tqdm import tqdm

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'progress_sum']


def rand_array(shape):
    return np.random.rand(*shape)


def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)


def my_mat_solve(A, b):
    return A.inv()*b


def progress_sum(a):
    """Sum all elements of a 1D array, showing a progress bar."""
    total = 0
    for x in tqdm(a): 
        total += x
    return total
