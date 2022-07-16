from .. import BaseFitModel, Linear
def test_parameters():
    assert BaseFitModel.parameters() == ['args']
    assert Linear().parameters() == ['a', 'b']