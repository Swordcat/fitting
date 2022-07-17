from .base import BasePeakFit
from numpy import array, power
from ..helpers.guess import peak


class Lorentzian(BasePeakFit):
    @classmethod
    def function(cls, x: array, height: float, sigma: float, offset: float, location: float):
        return offset + height * power(sigma, 2) / (power((x - location), 2) + power(sigma, 2))

    @classmethod
    def guess(cls, x: array, y: array):
        height, fwhm, offset, location = super().guess(x, y)
        # for Lorentzian fwhm ~ 2*sigma or sigma ~ 0.5 * fwhm
        return height, 0.5 * fwhm, offset, location
