import unittest

class Check(unittest.TestCase):
    def test_math(self):
        self.assertEqual(1 + 1, 2)
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
