from .base import BaseFitModel
from numpy import array

class Linear(BaseFitModel):
    @classmethod
    def function(cls, x: array, a: float, b: float) -> array:
        return a * x + b

    @classmethod
    def guess(cls, x: array, y: array) -> list[float]:
        slope = (y[-1] - y[0]) / (x[-1] - x[0])
        return [slope, y[0] - slope * x[0]]