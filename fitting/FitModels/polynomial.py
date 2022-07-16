from .base import BaseFitModel
from numpy import array
from numpy.polynomial.polynomial import Polynomial as poly


def Polynomial(order: int = 2):
    class Polynomial(BaseFitModel):
        order = None

        def __init__(self, name: str = None):
            super().__init__(name)
            self.set_order(order)

        @classmethod
        def function(cls, x: array, *args) -> array:
            return poly(args)(x)

        @classmethod
        def guess(cls, x: array, y: array) -> list[float]:
            return list(poly.fit(x, y, cls.order).convert().coef)

        @classmethod
        def parameters(cls) -> list[str]: return [f'a_{i}' for i in range(cls.order+1)]

        @classmethod
        def set_order(cls, order: int): cls.order = order

    return Polynomial
