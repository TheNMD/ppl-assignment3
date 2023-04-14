import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test1(self):
    #     input = """x : integer = x + 1 ;"""
    #     expect = "[]"
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
    #     expect = "Undeclared Identifier: z"
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
        
    # def test13(self):
    #     input = """a : integer = 1 + 2 + 3 ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 413))
        
    # def test14(self):
    #     input = """a : integer = 1 + 2 + 3.3 ;"""
    #     expect = "Type mismatch in expression: BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), FloatLit(3.3))"
    #     self.assertTrue(TestChecker.test(input, expect, 414))
        
    # def test15(self):
    #     input = """a : integer = 1 + 2.2 + 3 ;"""
    #     expect = "Type mismatch in expression: BinExpr(+, BinExpr(+, IntegerLit(1), FloatLit(2.2)), IntegerLit(3))"
    #     self.assertTrue(TestChecker.test(input, expect, 415))
    
    # def test16(self):
    #     input = """a : integer = 1 + true ;"""
    #     expect = "Type mismatch in expression: BooleanLit(True)"
    #     self.assertTrue(TestChecker.test(input, expect, 416))
        
    # def test17(self):
    #     input = """a : integer = 1 + 0.9 ;"""
    #     expect = "Type mismatch in expression: BinExpr(+, IntegerLit(1), FloatLit(0.9))"
    #     self.assertTrue(TestChecker.test(input, expect, 417))
        
    # def test18(self):
    #     input = """a : integer = 8 % 3 ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 418))
        
    # def test19(self):
    #     input = """a : integer = 8 % 2.3 ;"""
    #     expect = "Type mismatch in expression: FloatLit(2.3)"
    #     self.assertTrue(TestChecker.test(input, expect, 419))
        
    # def test20(self):
    #     input = """a : float = a % 2 ;"""
    #     expect = "Type mismatch in expression: Id(a)"
    #     self.assertTrue(TestChecker.test(input, expect, 420))
        
    # def test21(self):
    #     input = """a : boolean = true || false || 2 ;"""
    #     expect = "Type mismatch in expression: IntegerLit(2)"
    #     self.assertTrue(TestChecker.test(input, expect, 421))
        
    # def test22(self):
    #     input = """a : string = true || false || true ;"""
    #     expect = "Type mismatch in expression: BinExpr(||, BinExpr(||, BooleanLit(True), BooleanLit(False)), BooleanLit(True))"
    #     self.assertTrue(TestChecker.test(input, expect, 422))
        
    # def test23(self):
    #     input = """c, b : integer ; a : boolean = a && (c == b) ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 423))
        
    # def test24(self):
    #     input = """a, b, c : integer ; d : float = a + b + c ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 424))
        
    # def test25(self):
    #     input = """a, b : integer ; c : string ; d : float = a + b + c ;"""
    #     expect = "Type mismatch in expression: Id(c)"
    #     self.assertTrue(TestChecker.test(input, expect, 425))
        
    # def test26(self):
    #     input = """c, b : float ; a : boolean = c == b ;"""
    #     expect = "Type mismatch in expression: Id(c)"
    #     self.assertTrue(TestChecker.test(input, expect, 426))
        
    # def test27(self):
    #     input = """ a : integer = 2 == 6 ;"""
    #     expect = "Type mismatch in expression: BinExpr(==, IntegerLit(2), IntegerLit(6))"
    #     self.assertTrue(TestChecker.test(input, expect, 427))
        
    # def test28(self):
    #     input = """ a : boolean = 2 != false ;"""
    #     expect = "Type mismatch in expression: BooleanLit(False)"
    #     self.assertTrue(TestChecker.test(input, expect, 428))
        
    # def test29(self):
    #     input = """ a : boolean = 3 >= 3.4 ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 429))
        
    # def test30(self):
    #     input = """ b : float ; a : boolean = 3 >= b ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 430))
        
    # def test31(self):
    #     input = """ b : string ; a : boolean = 3 >= b ;"""
    #     expect = "Type mismatch in expression: Id(b)"
    #     self.assertTrue(TestChecker.test(input, expect, 431))
        
    # def test32(self):
    #     input = """ a : string = "2" :: "33" ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 432))

    # def test33(self):
    #     input = """ x : string = "223232" ; a : string = "2" :: x ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 433))
        
    # def test34(self):
    #     input = """ x : float = -2.5554 ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 434))
        
    # def test35(self):
    #     input = """ x : float = -2.5554 + 3 + -4.2 ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 435))
        
    # def test36(self):
    #     input = """ x : boolean = !true ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 436))
        
    # def test37(self):
    #     input = """ a : boolean = false ; x : boolean = !a ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 437))
        
    # def test38(self):
    #     input = """ a : string = "false" ; x : boolean = !a ;"""
    #     expect = "Type mismatch in expression: Id(a)"
    #     self.assertTrue(TestChecker.test(input, expect, 438))
        
    # def test39(self):
    #     input = """ x : integer ; a : array [1,2] of integer = {1, 2, x} ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 439))
        
    # def test40(self):
    #     input = """ x : float ; a : array [1,2] of integer = {1, 2, x} ;"""
    #     expect = "Illegal array literal: Id(x)"
    #     self.assertTrue(TestChecker.test(input, expect, 440))
        
    # def test41(self):
    #     input = """ a : array [1,2] of integer = {1, 2, x} ;"""
    #     expect = "Undeclared Identifier: x"
    #     self.assertTrue(TestChecker.test(input, expect, 441))
        
    # def test42(self):
    #     input = """ a : array [1,2] of integer = {1 + 2, 3 + 4} ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 442))
        
    # def test43(self):
    #     input = """ a : array [1,2] of integer = {true, 1} ;"""
    #     expect = "Illegal array literal: IntegerLit(1)"
    #     self.assertTrue(TestChecker.test(input, expect, 443))
        
    # def test44(self):
    #     input = """ x, y : integer ; a : array [1,2] of integer = {1 + x, 2 * y} ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 444))
        
    # def test45(self):
    #     input = """ x, y : integer ; b : array [2, 3] of integer ; a : array [1,2] of integer = {1 + x, 2 * b} ;"""
    #     expect = "Type mismatch in expression: Id(b)"
    #     self.assertTrue(TestChecker.test(input, expect, 445))
        
    # def test46(self):
    #     input = """ a : array [1,2] of integer = {true, true, false} ;"""
    #     expect = "Type mismatch in expression: ArrayLit([BooleanLit(True), BooleanLit(True), BooleanLit(False)])"
    #     self.assertTrue(TestChecker.test(input, expect, 446))
        
    # def test47(self):
    #     input = """ a : array [1, 2] of integer ; b : integer = a[2] ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 447))
        
    # def test48(self):
    #     input = """ b : integer = a[2] ;"""
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input, expect, 448))
        
    # def test49(self):
    #     input = """ a : integer ; b : integer = a[2] ;"""
    #     expect = "Type mismatch in expression: a"
    #     self.assertTrue(TestChecker.test(input, expect, 449))
        
    # def test50(self):
    #     input = """ a : array [1,2] of integer ; b : integer = a[2, 3, 5] ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 450))
        
    # def test51(self):
    #     input = """ a : array [1,2] of integer ; b : integer = a[2.2] ;"""
    #     expect = "Type mismatch in expression: FloatLit(2.2)"
    #     self.assertTrue(TestChecker.test(input, expect, 451))
        
    # def test52(self):
    #     input = """ a : array [1,2] of integer ; b : integer = a[1 + 2] ;"""
    #     expect = "Type mismatch in expression: BinExpr(+, IntegerLit(1), IntegerLit(2))"
    #     self.assertTrue(TestChecker.test(input, expect, 452))
        
    # def test53(self):
    #     input = """ a : auto = "false" ; b : auto = a ;"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 453))
        
    # def test54(self):
    #     input = """ a : integer = 4 ; b : float = (a + 3) / 4 ; """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 454))
        
    # def test55(self):
    #     input = """ a : integer = 4 ; b : string = !(((a + 3) / 4) >= 8) ; """
    #     expect = "Type mismatch in expression: UnExpr(!, BinExpr(>=, BinExpr(/, BinExpr(+, Id(a), IntegerLit(3)), IntegerLit(4)), IntegerLit(8)))"
    #     self.assertTrue(TestChecker.test(input, expect, 455))  
        
    # def test56(self):
    #     input = """ main1 : function integer (a : integer, b : float) {} main2 : function integer (c : integer, d : float) {} main3 : function integer (e : integer, f : float) {} """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 456))
        
    # def test57(self):
    #     input = """ main : function integer (a : integer, b : float, a : string) {}"""
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 457))
        
    # def test58(self):
    #     input = """ main, b, c : integer ; main : function integer (a : integer, b : float) {}"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 458))
        
    def test59(self):
        input = """ main : function integer (a : integer, b : float) {} x : integer = main() ;"""
        expect = "Type mismatch in expression: FuncCall(main, [])"
        self.assertTrue(TestChecker.test(input, expect, 459))  
        
    def test60(self):
        input = """ main : function integer (a : integer, b : float) {} x : integer = main(1 , 1) ;"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 460))                                                                                                                                                                         