import unittest
from example import check_char_count
from example import check_char_type
from example import check_char_match

class TestJsonEx(unittest.TestCase): #Uppercase first letter for classes just to identify better

#For unittests assume the use of a default constructor

    def test_check_char_count(self):
        self.assertEqual(check_char_count('AA'), 'AA count passes') #assertEqual is inherited from the unittest class (look at documentation)
        self.assertEqual(check_char_count('AAA'), 'AAA count FAILS')
        self.assertRaises(AssertionError, check_char_count, 1)
        self.assertRaises(AssertionError, check_char_count, True)
        self.assertRaises(AssertionError, check_char_count, ['AA', 'BB']) #The code ran even though we sent it a list instead of sending an error, so it FAILED

    def test_check_char_type(self):
        self.assertEqual(check_char_type('AA'), 'AA type passes')
        self.assertEqual(check_char_type('AAA'),'AAA type passes')
        self.assertEqual(check_char_type('Aa'), 'Aa type FAILS')
        self.assertEqual(check_char_type('aa'), 'aa type FAILS')
        self.assertEqual(check_char_type('A1'), 'A1 type FAILS')
        self.assertEqual(check_char_type('a1'), 'a1 type FAILS')
        self.assertRaises(AttributeError, check_char_type, 1)
        self.assertRaises(AttributeError, check_char_type, True)
        self.assertRaises(AttributeError, check_char_type, ['AA', 'BB'])

    def test_check_char_match(self):
        self.assertEqual(check_char_match('BZ','Brizona'), 'BZ match FAILS')
        self.assertEqual(check_char_match('AZ','Arizona'), 'AZ match passes')
        self.assertRaises(IndexError, check_char_match, 'AA', '')

if __name__ == '__main__':
    unittest.main()
