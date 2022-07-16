import numpy as np
from .filter import smooth


def peak(x: np.array, y: np.array) -> list[float]:
    x, y = filter(x), filter(y)
    offset = (y[0] + y[-1]) / 2
    bias = 1 if np.abs(np.min(y) - offset) < np.abs(np.max(y) - offset) else -1
    y = y * bias
    peak_indx = np.argmax(y)
    height = y[peak_indx]*bias - offset
    return [height, fwhm(x, y, peak_indx, np.abs(offset), np.abs(height)), offset, x[peak_indx]]


def fwhm(x: np.array, y: np.array, peak_index: int, offset: float, height: float) -> float:
    try: fwhm_l = x[:peak_index][y[:peak_index] < offset + height / 2][-1]
    except IndexError: fwhm_l = x[0]
    try: fwhm_h = x[peak_index:][y[peak_index:] < offset + height / 2][0]
    except IndexError: fwhm_h = x[-1]
    return fwhm_h+fwhm_l
