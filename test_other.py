from hypothesis import given, example
from hypothesis.strategies import integers

from simple import add_one

@given(integers())
@example(-1)
def test_add_one(s):
    assert add_one(s) == s + 1