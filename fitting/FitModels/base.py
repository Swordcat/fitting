from numpy import array, inf, sqrt, diag, random
from typing import Union
from scipy.optimize import curve_fit
from inspect import signature
from ..helpers import dataclass


class BaseFitModel:
    def __init__(self, name:str = None):
        self.name = name if name else self._classname()

    def __call__(self, x: array, *args):
        return self.function(x, *args)

    @classmethod
    def function(cls, x: array, *args) -> array:
        raise NotImplementedError("Each FitModel should implement its own function")

    @classmethod
    def guess(cls, x: array, y: array) -> list[float]:
        raise NotImplementedError("Each FitModel should implement its own guess")

    @classmethod
    def bounds(cls, x: array, y: array, guess: list[float] = None) -> Union[tuple[float, float], tuple[list[float], list[float]]]:
        '''
        returns upper and lower bounds on the parameters of the function to be fit.
        Defaults to no bounds (-inf to inf)
        '''
        return -inf, inf

    @classmethod
    def fit(cls, x: array, y: array, guess=None, bounds=None):
        # some fit models may want to use _log_fit instead of _fit
        return cls._fit(x, y, guess=guess, bounds=bounds)

    @classmethod
    def _fit(cls, x: array, y: array, guess=None, bounds=None):
        popt, pcov = curve_fit(cls.function, x, y,
                               p0=guess if guess else cls.guess(x, y),
                               bounds=bounds if bounds else cls.bounds(x, y))
        return popt, sqrt(diag(pcov)), pcov

    @classmethod
    def generate_noisy_data(cls, noise: float, x: array, *args) -> array:
        return noise * random.randn(x.size) + cls.function(x, *args)

    @classmethod
    def parameters(cls) -> list[str]: return list(signature(cls.function).parameters.keys())[1:]  # todo explain

    def dataclass(self): return dataclass.factory(self.name, self.parameters())

    @classmethod
    def _classname(cls): return cls.__name__
