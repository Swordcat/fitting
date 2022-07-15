import numpy as np
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Union, Callable
from scipy.optimize import curve_fit

class BaseFitModel():
    def __call__(self, x: np.array, *args: list[float]):
        return self.function(x, *args)

    @classmethod
    def function(cls, x: np.array, *args: list[float]) -> np.array:
        raise NotImplementedError("Each FitModel should implement its own function")

    @classmethod
    def guess(cls, x: np.array, y: np.array) -> list[float]:
        raise NotImplementedError("Each FitModel should implement its own guess")

    @classmethod
    def bounds(cls, x: np.array, y: np.array, guess: list[float] = None) -> Union[tuple[float, float], tuple[list[float], list[float]]]:
        '''
        returns upper and lower bounds on the parameters of the function to be fit.
        Defaults to no bounds (-inf to inf)
        '''
        return -np.inf, np.inf

    @classmethod
    def fit(cls, x: np.array, y: np.array, guess=None, bounds=None):
        # some fit models may want to use _log_fit instead of _fit
        return cls._fit(x, y, guess=guess, bounds=bounds)

    @classmethod
    def _fit(cls, x: np.array, y: np.array, guess=None, bounds=None):
        popt, pcov = curve_fit(cls.function, x, y,
                               p0=guess if guess else cls.guess(x, y),
                               bounds=bounds if bounds else cls.bounds(x, y))
        return popt, np.sqrt(np.diag(pcov)), pcov

    @classmethod
    def generate_noisy_data(cls, noise: float, x: np.array, *args: list[float]) -> np.array:
        return noise * np.random.randn(x.size) + cls.function(x, *args)
