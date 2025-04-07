import unittest
from src.roman_converter import roman_to_decimal

class TestRomanToDecimal(unittest.TestCase):

    def test_I(self):
        decimal = roman_to_decimal('I')
        self.assertEqual(decimal, 1)

    def test_II(self):
        decimal = roman_to_decimal('II')
        self.assertEqual(decimal, 2)

    def test_III(self):
        decimal = roman_to_decimal('III')
        self.assertEqual(decimal, 3)

    def test_IV(self):
        decimal = roman_to_decimal('IV')
        self.assertEqual(decimal, 4)

    def test_V(self):
        decimal = roman_to_decimal('V')
        self.assertEqual(decimal, 5)

    def test_VI(self):
        decimal = roman_to_decimal('VI')
        self.assertEqual(decimal, 6)

    def test_VIII(self):
        decimal = roman_to_decimal('VIII')
        self.assertEqual(decimal, 8)

    def test_IX(self):
        decimal = roman_to_decimal('IX')
        self.assertEqual(decimal, 9)

    def test_X(self):
        decimal = roman_to_decimal('X')
        self.assertEqual(decimal, 10)

    def test_XL(self):
        decimal = roman_to_decimal('XL')
        self.assertEqual(decimal, 40)

    def test_L(self):
        decimal = roman_to_decimal('L')
        self.assertEqual(decimal, 50)

    def test_XC(self):
        decimal = roman_to_decimal('XC')
        self.assertEqual(decimal, 90)

    def test_C(self):
        decimal = roman_to_decimal('C')
        self.assertEqual(decimal, 100)

    def test_CD(self):
        decimal = roman_to_decimal('CD')
        self.assertEqual(decimal, 400)

    def test_D(self):
        decimal = roman_to_decimal('D')
        self.assertEqual(decimal, 500)

    def test_CM(self):
        decimal = roman_to_decimal('CM')
        self.assertEqual(decimal, 900)

    def test_M(self):
        decimal = roman_to_decimal('M')
        self.assertEqual(decimal, 1000)

    def test_complex(self):
        self.assertEqual(roman_to_decimal('XLIX'), 49)
        self.assertEqual(roman_to_decimal('XCIX'), 99)
        self.assertEqual(roman_to_decimal('CDXCIX'), 499)
        self.assertEqual(roman_to_decimal('CMXCIX'), 999)
        self.assertEqual(roman_to_decimal('MMMCMXCIX'), 3999)

def main():
    my_roman = input('decime tu romano: ')
    decimal_humano = roman_to_decimal(my_roman)
    print(my_roman + ' -> ' + str(decimal_humano))

if __name__ == '__main__':
    unittest.main()
