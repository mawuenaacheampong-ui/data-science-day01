
import unittest

from data_02_data_structures import (
    binary_search,
    linear_search,
    unique_preserving_order,
)


class TestDayTwo(unittest.TestCase):

    def test_linear_search_found(self):
        self.assertEqual(linear_search([10, 20, 30], 20), 1)

    def test_linear_search_missing(self):
        self.assertEqual(linear_search([10, 20, 30], 99), -1)

    def test_binary_search_found(self):
        self.assertEqual(binary_search([10, 20, 30, 40], 30), 2)

    def test_binary_search_missing(self):
        self.assertEqual(binary_search([10, 20, 30, 40], 99), -1)

    def test_binary_search_empty_list(self):
        self.assertEqual(binary_search([], 10), -1)

    def test_unique_ids_preserve_order(self):
        self.assertEqual(
            unique_preserving_order([201, 202, 201, 203, 202]),
            [201, 202, 203],
        )

    def test_empty_list(self):
        self.assertEqual(unique_preserving_order([]), [])


if __name__ == "__main__":
    unittest.main()
