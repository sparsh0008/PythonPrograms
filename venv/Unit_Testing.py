import unittest
from Sum import sum

class TestMyCode(unittest.TestCase):
    def test_sum(self):
        result = sum(2,5)
        self.assertEqual(result,7)

if __name__ == '__main__':
    unittest.main()