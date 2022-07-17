from .base import BasePeakFit
from numpy import array, exp, power, inf
from typing import Union


class Gaussian(BasePeakFit):
    @classmethod
    def function(cls, x: array, height: float, sigma: float, offset: float, location: float):
        return offset + height * exp(-power((x - location), 2) / (2 * power(sigma, 2)))

    @classmethod
    def guess(cls, x: array, y: array):
        height, fwhm, offset, location = super().guess(x, y)
        # for Gaussian fwhm ~ 2.355*sigma or sigma ~ 0.43 * fwhm
        return height, 0.43 * fwhm, offset, location
