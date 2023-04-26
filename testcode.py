import unittest
import dec_2_hex as dh

class averageTestCase(unitest.TestCase):

    def test_average1(self):
        answer = dh.decimal_to_hex(100)
        self.assertEqual(answer, "64")

    def test_average2(self):
        answer = dh.decimal_to_hex(1)
        self.assertEqual(answer, "1")

if __name__ == "__main__":
    unittest.main()