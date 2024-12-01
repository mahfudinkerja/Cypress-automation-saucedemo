import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5


def test_add_strings():
    result = my_functions.add('I Like ','Burgers')
    assert result == 'I Like Burgers'


def test_devine():
    result = my_functions.devine(10,5)
    assert  result == 2


def test_devide_by_zero():
    with pytest.raises(ValueError):
        my_functions.devine(10,0)