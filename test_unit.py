from math_test import *

def testAdd():
    assert add(5,3) == 8
    assert add(1,1) == 2
    assert add(0,0) == 0

def testMinus():
    assert minus(5,3) == 2
    assert minus(1,1) == 0
    assert minus(0,0) == 0