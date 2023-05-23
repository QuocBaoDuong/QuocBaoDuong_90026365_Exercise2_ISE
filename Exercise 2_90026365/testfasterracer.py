import unittest

from Q3PartB import fastest_racer

class FastestRacerTestCase(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(fastest_racer("John", "Mike", 1, 1, 1, 1), "Tie")
        self.assertEqual(fastest_racer("John", "Mike", 1, 2, 1, 1), "John")
        self.assertEqual(fastest_racer("John", "Mike", 2, 1, 1, 1), "Mike")
        self.assertEqual(fastest_racer("John", "Mike", 1000, 1000, 1, 1), "Tie")
        self.assertEqual(fastest_racer("John", "Mike", 1, 1000, 1, 1), "John")
        self.assertEqual(fastest_racer("John", "Mike", 1000, 1, 1, 1), "Mike")

    def test_invalid_inputs(self):
        self.assertEqual(fastest_racer("John", "Mike", 0, 1, 1, 1), "Invalid Input")
        self.assertEqual(fastest_racer("John", "Mike", 1, 0, 1, 1), "Invalid Input")
        self.assertEqual(fastest_racer("John", "Mike", -1, 1, 1, 1), "Invalid Input")
        self.assertEqual(fastest_racer("John", "Mike", 1, -1, 1, 1), "Invalid Input")
        self.assertEqual(fastest_racer("John", "Mike", 0, 0, 1, 1), "Invalid Input")
        self.assertEqual(fastest_racer("John", "Mike", -1, -1, 1, 1), "Invalid Input")

if __name__ == '__main__':
    unittest.main()