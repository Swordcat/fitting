from .base import BaseFitModel
import numpy as np


class Linear(BaseFitModel):
    @classmethod
    def function(cls, x: np.array, a: float, b: float) -> np.array:
        return a * x + b

    @classmethod
    def guess(cls, x: np.array, y: np.array) -> list[float]:
        slope = (y[-1] - y[0]) / (x[-1] - x[0])
        return [slope, y[0] - slope * x[0]]