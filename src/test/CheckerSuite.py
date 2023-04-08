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
    
    def test8(self):
        input = """a, b, c, d, e : integer = 2, a, b, c, d ; x, y, z : float = a, b, c ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test9(self):
        input = """a : string ; b : string = a ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test10(self):
        input = """a : integer = 1 + 1.2 ;"""
        expect = "Type mismatch in expression: BinExpr(+, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test11(self):
        input = """a : float = 1 + 1.2 ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 411))
        
    def test12(self):
        input = """a : integer = 1.93 + 1.2 ;"""
        expect = "Type mismatch in expression: BinExpr(+, FloatLit(1.93), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 412))
        
    def test13(self):
        input = """a : integer = 1 + 2 + 3 ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
    def test14(self):
        input = """a : integer = 1 + 2 + 3.3 ;"""
        expect = "Type mismatch in expression: BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), FloatLit(3.3))"
        self.assertTrue(TestChecker.test(input, expect, 414))
        
    def test15(self):
        input = """a : integer = 1 + 2.2 + 3 ;"""
        expect = "Type mismatch in expression: BinExpr(+, BinExpr(+, IntegerLit(1), FloatLit(2.2)), IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 415))
    
    def test16(self):
        input = """a : integer = 1 + true ;"""
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker.test(input, expect, 416))
        
    def test17(self):
        input = """a : integer = 1 + 0.9 ;"""
        expect = "Type mismatch in expression: BinExpr(+, IntegerLit(1), FloatLit(0.9))"
        self.assertTrue(TestChecker.test(input, expect, 417))
        
    def test18(self):
        input = """a : integer = 8 % 3 ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
    def test19(self):
        input = """a : integer = 8 % 2.3 ;"""
        expect = "Type mismatch in expression: FloatLit(2.3)"
        self.assertTrue(TestChecker.test(input, expect, 419))
        
    def test20(self):
        input = """a : float = 8 % 2 ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 420))
        
    def test21(self):
        input = """a : boolean = true || false || 2 ;"""
        expect = "Type mismatch in expression: IntegerLit(2)"
        self.assertTrue(TestChecker.test(input, expect, 421))
        
    def test22(self):
        input = """a : string = true || false || true ;"""
        expect = "Type mismatch in expression: BinExpr(||, BinExpr(||, BooleanLit(True), BooleanLit(False)), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 422))
        
    def test23(self):
        input = """c, b : integer ; a : boolean = c == b ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 423))
        
    def test24(self):
        input = """a, b, c : integer ; d : float = a + b + c ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 424))
        
    def test25(self):
        input = """a, b : integer ; c : string ; d : float = a + b + c ;"""
        expect = "Type mismatch in expression: Id(c)"
        self.assertTrue(TestChecker.test(input, expect, 425))
        
    def test26(self):
        input = """c, b : float ; a : boolean = c == b ;"""
        expect = "Type mismatch in expression: Id(c)"
        self.assertTrue(TestChecker.test(input, expect, 426))
        
    def test27(self):
        input = """ a : integer = 2 == 6 ;"""
        expect = "Type mismatch in expression: BinExpr(==, IntegerLit(2), IntegerLit(6))"
        self.assertTrue(TestChecker.test(input, expect, 427))
        
    def test28(self):
        input = """ a : boolean = 2 != false ;"""
        expect = "Type mismatch in expression: BooleanLit(False)"
        self.assertTrue(TestChecker.test(input, expect, 428))
        
    def test29(self):
        input = """ a : boolean = 3 >= 3.4 ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 429))
        
    def test30(self):
        input = """ b : float ; a : boolean = 3 >= b ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 430))
        
    def test31(self):
        input = """ b : string ; a : boolean = 3 >= b ;"""
        expect = "Type mismatch in expression: Id(b)"
        self.assertTrue(TestChecker.test(input, expect, 431))
        
    def test32(self):
        input = """ a : string = "2" :: "33" ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test33(self):
        input = """ x : string = "223232" ; a : string = "2" :: x ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 433))
        
    def test34(self):
        input = """ x : float = -2.5554 ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 434))
        
    def test35(self):
        input = """ x : float = -2.5554 + 3 + -4.2 ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 435))
        
    def test36(self):
        input = """ x : boolean = !true ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 436))
        
    def test37(self):
        input = """ a : boolean = false ; x : boolean = !a ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 437))
        
    def test38(self):
        input = """ a : string = "false" ; x : boolean = !a ;"""
        expect = "Type mismatch in expression: Id(a)"
        self.assertTrue(TestChecker.test(input, expect, 438))                                                                