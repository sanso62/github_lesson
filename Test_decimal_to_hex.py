import unittest
import decimal_to_hex as dh

class averageTestCase(unittest.TestCase):
    def test_average1(self):
        answer=dh.decimal_to_hex(0)
        self.assertEqual(answer, "0x0")
    def test_average2(self):
        answer=dh.decimal_to_hex(16)
        self.assertEqual(answer, "0x10")
    def test_average3(self):
        answer=dh.decimal_to_hex(92357)
        self.assertEqual(answer, "0x168c5")

if __name__=="__main__":
    unittest.main()