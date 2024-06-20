import pytest

@pytest.mark.smoke
def test_dummy():
    pass

@pytest.mark.xfail(reason="Feature is not implemented yet")
def test_dummy_2():
    pass

def test_dummy_3():
    pass