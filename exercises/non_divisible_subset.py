from unittest import TestCase
from collections import Counter
from itertools import combinations


def get_non_divisible_subset(values, k):
    x = combinations(values, 2)
    stuff = [i[0] for i in list(x) if not is_valid(sum(i), k)]
    c = Counter(stuff)
    return len(c)


def is_valid(number, k):
    return number % k != 0


class NonDivisibleSubset(TestCase):

    def test_non_divisibile_subset_first(self):
        values = [19, 10, 12, 10, 24, 25, 22]
        k = 4
        result = get_non_divisible_subset(values, k)
        self.assertEqual(result, 3)

    def test_non_divisibile_subset_second(self):
        values = [1, 7, 2, 4]
        k = 3
        result = get_non_divisible_subset(values, k)
        self.assertEqual(result, 3)
