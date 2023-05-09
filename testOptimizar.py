import pytest
from optimizar import Optimizar

def test_media():
    optimizado = Optimizar()
    optimizado.array.clear()
    assert len(optimizado.array) == 0
    optimizado.add(3)
    optimizado.add(6)
    optimizado.add(9)
    assert len(optimizado.array) == 3
    assert optimizado.media() == 6

def test_add():
    optimizado = Optimizar()
    optimizado.add(12)
    assert optimizado.array == [3,6,9,12]

def test_media_con_array_vacio():
    optimizado = Optimizar()
    optimizado.array.clear()
    assert len(optimizado.array) == 0
    assert optimizado.media() == 1

def test_inp(mocker):
    mocker.patch('builtins.input', return_value='4')
    optimizado = Optimizar()
    assert optimizado.inp() == 4
