import unittest
from main import *

# Test Command: python -m unittest test.py

class TestPig(unittest.TestCase):
    def test_winner(self):
        self.assertTrue(winner(100, "Player 1"))
        self.assertTrue(winner(121, "Player 1"))
        self.assertTrue(winner(103, "Player 2"))
        self.assertFalse(winner(90, "Player 1"))
        self.assertFalse(winner(99, "Player 2"))
        self.assertFalse(winner(35, "Player 1"))


    def test_roll(self):
        self.assertEqual(roll("Player 1", roll=[2,2], scores={"Player 1": 12, "Player 2": 24}), 16)
        self.assertEqual(roll("Player 2", roll=[1,1], scores={"Player 1": 32, "Player 2": 87}), 0)
        self.assertEqual(roll("Player 2", roll=[5,7], scores={"Player 1": 43, "Player 2": 25}), 37)
        self.assertEqual(roll("Player 1", roll=[1,6], scores={"Player 1": 71, "Player 2": 21}), 71)
        self.assertEqual(roll("Player 1", roll=[1,2], scores={"Player 1": 16, "Player 2": 7}), 16)
