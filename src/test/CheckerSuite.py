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

    def test4(self):
        input = """x, y, z : string = "abd", "eex", 5 ;"""
        expect = "Type mismatch in expression: IntegerLit(5)"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test5(self):
        input = """x, y : integer = 2, x ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test6(self):
        input = """x : string = 22 ;"""
        expect = "Type mismatch in expression: IntegerLit(22)"
        self.assertTrue(TestChecker.test(input, expect, 406))
        
    def test7(self):
        input = """x, y : string = "22", z ;"""
        expect = "Undeclared Variable: z"
        self.assertTrue(TestChecker.test(input, expect, 407))