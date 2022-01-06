from unittest import TestCase


class NegativeNumberException(Exception):
    pass


def extra_long_factorial(number):
    if number < 0:
        raise NegativeNumberException()
    value = 1
    for n in range(1, number + 1):
        value = value * n
    return value


class ExtraLongFactorialTests(TestCase):
    def test_number_25(self):
        n = 25
        result = extra_long_factorial(n)
        self.assertEqual(result, 15511210043330985984000000)

    def test_number_5(self):
        n = 5
        result = extra_long_factorial(n)
        self.assertEqual(result, 120)

    def test_number_0(self):
        n = 0
        result = extra_long_factorial(n)
        self.assertEqual(result, 1)

    def test_number_less_than_0(self):
        n = -1
        with self.assertRaises(NegativeNumberException):
            result = extra_long_factorial(n)
