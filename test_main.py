import pytest
from main import adunare

def test_adunare():
    assert adunare(2, 3) == 5
    assert adunare(-1, 1) == 0
