from .base import BaseFitModel
from numpy import array, exp, power, inf
from typing import Union
from ..helpers.guess import peak


class Lorentzian(BaseFitModel):
    @classmethod
    def function(cls, x: array, height: float, sigma: float, offset: float, location: float):
        return offset + height * power(sigma, 2) / (power((x - location), 2) + power(sigma, 2))

    @classmethod
    def guess(cls, x: array, y: array):
        height, fwhm, offset, location = peak(x, y)
        # for Lorentzian fwhm ~ 2*sigma or sigma ~ 0.5 * fwhm
        return height, 0.5 * fwhm, offset, location

    @classmethod
    def bounds(cls, x: array, y: array, guess: list[float] = None) -> Union[tuple[float, float], tuple[list[float], list[float]]]:
        return [-inf, 0, -inf, -inf], [inf, inf, inf, inf]
