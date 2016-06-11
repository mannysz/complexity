from unittest import TestCase

from solutions.slow import solution as slow_solution


class SlowSolutionTest(TestCase):

    def test_small_range(self):
        """
        Expects value to be 55.
        """
        value = slow_solution(10)
        self.assertEqual(value, 55)

    def test_fair_range(self):
        """
        Expects value to be 50 million and 5 thousand
        """
        value = slow_solution(10000)
        self.assertEqual(value, 50005000)

    def test_double_range(self):
        """
        Expects value to be 20 millions and 10 thousand.
        """
        value = slow_solution(20000)
        self.assertEqual(value, 200010000)
