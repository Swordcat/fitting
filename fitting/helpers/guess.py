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
    # gets x value where y value is closest to halfway between background offset and peak height on left side of peak
    fwhm_l = x[:peak_index][argmin(abs(y[:peak_index] - (height / 2 + offset)))]
    # gets x value where y value is closest to halfway between background offset and peak height on right side of peak
    fwhm_r = x[peak_index:][argmin(abs(y[peak_index:] - (height / 2 + offset)))]
    return abs(fwhm_r-fwhm_l)
