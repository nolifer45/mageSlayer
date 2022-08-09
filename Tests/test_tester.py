#This is a test

def moduloTwoWorks(x):
    return 2 % x

def testInput():
    for i in range(100):    
        assert moduloTwoWorks(i) == 0