import unittest

class SmokeTest(unittest.TestCase):

    def test_smoke(self):
        self.assertEqual(2 + 2, 4)


if __name__ == '__main__':
    unittest.main()