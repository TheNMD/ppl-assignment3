import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test1(self):
        input = """x : integer ; x : float ;"""
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test2(self):
        input = """x : integer = 2.0 ;"""
        expect = "Type mismatch in expression: FloatLit(2.0)"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test3(self):
        input = """x : auto ;"""
        expect = "Invalid Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 403))