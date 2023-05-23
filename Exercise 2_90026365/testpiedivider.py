import unittest
from io import StringIO
from unittest.mock import patch
from Q3PartC import pie_divider

class PieDividerTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=['5', '20'])
    def test_valid_input_values(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            pie_divider()
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "4\n0\nPerfect")

    @patch('builtins.input', side_effect=['-10', '3'])
    def test_negative_number_of_pies(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            pie_divider()
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "Invalid\n0\nPerfect")

    @patch('builtins.input', side_effect=['0', '10'])
    def test_zero_number_of_people(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            pie_divider()
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "Invalid\n0\nPerfect")

    @patch('builtins.input', side_effect=['2', '0'])
    def test_zero_number_of_pies(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            pie_divider()
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "Invalid\n0\nPerfect")

    @patch('builtins.input', side_effect=['15', '4'])
    def test_uneven_division_of_pies(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            pie_divider()
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "3\n3")

if __name__ == '__main__':
    unittest.main()