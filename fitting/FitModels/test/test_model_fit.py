from .. import Fermi
from .. import Gaussian
from .. import Linear
from .. import Lorentzian
from .. import Polynomial
import numpy as np


def check_model_fit(model, noise, x_0, x_1, x_n, *args):
    x = np.linspace(x_0, x_1, x_n)
    y = model.generate_noisy_data(noise, x, *args)
    guess = model.guess(x, y)
    bounds = model.bounds(x, y, guess)
    popt, perr, _ = model.fit(x, y, guess=guess, bounds=bounds)

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


def test_fermi_fit():
    check_model_fit(Fermi(), 0.2, -20, 20, 1000, 0.8, 2, 0.1, 5)
    check_model_fit(Fermi(), 0.2, -20, 20, 1000, -0.8, 2, 0.1, -5)
    check_model_fit(Fermi(), 0.2, -20, 20, 1000, -0.8, 2, 10, -5)
    check_model_fit(Fermi(), 0.3, -20, 20, 1000, -0.8, 2, 10, -5)
    check_model_fit(Fermi(), 3, -20, 20, 1000, 10, 4, 10, -5)


def test_gaussian_fit():
    check_model_fit(Gaussian(), 0.2, -20, 20, 1000, 0.8, 2, 0.1, 5)
    check_model_fit(Gaussian(), 0.2, -20, 20, 1000, -0.8, 2, 0.1, -5)
    check_model_fit(Gaussian(), 0.2, -20, 20, 1000, -0.8, 2, 10, -5)
    check_model_fit(Gaussian(), 0.3, -20, 20, 1000, -0.8, 2, 10, -5)
    check_model_fit(Gaussian(), 3, -20, 20, 1000, 10, 4, 10, -5)

def test_lorentzian_fit():
    check_model_fit(Lorentzian(), 0.2, -20, 20, 1000, 0.8, 2, 0.1, 5)
    check_model_fit(Lorentzian(), 0.2, -20, 20, 1000, -0.8, 2, 0.1, -5)
    check_model_fit(Lorentzian(), 0.2, -20, 20, 1000, -0.8, 2, 10, -5)
    check_model_fit(Lorentzian(), 0.3, -20, 20, 1000, -0.8, 2, 10, -5)
    check_model_fit(Lorentzian(), 3, -20, 20, 1000, 10, 4, 10, -5)
