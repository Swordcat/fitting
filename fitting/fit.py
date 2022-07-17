from numpy import array
from os import getcwd
from typing import Union
import matplotlib.pyplot as plt
from json import dump

from .FitModels import BaseFitModel
from .helpers.dataclass import Parameter
from .registry import model_registry


class Fitting:
    def __init__(self, model: Union[BaseFitModel, str],
                 guess: list[float] = None,
                 bounds: Union[tuple[float, float], tuple[list[float], list[float]]] = None):
        self.model = model if isinstance(model, BaseFitModel) else model_registry.get(model)()
        self.guess = guess
        self.bounds = bounds
        self.result = None

    def fit(self, x: array, y: array, plot: bool = False):
        self._guess(x, y), self._bounds(x, y)
        popt, perr, pcov = self.model.fit(x, y, self.guess, self.bounds)
        self.result = self.model.dataclass()(*[Parameter(i, j) for i, j in zip(popt, perr)])
        if plot: self.plot(x, y, show=False)
        return popt, perr, pcov

    def plot(self, x: array, y: array, close_old: bool = True, show: bool = True, save: bool = False):
        self._guess(x, y)
        if close_old: plt.close(self.model.name)
        plt.figure(self.model.name)
        plt.plot(x, y, label='data')
        if self.result is not None: plt.plot(x, self.model.function(x, *self.result.values()), label=f'Fit:\n{self.result.to_text(".3e")}')
        plt.plot(x, self.model.function(x, *self.guess), 'C3', label='guess')
        plt.legend()
        if save: self.save_figure()
        if show: plt.show()

    def save_figure(self, xlabel: str = None, ylabel: str = None, title: str = None, path: str = '', name: str = '') -> str:
        plt.figure(self.model.name)
        if xlabel: plt.xlabel(xlabel)
        if ylabel: plt.ylabel(ylabel)
        if title: plt.title(title)
        plt.tight_layout()
        file_path = f"{self._filepath(path, name)}.png"
        plt.savefig(file_path, dpi=150)
        return file_path

    def save_result(self, path: str = '', name: str = ''):
        dump({'model': self.model.name, "result": self.result.to_dict()},
             open(f'{self._filepath(path, name)}.json', 'w'), indent=4)

    def _guess(self, x: array, y: array):
        self.guess = self.guess if self.guess else self.model.guess(x, y)

    def _bounds(self, x: array, y: array):
        self.bounds = self.bounds if self.bounds else self.model.bounds(x, y)

    def _filepath(self, path: str, name: str) -> str:
        return f"{path if path else getcwd()}/{name if name else self.model.name}"
