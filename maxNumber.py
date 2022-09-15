#MaxNumberProgram


#Will determine the biggest number and return that to the user
def maxNumber(x,y):
    if(x>y):
        return x
    else:
        return y

#Will determine the middle number of three different numbers
def middleNumber(x,y,z):
    if(x>y and z>x):
        return x
    elif(y>x and z>y):
        return y
    else:
        return z
print(middleNumber(2,6, 8))

