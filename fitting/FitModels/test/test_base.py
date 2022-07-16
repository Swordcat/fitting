from .. import BaseFitModel, Linear, Polynomial


def test_name():
    model = BaseFitModel()
    assert model.name == 'BaseFitModel'

    model = BaseFitModel(name='name_test')
    assert model.name == 'name_test'

    model = Linear()
    assert model.name == 'Linear'

    model = Polynomial()()
    assert model.name == 'Polynomial'


def test_parameters():
    assert BaseFitModel.parameters() == ['args']
    assert Linear().parameters() == ['a', 'b']
    assert Polynomial(order=4)().parameters() == ['a_0', 'a_1', 'a_2', 'a_3', 'a_4']
