"""
    Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
    A palindrome is a word or phrase that is the same forwards and backwards. A permutation
    is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
    
    Complexity of my solutions is O(N) with the optimization of space in (palindromePermutation_BitVector)
"""
import string
def palindromePermutation_AuxSpace(st):
    ascii_char = dict.fromkeys(string.ascii_lowercase + string.ascii_uppercase, True) 
    
    dictionary = {}
    for char in st.lower():
        if(ascii_char.get(char) != None): # ignore char that are not ASCII
            if dictionary.get(char) == None or dictionary.get(char) == 0:
                dictionary[char] = 1
            else:
                dictionary[char] -= 1
    
    countNonZero = 0
    for freq in dictionary.values():
        if(freq > 0):
            countNonZero += 1
    
    #print(dictionary)
    
    if(countNonZero > 1):
        return False
    else:
        return True
    

def palindromePermutation_BitVector(st):
    ascii_char = dict.fromkeys(string.ascii_lowercase, True) 
    storage = 0
    for char in st.lower():
        
        bitIndex = ord(char) - ord('a')
        
        if(ascii_char.get(char) != None): # ignore char that are not ASCII
            if ((storage & 1<<bitIndex) == 0): # if bitIndex'th bit is OFF, then turn it on
                storage |= 1<<bitIndex
            else:
                storage ^= (1<<bitIndex)
    
    """
        If storage is either Zero, MEANS the string is EVEN palindrome OR 
        check for ODD palindrome i.e. storage will be power of 2 (power of 2 means ONLY ONE bit is ON at a time) 
            then, the provided string is considered to be permutation of a palindrome
    """
    return (storage == 0 or (storage & (storage-1) == 0))
    
#palindromePermutation_BitVector("anaaacaaaana") #madamimadam, imada m'm adam, never odd or even

import unittest
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_palindromePermutation_BitVector(self):
        for [test_string, expected] in self.data:
            actual = palindromePermutation_BitVector(test_string)
            self.assertEqual(actual, expected)

    if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)

