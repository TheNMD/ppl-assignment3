import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test1(self):
    #     input = """x : integer ; x : float ;"""
    #     expect = "Redeclared Variable: x"
    #     self.assertTrue(TestChecker.test(input, expect, 401))
        
    # def test2(self):
    #     input = """x : integer = 2.0 ;"""
    #     expect = "Type mismatch in expression: FloatLit(2.0)"
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test3(self):
    #     input = """x : auto ;"""
    #     expect = "Invalid Variable: x"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test4(self):
    #     input = """x, y, z : string = "abd", "eex", 5 ;"""
    #     expect = "Type mismatch in expression: IntegerLit(5)"
    #     self.assertTrue(TestChecker.test(input, expect, 404))
        
    # def test5(self):
    #     input = """x, y : integer = 2, x ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 405))
    
    # def test6(self):
    #     input = """x : string = 22 ;"""
    #     expect = "Type mismatch in expression: IntegerLit(22)"
    #     self.assertTrue(TestChecker.test(input, expect, 406))
        
    # def test7(self):
    #     input = """x, y : string = "22", z ;"""
    #     expect = "Undeclared Variable: z"
    #     self.assertTrue(TestChecker.test(input, expect, 407))
    
    # def test8(self):
    #     input = """a, b, c, d, e : integer = 2, a, b, c, d ; x, y, z : float = a, b, c ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 408))
        
    # def test9(self):
    #     input = """a : string ; b : string = a ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 409))
    
    # def test10(self):
    #     input = """a : integer = 1 + 1.2 ;"""
    #     expect = "Type mismatch in expression: BinExpr(+, IntegerLit(1), FloatLit(1.2))"
    #     self.assertTrue(TestChecker.test(input, expect, 410))
        
    # def test11(self):
    #     input = """a : float = 1 + 1.2 ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 411))
        
    # def test12(self):
    #     input = """a : integer = 1.93 + 1.2 ;"""
    #     expect = "Type mismatch in expression: BinExpr(+, FloatLit(1.93), FloatLit(1.2))"
    #     self.assertTrue(TestChecker.test(input, expect, 412))
        
    def test13(self):
        input = """a : integer = 1 + 2 + 3 ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
    # def test14(self):
    #     input = """a : integer = 1 + 2 + 3.3 ;"""
    #     expect = "Type mismatch in expression: BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), FloatLit(3.3))"
    #     self.assertTrue(TestChecker.test(input, expect, 414))
        
    # def test15(self):
    #     input = """a : integer = 1 + 2.2 + 3 ;"""
    #     expect = "Type mismatch in expression: BinExpr(+, BinExpr(+, IntegerLit(1), FloatLit(2.2)), IntegerLit(3))"
    #     self.assertTrue(TestChecker.test(input, expect, 415))
    
    # def test16(self):
    #     input = """a : float = 1 + 2 + 3.3 ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 416))                      