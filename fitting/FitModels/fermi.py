from .base import BaseFitModel
from numpy import array, exp, min, max, argmin, abs, inf
from typing import Union
from ..helpers.filter import smooth


class Fermi(BaseFitModel):
    @classmethod
    def function(cls, x: array, height: float, sigma: float, offset: float, step: float):
        return offset + height * 1 / (1 + exp((x - step) / sigma))

    @classmethod
    def guess(cls, x: array, y: array):
        x, y = smooth(x), smooth(y)
        offset = min(y)
        height = max(y) - offset
        step = x[argmin(abs(y - (height / 2 + offset)))]  # gets x value closest to y value halfway between min(y) and max(y)
        sigma = abs(x[argmin(abs(y - (height / 4 + offset)))] - step)  # gets x value distance between y values closest to half and quarter way between min(y) and max(y)
        return height, sigma, offset, step

    @classmethod
    def bounds(cls, x: array, y: array, guess: list[float] = None) -> Union[tuple[float, float], tuple[list[float], list[float]]]:
        return [-inf, 0, -inf, -inf], [inf, inf, inf, inf]
