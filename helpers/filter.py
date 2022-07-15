import scipy.signal
import numpy as np

def filter(data: np.array, length: int=7, bias_sign: int = 1):
    return scipy.signal.savgol_filter(data, length, 2) * bias_sign