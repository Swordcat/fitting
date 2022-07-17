from ..registry import model_registry

def test_case_insensitive():
    m1 = model_registry.get('Linear')
    m2 = model_registry.get('linear')
    m3 = model_registry.get('LINEAR')
    m4 = model_registry.get('LiNeAr')
    assert m1 == m2
    assert m1 == m3
    assert m1 == m4
