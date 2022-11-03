import pytest
from lesson_netology.practice_netology import multiplication_string, multiplication_int

FIXTURES = [
    (2, 3, 6),
    (-2, 1, -2),
    (-2, -2, 4),
    (-2, 2, -4)

]


@pytest.mark.parametrize("a, b, exp_result", FIXTURES)
def test_multiplication_int(a, b, exp_result):
    result = multiplication_int(a, b)
    assert exp_result == result
#
# def test_multiplication_string():
#     result = multiplication_string("q", 2)
#     assert "qq" == result
