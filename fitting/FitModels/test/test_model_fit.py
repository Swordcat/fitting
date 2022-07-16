import pytest

from .. import Linear
import numpy as np


def check_model_fit(model, noise, x_0, x_1, x_n, *args):
    x = np.linspace(x_0, x_1, x_n)
    y = model.generate_noisy_data(noise, x, *args)
    popt, perr, _ = model.fit(x, y)

    # passes if difference between fitted and real value of parameter is within two times the 'error' on fitted value
    for i, (opt, err) in enumerate(zip(popt, perr)):
        assert np.abs(args[i]-opt) < err * 3


def test_linear_fit():
    check_model_fit(Linear(), 1, 10, 20, 1000, 5, 11)
    check_model_fit(Linear(), 1, 10, 20, 1000, -5, 11)
    check_model_fit(Linear(), 1, -20, -10, 1000, 0, 11)
    check_model_fit(Linear(), 5, -20, -10, 1000, 0, 11)
    check_model_fit(Linear(), 5, -20, -10, 1000, 4, 11)