from unittest import TestCase


def flatland_space_stations(n, m, c):
    max_number = 0
    for number in  range(0, n):
        max_number =  max(min([abs(number - place) for place in c]), max_number)
    return max_number


class FlatlandSpaceStationTests(TestCase):
    def test_scenario_1(self):
        n = 3
        m = 1
        c = [1]
        result = flatland_space_stations(n, m, c)
        self.assertEqual(result, 1)

    def test_scenario_2(self):
        n = 6
        m = 6
        c = [0, 1, 2, 3, 4, 5]
        result = flatland_space_stations(n, m, c)
        self.assertEqual(result, 0)
