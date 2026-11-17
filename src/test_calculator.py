import unittest

from calculator import calculator


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator("add", 3, 2), 5)

    def test_subtraction(self):
        self.assertEqual(calculator("subtract", 3, 2), 1)

    def test_multiplication(self):
        self.assertEqual(calculator("multiply", 3, 2), 6)

    def test_division(self):
        self.assertEqual(calculator("divide", 6, 2), 3)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculator("divide", 6, 0)

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculator("modulo", 6, 2)


if __name__ == "__main__":
    unittest.main()