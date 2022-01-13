from unittest import TestCase
from collections import Counter
from itertools import combinations


def most_numerous_letter_in_string(word):
    counter = Counter()
    max_count = 0
    max_letter = []
    for letter in word:
       counter.update({letter: 1})
       if counter[letter] > max_count:
           max_count = counter[letter]
           max_letter = [letter]
       elif counter[letter] == max_count:
            max_letter.append(letter)
    return max_letter


class MostNumerousLetterInStringTests(TestCase):

    def test_most_numerous_letter_in_string_first(self):
        word = 'aaaaaaabsdfje'
        result = most_numerous_letter_in_string(word)
        self.assertEqual(result, ['a'])

    def test_most_numerous_letter_in_string_second(self):
        word = 'aaaaaaabsdfjezzzzzzzzzzzzzzzz'
        result = most_numerous_letter_in_string(word)
        self.assertEqual(result, ['z'])

    def test_most_numerous_letter_handles_two_equal_number_of_max_letters(self):
        word = 'aaadfjezzz'
        result = most_numerous_letter_in_string(word)
        self.assertCountEqual(result, ['z', 'a'])
