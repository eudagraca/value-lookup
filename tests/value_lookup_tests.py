import unittest
from  value_lookup import vlookup

class ExistingValueTestCase(unittest.TestCase):

    # If the word can be found on one char 
    def test_checkSingleString(self):
        result = vlookup("a", "a")
        self.assertTrue(result)
    
    # If a number can be found on one char 

    def test_checkSingleInteger(self):
        result = vlookup(1, 1)
        self.assertTrue(result)

    # If a char can be found in  an string list 

    def test_checkArrayOfStrings(self):
        result = vlookup("a", ["a","b","e","c"])
        self.assertTrue(result)

    # If char can be found in an integer list

    def test_checkArrayOfIntegers(self):
        result = vlookup(0, [1,2,4,5,6])
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()