from numpy import abs, argmax, argmin, array, max, min
from .filter import smooth


def peak(x: array, y: array) -> list[float]:
    x, y = smooth(x), smooth(y)
    offset = (y[0] + y[-1]) / 2
    bias = 1 if abs(min(y) - offset) < abs(max(y) - offset) else -1
    y = y * bias
    peak_indx = argmax(y)
    height = y[peak_indx]*bias - offset
    return [height, fwhm(x, y, peak_indx, abs(offset), abs(height)), offset, x[peak_indx]]


def fwhm(x: array, y: array, peak_index: int, offset: float, height: float) -> float:
    return abs(whm_l(x, y, peak_index, offset, height) + whm_r(x, y, peak_index, offset, height))


def whm_l(x: array, y: array, peak_index: int, offset: float, height: float) -> float:
    # gets x value where y value is closest to halfway between background offset and peak height on left side of peak
    return x[peak_index] - x[:peak_index][argmin(abs(y[:peak_index] - (height / 2 + offset)))]


def whm_r(x: array, y: array, peak_index: int, offset: float, height: float) -> float:
    # gets x value where y value is closest to halfway between background offset and peak height on right side of peak
    return x[peak_index:][argmin(abs(y[peak_index:] - (height / 2 + offset)))] - x[peak_index]
