import unittest
from lesson_netology.practice_netology import multiplication_string, multiplication_int
from parameterized import parameterized

FIXTURES = [
    (2, 3, 6),
    (-2, 1, -2),
    (-2, -2, 4),
    (-2, 2, -4)

]


class TestFunctions(unittest.TestCase):
    # def setUp(self) -> None:
    #     print("метод срабатывает перед каждым тестом ==> setUp")
    #
    # def tearDown(self) -> None:
    #     print("Метод срабатывает после каждого теста ==> setUp")

    @parameterized.expand(FIXTURES)
    def test_multiplication_int(self, a, b, exp_result):
        result = multiplication_int(a, b)
        self.assertEqual(exp_result, result)

    # def test_multiplication_string(self):
    #     result = multiplication_string("q", 2)
    #     self.assertEqual("qq", result)
