
import unittest

from revenue_calculator import calculate_revenue


class TestCalculateRevenue(unittest.TestCase):

    def test_normal_calculation(self):
        self.assertEqual(calculate_revenue(4, 25), 100)

    def test_zero_quantity(self):
        self.assertEqual(calculate_revenue(0, 25), 0)

    def test_decimal_price(self):
        self.assertAlmostEqual(calculate_revenue(3, 2.50), 7.50)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_revenue(-1, 25)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_revenue(2, -25)

    def test_missing_quantity(self):
        with self.assertRaises(TypeError):
            calculate_revenue(None, 25)

    def test_text_input(self):
        with self.assertRaises(TypeError):
            calculate_revenue("four", 25)


if __name__ == "__main__":
    unittest.main()
