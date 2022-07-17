from ..fit import Fitting
from ..registry import REGISTERED_MODELS
from numpy import linspace
from ..FitModels import Linear, BaseFitModel

import pytest
import matplotlib.pyplot as plt
from os import path, remove


@pytest.fixture()
def x(): return linspace(10, 20, 100)


@pytest.fixture()
def y(x): return Linear.generate_noisy_data(4, x, 5, 11)


@pytest.fixture()
def f(): return Fitting(Linear())


def test_initialising():
    for model in REGISTERED_MODELS:
        f = Fitting(model())
        assert isinstance(f.model, BaseFitModel)
        f_from_string = Fitting(model.__name__)
        assert isinstance(f_from_string.model, BaseFitModel)


def test_fitting(x, y, f):
    assert f.guess is None
    assert f.bounds is None
    assert f.result is None

    f.fit(x, y, plot=False)

    assert f.guess is not None
    assert f.bounds is not None
    assert f.result is not None


@pytest.mark.plotting
def test_plotting(x, y, f):
    plt.ion()
    f.plot(x, y, show=True)
    plt.ioff()


@pytest.mark.plotting
def test_saving_plots(x, y, f):
    f.plot(x, y, show=False, save=False)
    fig_path = f.save_figure(path = path.dirname(path.abspath(__file__)))
    assert path.exists(fig_path)
    remove(fig_path)


