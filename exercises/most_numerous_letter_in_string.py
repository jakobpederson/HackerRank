from unittest import TestCase
from collections import Counter
from itertools import combinations


def most_numerous_letter_in_string(word):
    # counter = Counter(word)
    # max_value = max(counter.items(), key=lambda x: x[1])[1]
    # return [key for key, val in counter.items() if val == max_value]
    count = {}
    max_count = None
    list_of_max_counts = []
    for i in word:
        if count.get(i):
            count[i] += 1
        else:
            count[i] = 1
        if i != max_count:
            if count[i] == count.get(max_count, 0):
                list_of_max_counts.append(i)
        if count[i] > count.get(max_count, 0):
            list_of_max_counts = [i]
            max_count = i
    return list_of_max_counts


class MostNumerousLetterInStringTests(TestCase):

    def test_most_numerous_letter_in_string_first(self):
        word = 'aaaaaaabsdfje'
        result = most_numerous_letter_in_string(word)
        self.assertEqual(result, ['a'])

    def test_most_numerous_letter_in_string_second(self):
        word = 'aaaaaaabsdfjezzzzzzzzzzzzzzzz'
        result = most_numerous_letter_in_string(word)
        self.assertEqual(result, ['z'])

    def test_most_numerous_letter_handles_two_equal_number_of_max_counts(self):
        word = 'aaadfjezzz'
        result = most_numerous_letter_in_string(word)
        self.assertCountEqual(result, ['z', 'a'])
