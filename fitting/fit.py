from numpy import array
from typing import Union
import matplotlib.pyplot as plt

from .FitModels import BaseFitModel
from .helpers.dataclass import Parameter
from .registry import model_registry


class Fitting:
    def __init__(self, model: Union[BaseFitModel, str],
                 guess: list[float] = None,
                 bounds: Union[tuple[float, float], tuple[list[float], list[float]]] = None):
        self.model = model if isinstance(model, BaseFitModel) else model_registry.get(model)
        self.guess = guess
        self.bounds = bounds
        self.result = None

    def fit(self, x: array, y: array, plot: bool = False):
        self._guess(x, y), self._bounds(x, y)
        popt, perr, pcov = self.model.fit(x, y, self.guess, self.bounds)
        self.result = self.model.dataclass()(*[Parameter(i, j) for i, j in zip(popt, perr)])
        if plot: self.plot(x, y)
        return popt, perr, pcov

    def plot(self, x: array, y: array):
        self._guess(x, y)
        plt.figure()
        plt.plot(x, y, label='data')
        if self.result is not None: plt.plot(x, self.model.function(x, *self.result.values()), label=f'Fit:\n{self.result.to_text(".3e")}')
        plt.plot(x, self.model.function(x, *self.guess), label='guess')
        plt.legend()

    def _guess(self, x: array, y: array):
        self.guess = self.guess if self.guess else self.model.guess(x, y)

    def _bounds(self, x: array, y: array):
        self.bounds = self.bounds if self.bounds else self.model.bounds(x, y)
