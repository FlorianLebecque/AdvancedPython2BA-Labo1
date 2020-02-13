# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
from utils import *

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(fact(5),120)
        # À compléter...
        pass
    
    def test_roots(self):
        # À compléter...
        self.assertEqual(roots(1,0,1),())
        self.assertEqual(roots(1,1,0),(0,-1))
        pass
    
    def test_integrate(self):
        # À compléter...
        self.assertAlmostEqual(integrate('x ** 2 - 1', -1, 1),-1.333333,6)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
