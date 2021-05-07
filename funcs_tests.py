import unittest
from funcs import *

class TestCases(unittest.TestCase):
   def test_f_1(self):
      self.assertAlmostEqual(f(1),9)

   def test_f_2(self):
      self.assertAlmostEqual(f(0),0)

   def test_g_1(self):
      # Add code here. REMOVE PASS
      self.assertAlmostEqual(g(1,0),0.3333333333)
      
   def test_g_2(self):
      self.assertAlmostEqual(g(1,1),0.6666666666)

   def test_g_3(self):
      self.assertRaises(ZeroDivisionError, g, 0, 3)

   def test_hypotenuse1(self):
      # Add code here. REMOVE PASS
      self.assertAlmostEqual(hypotenuse(3,4),5)
  
   def test_hypotenuse2(self):
      self.assertAlmostEqual(hypotenuse(6,8),10)

   def test_ispositive1(self):
      self.assertFalse(is_positive(-1))

   def test_ispositive2(self):
      self.assertTrue(is_positive(1))   
   
   # Add five more tests...

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

