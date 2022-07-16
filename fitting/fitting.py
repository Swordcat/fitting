
from numpy import array
from inspect import signature
from typing import Union

from .FitModels import BaseFitModel
from .helpers.dataclasses import factory, Parameter
from .registry import model_registry

class Fitting:
    def __init__(self, model: Union[BaseFitModel, str],
                 guess:list[float] = None,
                 bounds: Union[tuple[float, float], tuple[list[float], list[float]]] = None):
        self.model = model if isinstance(model, BaseFitModel) else model_registry.get(model)
        self.guess = guess
        self.bounds = bounds
        self.result = None

    def fit(self, x: array, y: array, plot: bool=False):
        self.guess = self.guess if self.guess else self.model.guess(x, y)
        self.bounds = self.bounds if self.bounds else self.model.bounds(x, y)
        popt, perr, pcov = self.model.fit(x, y, self.guess, self.bounds)
        self.result = self.dataclass(popt, perr)
        if plot: self.plot()
        return popt, perr, pcov

    def parameters(self) -> list[str]:
        return list(signature(self.model.function).parameters.keys())[1:]

    def dataclass(self, popt: list[float], perr: list[float]):
        assert len(popt) == len(perr), f"{self.model.__name__}.dataclass: length of 'popt' ({len(popt)}) and 'perr' ({len(perr)}) must match"
        dc = factory(self.model.__name__, self.parameters() if len(self.parameters()) == len(popt) else [f"args[{i}" for i in enumerate(popt)])
        return dc(*[Parameter(i, j) for i, j in zip(popt, perr)])

    def plot(self):
        ...