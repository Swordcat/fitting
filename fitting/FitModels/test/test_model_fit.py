import pytest

from .. import Linear
from .. import Polynomial
import numpy as np


def check_model_fit(model, noise, x_0, x_1, x_n, *args):
    x = np.linspace(x_0, x_1, x_n)
    y = model.generate_noisy_data(noise, x, *args)
    popt, perr, _ = model.fit(x, y)
    print(model.guess(x,y))
    print(args)

    # passes if difference between fitted and real value of parameter is within two times the 'error' on fitted value
    for i, (opt, err) in enumerate(zip(popt, perr)):
        assert np.abs(args[i]-opt) < err * 4


def test_linear_fit():
    check_model_fit(Linear(), 1, 10, 20, 1000, 5, 11)
    check_model_fit(Linear(), 1, 10, 20, 1000, -5, 11)
    check_model_fit(Linear(), 1, -20, -10, 1000, 0, 11)
    check_model_fit(Linear(), 5, -20, -10, 1000, 0, 11)
    check_model_fit(Linear(), 5, -20, -10, 1000, 4, 11)


def test_polynomial_fit():
    check_model_fit(Polynomial(order=2)(), 1, -10, 20, 1000, 5, 11, 3)
    check_model_fit(Polynomial(order=2)(), 1, 10, 20, 1000, 5, 11, 3)
    check_model_fit(Polynomial(order=2)(), 1, -20, 20, 1000, 1, 2, 3)
    for i in range(2, 7):
        check_model_fit(Polynomial(order=i)(), 1, -20, 20, 1000, *list((np.arange(i+1))+1))
