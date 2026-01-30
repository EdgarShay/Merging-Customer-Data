import unittest
from src.merge_customer_data import merge
class TestMergeCustomerData(unittest.TestCase):
    # Normal cases
    def test_normal_case_1(self):
        data1 = [101, 104, 107, 0, 0, 0]
        merge(data1, 3, [102, 105, 108], 3)
        self.assertEqual(data1, [101, 102, 104, 105, 107, 108])
    def test_normal_case_2(self):
        data1 = [1, 3, 5, 0, 0]
        merge(data1, 3, [2, 4], 2)
        self.assertEqual(data1, [1, 2, 3, 4, 5])
    def test_normal_case_3(self):
        data1 = [2, 4, 6, 0, 0, 0]
        merge(data1, 3, [1, 3, 5], 3)
        self.assertEqual(data1, [1, 2, 3, 4, 5, 6])
    # Edge cases
    def test_edge_case_empty_second_array(self):
        data1 = [103]
        merge(data1, 1, [], 0)
        self.assertEqual(data1, [103])
    def test_edge_case_empty_first_array(self):
        data1 = [0, 0, 0]
        merge(data1, 0, [1, 2, 3], 3)
        self.assertEqual(data1, [1, 2, 3])
    def test_edge_case_all_same_values(self):
        data1 = [2, 2, 2, 0, 0]
        merge(data1, 3, [2, 2], 2)
        self.assertEqual(data1, [2, 2, 2, 2, 2])

if __name__ == "__main__":
    unittest.main()

