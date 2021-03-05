import unittest
import pytest
import fibonacci


#unittest class tests
class TestCase(unittest.TestCase):
    #expected results pulled from this website: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html
    def test_fib_9(self): # made before the fib() function was created
        self.assertEqual(fibonacci.fib(9), 34) #compare expected 9th fib number (34) with output with 9 passed
    def test_fib_0(self): 
        self.assertEqual(fibonacci.fib(0), 0)
    def test_fib_1000(self): 
        self.assertEqual(fibonacci.fib(100), 354224848179261915075)  

        
    def test_fac_9(self):
        self.assertEqual(fibonacci.factorial(9), 362880)

    def test_fac_0(self):
        self.assertEqual(fibonacci.factorial(0), 1 )

    def test_fac5(self):
        self.assertEqual(fibonacci.factorial(5), 120)     



#pytest functions (same as above, just different testing framework)
def test_fib_9():
    assert fibonacci.fib(9) == 34
    
def test_fib_0():
    assert fibonacci.fib(0) == 0

def test_fib_1000():
    assert fibonacci.fib(100) == 354224848179261915075






if __name__ == '__main__':
    unittest.main(verbosity=2)
