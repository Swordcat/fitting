from .base import BaseFitModel
from numpy import array, exp, sin, pi, power, inf
from typing import Union
from ..helpers.guess import oscillation


class Oscillation(BaseFitModel):
    @classmethod
    def function(cls, x: array, amplitude: float, frequency: float, phase: float, offset: float):
        return offset + amplitude * sin(2*pi*frequency * x + phase)

    @classmethod
    def guess(cls, x: array, y: array):
        return oscillation(x, y)[:-1]

    @classmethod
    def bounds(cls, x: array, y: array, guess: list[float] = None) -> Union[tuple[float, float], tuple[list[float], list[float]]]:
        return [0, -inf, 0, -inf], [inf, inf, 2*pi, inf]


class SinExpDecay(BaseFitModel):
    @classmethod
    def function(cls, x: array, amplitude: float, frequency: float, phase: float, offset: float, decay_time: float):
        return offset + amplitude * sin(2*pi*frequency * x + phase) * exp(-x/decay_time)

    @classmethod
    def guess(cls, x: array, y: array):
        return oscillation(x, y)

    @classmethod
    def bounds(cls, x: array, y: array, guess: list[float] = None) -> Union[tuple[float, float], tuple[list[float], list[float]]]:
        return [0, -inf, 0, -inf, 0], [inf, inf, 2*pi, inf, inf]


class SinGaussDecay(SinExpDecay):
    @classmethod
    def function(cls, x: array, amplitude: float, frequency: float, phase: float, offset: float, decay_time: float):
        return offset + amplitude * sin(2*pi*frequency * x + phase) * exp(-power(x/decay_time, 2))

    @classmethod
    def guess(cls, x: array, y: array):
        guess = oscillation(x, y)
        # at some point I calculated that this value should be multiplied by 1.67. It seems to work
        guess[-1] *= 1.67
        return guess
