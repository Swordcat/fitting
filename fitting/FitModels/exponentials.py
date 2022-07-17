from .base import BaseFitModel
from numpy import abs, argmin, array, exp, max, min
from ..helpers.filter import smooth


class Exponential(BaseFitModel):
    @classmethod
    def function(cls, x: array, amplitude: float, exponent: float, offset: float):
        return offset + amplitude * exp(-x * exponent)

    @classmethod
    def guess(cls, x: array, y: array):
        x, y = smooth(x), smooth(y)
        offset = min(y)
        amplitude = max(y) - offset
        exponent = x[argmin(abs(y - offset - amplitude / 2.7))]  # e~2.7
        return amplitude, exponent, offset