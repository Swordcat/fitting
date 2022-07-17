from .. import BaseFitModel, Fermi, Gaussian, InvCoshSq, Linear, Lorentzian, Oscillation, Polynomial, SinExpDecay, SinGaussDecay


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
    assert Fermi().parameters() == ['height', 'sigma', 'offset', 'step']
    assert Gaussian().parameters() == ['height', 'sigma', 'offset', 'location']
    assert InvCoshSq().parameters() == ['height', 'sigma', 'offset', 'location']
    assert Linear().parameters() == ['a', 'b']
    assert Lorentzian().parameters() == ['height', 'sigma', 'offset', 'location']
    assert Oscillation().parameters() == ['amplitude', 'frequency', 'phase', 'offset']
    for i in range(2,7):
        assert Polynomial(order=i)().parameters() == [f'a_{j}' for j in range(i+1)]
    assert SinExpDecay().parameters() == ['amplitude', 'frequency', 'phase', 'offset', 'decay']
    assert SinGaussDecay().parameters() == ['amplitude', 'frequency', 'phase', 'offset', 'decay']

