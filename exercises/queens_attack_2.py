from unittest import TestCase
from collections import Counter
from itertools import combinations


def queens_attack(board_length, number_obstacles, queen, obstacles):
    count = 0
    for x in range(board_length + 1):
        if x != queen[0]:
            count += 1
    for y in range(board_length +  1):
        if y != queen[1]:
            count += 1
    return count


class QueensAttackTests(TestCase):

    def test_queens_attack_first(self):
        board_length = 4
        number_obstacles = 0
        queen = [4, 4]
        result = queens_attack(board_length, number_obstacles, queen, [])
        self.assertEqual(result, 9)

    def test_queens_attack_second(self):
        board_length = 5
        number_obstacles = 3
        queen = [4, 3]
        obstacles = [(5, 5), (4, 2), (2, 3)]
        result = queens_attack(board_length, number_obstacles, queen, obstacles)
        self.assertEqual(result, 10)
