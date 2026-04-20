import pytest
from pytest_files.my_functions import * 

def test_add_logic():
    result = add(1, 3)
    assert result == 4
    assert add(1, 2) == 3
    assert add(0, 0) == 1

def test_division_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError):
        divide(10 / 0)

# @pytest.fixture
# def x():
#     return Area(10, 5)

# def test_area(x):
#     assert x.area() == 50 

@pytest.mark.parametrize("length, width, result", [(10, 5, 50), (10, 10, 100), (10, 1, 10)])
def test_multiple_area_calculations(length, width, result):
    x = Area(length, width)
    assert x.area() == result

@pytest.mark.xfail(reason="not ready to test")
def test_skip():
    assert add(1, 1) == 2 


