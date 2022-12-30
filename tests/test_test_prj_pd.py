import pytest
from hypothesis import given, strategies as hy

from test_prj_pd.test_prj_pd import get_my_int


@given(number=hy.integers())
def test_my_integers(number):
    assert number == get_my_int(number)
