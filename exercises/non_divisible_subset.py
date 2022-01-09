from unittest import TestCase
from collections import Counter
from itertools import combinations


def get_non_divisible_subset(values, k):
    counts = Counter()
    for number in values:
        counts.update({number % k: 1})
    counts.update({'answer': min(counts[0], 1)})
    if k % 2 == 0:
        counts.update({'answer': min(counts[k//2], 1)})
    for i in range(1 , k//2 + 1) :
        if i != k - i:
            counts.update({'answer': max(counts[i] , counts[k-i])})
    return counts['answer']



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

    def test_non_divisibile_subset_third(self):
        values = [1, 2, 3, 4, 5, 6]
        k = 3
        result = get_non_divisible_subset(values, k)
        self.assertEqual(result, 3)
