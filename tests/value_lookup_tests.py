import unittest
from  value_lookup import ValueLookup

class ExistingValueTestCase(unittest.TestCase):

    def setUp(self):
        self.check_exist_val = ValueLookup()
    
    # If the word can be found on one char 
    def test_checkSingleString(self):
        result = self.check_exist_val.value_exists("a", "a")
        self.assertFalse(result)
    
    # If a number can be found on one char 

    def test_checkSingleInteger(self):
        result = self.check_exist_val.value_exists(1, 1)
        self.assertFalse(result)

    # If a char can be found in  an string list 

    def test_checkArrayOfStrings(self):
        result = self.check_exist_val.value_exists("a", ["a","b","e","c"])
        self.assertFalse(result)

    # If char can be found in an integer list

    def test_checkArrayOfIntegers(self):
        result = self.check_exist_val.value_exists(0, [1,2,4,5,6])
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()