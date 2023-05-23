import unittest
from Q3PartA import move_direction

class MoveDirectionTestCase(unittest.TestCase):
    def test_valid_positions_and_directions(self):
        self.assertEqual(move_direction('N', 3, 4), (3, 3))
        self.assertEqual(move_direction('S', 2, 5), (2, 6))
        self.assertEqual(move_direction('E', 6, 3), (7, 3))
        self.assertEqual(move_direction('W', 4, 2), (3, 2))
        self.assertEqual(move_direction('NE', 1, 6), (2, 5))
        self.assertEqual(move_direction('NW', 5, 7), (4, 6))
        self.assertEqual(move_direction('SE', 0, 0), (1, 1))

    def test_invalid_positions(self):
        with self.assertRaises(ValueError):
            move_direction('N', -1, 4)
        with self.assertRaises(ValueError):
            move_direction('N', 3, -1)
        with self.assertRaises(ValueError):
            move_direction('N', 8, 4)
        with self.assertRaises(ValueError):
            move_direction('N', 4, 8)
        with self.assertRaises(ValueError):
            move_direction('NE', -1, 6)
        with self.assertRaises(ValueError):
            move_direction('NE', 1, 8)
        with self.assertRaises(ValueError):
            move_direction('SE', -1, 0)
        with self.assertRaises(ValueError):
            move_direction('SE', 0, 8)
        with self.assertRaises(ValueError):
            move_direction('SW', 6, 8)

    def test_invalid_directions(self):
        with self.assertRaises(ValueError):
            move_direction('X', 3, 4)
        with self.assertRaises(ValueError):
            move_direction('', 2, 5)

if __name__ == '__main__':
    unittest.main()