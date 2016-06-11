from unittest import TestCase

from solutions.fast import solution


class FairSolutionTest(TestCase):

    def test_small_range(self):
        """
        Expects value to be 55.
        """
        value = solution(10)
        self.assertEqual(value, 55)

    def test_fair_range(self):
        """
        Expects value to be 50 million and 5 thousand
        """
        value = solution(10000)
        self.assertEqual(value, 50005000)

    def test_double_range(self):
        """
        Expects value to be 20 millions and 10 thousand.
        """
        value = solution(20000)
        self.assertEqual(value, 200010000)

    def test_huge_range(self):
        """
        Expects value to be a huge outnumbered number that can be
        writen extense
        """
        value = solution(1000000)
        self.assertEqual(value, 500000500000)
