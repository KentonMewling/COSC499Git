#MaxNumberProgram
import unittest

def maxNumber(x,y):
    if(x>y):
        return x
    else:
        return y
        
#Program for returning the smallest number
def minNumber(x,y):
    if(x>y):
        return y
    else:
        return x

class Tests(unittest.TestCase):
    def test(self):  #method that tests the function 
        self.assertEqual(minNumber(4,-2),-2) #testing minNumber function

if __name__ == '__main__':
    unittest.main()


