''' Run "pytest" to run tests '''
import random
import pytest
from app import elo


def test_sort():
    ''' Try 1000 times, the result should have a very high chance to be perfectly
    sorted '''
    items = [random.randint(-1000, 1000) for _ in xrange(10)]
    elo_res = elo.sorted(items, rounds=len(items)*1000)
    py_res = sorted(items)
    assert elo_res == py_res
