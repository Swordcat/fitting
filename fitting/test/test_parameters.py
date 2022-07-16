from ..FitModels import BaseFitModel, Linear
from ..fitting import Fitting

def test_parameters():
    assert Fitting(BaseFitModel()).parameters() == ['args']
    assert Fitting(Linear()).parameters() == ['a', 'b']