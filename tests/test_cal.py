from src.calculator import add
import pytest

def test_add():
    result = add(3, 5)
    assert result == 8
