from .base import BasePeakFit
from numpy import array, power, tanh
from ..helpers.guess import peak


class InvCoshSq(BasePeakFit):
    '''
    Functional form of a coulomb peak
    '''
    @classmethod
    def function(cls, x: array, height: float, sigma: float, offset: float, location: float):
        # 1/cosh()**2 = (1 - tanh()**2)
        return offset + height * (1 - power(tanh((x - location) / sigma), 2))

    @classmethod
    def guess(cls, x: array, y: array):
        height, fwhm, offset, location = super().guess(x, y)
        # for InvCoshSq fwhm ~ 2*sigma or sigma ~ 0.5 * fwhm
        return height, 0.568 * fwhm, offset, location