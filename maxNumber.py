#MaxNumberProgram
import unittest

def maxNumber(x,y):
        if(x>y):
            return x
        else:
            return y

    #Will determine the middle number of three different numbers
def middleNumber(x,y,z):
    if((x>y and z>x) or (y>x and x>z)):
           return x
    elif((y>x and z>y) or (x>y and y>z)):
        return y
    elif((z>x and y>z) or (x>z and z>y)):
        return z
    else:
        return 0
#Program for returning the smallest number
def minNumber(x,y):
    if(x>y):
        return y
    else:
        return x


print(maxNumber(4,-2)) #4
print(minNumber(4,-2))  #-2
print(middleNumber(4,2,6))  #4

#Inline Comment  

class Tests(unittest.TestCase):
    def test(self):  #method that tests the function 
        self.assertEqual(minNumber(4,-2),-2) #testing minNumber function
        self.assertEqual(maxNumber(4,-2),4) #testing maxNumber function
        self.assertEqual(middleNumber(4,2,6),4) #testing middleNumber function

if __name__ == '__main__':
    unittest.main()


