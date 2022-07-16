from ..dataclass import *

def test_dataclass():
    test_dc = factory('test', ['a', 'b', 'c'])
    instance = test_dc(Parameter(1, 0), Parameter(3, 2), Parameter(5, 2.3))

    assert list(instance.to_dict().keys()) == ['a', 'b', 'c']

    assert instance.a.value == 1
    assert instance.a.error == 0
    assert instance.b.value == 3
    assert instance.b.error == 2
    assert instance.c.value == 5
    assert instance.c.error == 2.3

    assert instance.values() == [1, 3, 5]
    assert instance.errors() == [0, 2, 2.3]
    assert instance.parameters() == ['a', 'b', 'c']