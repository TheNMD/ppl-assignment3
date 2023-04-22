import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test1(self):
        input = """x : integer ; y : integer ; main : function void () {} """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test2(self):
        input = """x : integer = y ; y : integer = 2 ;"""
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test3(self):
        input = """x : auto ;"""
        expect = "Invalid Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test4(self):
        input = """x, y, z : string = "abd", "eex", 5 ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(z, StringType, IntegerLit(5))"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test5(self):
        input = """x, y : integer = 2, x ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test6(self):
        input = """x : string = 22 ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(x, StringType, IntegerLit(22))"
        self.assertTrue(TestChecker.test(input, expect, 406))
        
    def test7(self):
        input = """x, y : string = "22", z ;"""
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test8(self):
        input = """a, b, c, d, e : integer = 2, a, b, c, d ; x, y, z : float = a, b, c ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test9(self):
        input = """a : string ; b : string = a ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test10(self):
        input = """a : integer = 1 + 1.2 ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, IntegerLit(1), FloatLit(1.2)))"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test11(self):
        input = """a : float = 1 + 1.2 ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 411))
        
    def test12(self):
        input = """a : integer = 1.93 + 1.2 ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, FloatLit(1.93), FloatLit(1.2)))"
        self.assertTrue(TestChecker.test(input, expect, 412))
        
    def test13(self):
        input = """a : integer = 1 + 2 + 3 ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
    def test14(self):
        input = """a : integer = 1 + 2 + 3.3 ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), FloatLit(3.3)))"
        self.assertTrue(TestChecker.test(input, expect, 414))
        
    def test15(self):
        input = """a : integer = 1 + 2.2 + 3 ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, BinExpr(+, IntegerLit(1), FloatLit(2.2)), IntegerLit(3)))"
        self.assertTrue(TestChecker.test(input, expect, 415))
    
    def test16(self):
        input = """a : integer = 1 + true ;"""
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker.test(input, expect, 416))
        
    def test17(self):
        input = """a : integer = 1 + 0.9 ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, IntegerLit(1), FloatLit(0.9)))"
        self.assertTrue(TestChecker.test(input, expect, 417))
        
    def test18(self):
        input = """a : integer = 8 % 3 ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
    def test19(self):
        input = """a : integer = 8 % 2.3 ;"""
        expect = "Type mismatch in expression: FloatLit(2.3)"
        self.assertTrue(TestChecker.test(input, expect, 419))
    
    def test20(self):
        input = """a : integer = 8 % 2 ;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 420))
        
    def test21(self):
        input = """a : boolean = true || false || 2 ;"""
        expect = "Type mismatch in expression: IntegerLit(2)"
        self.assertTrue(TestChecker.test(input, expect, 421))
        
    def test22(self):
        input = """a : string = true || false || true ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(||, BinExpr(||, BooleanLit(True), BooleanLit(False)), BooleanLit(True)))"
        self.assertTrue(TestChecker.test(input, expect, 422))
        
    def test23(self):
        input = """a : boolean = true || false || true ;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 423))
        
    def test24(self):
        input = """a, b, c : integer ; d : float = a + b + c ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 424))
        
    def test25(self):
        input = """a, b : integer ; c : string ; d : float = a + b + c ;"""
        expect = "Type mismatch in expression: Id(c)"
        self.assertTrue(TestChecker.test(input, expect, 425))
        
    def test26(self):
        input = """c, b : float ; a : boolean = c == b ;"""
        expect = "Type mismatch in expression: BinExpr(==, Id(c), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 426))
        
    def test27(self):
        input = """ a : integer = 2 == 6 ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(==, IntegerLit(2), IntegerLit(6)))"
        self.assertTrue(TestChecker.test(input, expect, 427))
        
    def test28(self):
        input = """ a : boolean = 2 != false ;"""
        expect = "Type mismatch in expression: BinExpr(!=, IntegerLit(2), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 428))
        
    def test29(self):
        input = """ a : boolean = 3 >= 3.4 ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 429))
        
    def test30(self):
        input = """ b : float ; a : boolean = 3 >= b ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 430))
        
    def test31(self):
        input = """ b : string ; a : boolean = 3 >= b ;"""
        expect = "Type mismatch in expression: Id(b)"
        self.assertTrue(TestChecker.test(input, expect, 431))
        
    def test32(self):
        input = """ a : string = "2" :: "33" ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test33(self):
        input = """ x : string = "223232" ; a : string = "2" :: x ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 433))
        
    def test34(self):
        input = """ x : float = -2.5554 ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 434))
        
    def test35(self):
        input = """ x : float = -2.5554 + 3 + -4.2 ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 435))
        
    def test36(self):
        input = """ x : boolean = !true ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 436))
        
    def test37(self):
        input = """ a : boolean = false ; x : boolean = !a ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 437))
        
    def test38(self):
        input = """ a : string = "false" ; x : boolean = !a ;"""
        expect = "Type mismatch in expression: Id(a)"
        self.assertTrue(TestChecker.test(input, expect, 438))
        
    def test39(self):
        input = """ x : integer ; a : array [3,1] of integer = {{1}, {2}, {x}} ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 439))
        
    def test40(self):
        input = """ x : float ; a : array [1,2] of integer = {1, 2, x} ;"""
        expect = "Illegal array literal: Id(x)"
        self.assertTrue(TestChecker.test(input, expect, 440))
        
    def test41(self):
        input = """ a : array [1,2] of integer = {1, 2, x} ;"""
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 441))
        
    def test42(self):
        input = """ a : array [2,1] of integer = {{1 + 2}, {3 + 4}} ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 442))
        
    def test43(self):
        input = """ a : array [1,2] of integer = {true, 1} ;"""
        expect = "Illegal array literal: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test44(self):
        input = """ x, y : integer ; a : array [2] of integer = {1 + x, 2 * y} ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 444))
        
    def test45(self):
        input = """ x, y : integer ; b : array [2, 3] of integer ; a : array [1,2] of integer = {1 + x, 2 * b} ;"""
        expect = "Type mismatch in expression: Id(b)"
        self.assertTrue(TestChecker.test(input, expect, 445))
        
    def test46(self):
        input = """ a : array [1,2] of integer = {true, true, false} ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([1, 2], IntegerType), ArrayLit([BooleanLit(True), BooleanLit(True), BooleanLit(False)]))"
        self.assertTrue(TestChecker.test(input, expect, 446))
        
    def test47(self):
        input = """ a : array [2, 2] of integer = {{1, 2}, {3, 4}} ; b : integer = a[0] ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayCell(a, [IntegerLit(0)]))"
        self.assertTrue(TestChecker.test(input, expect, 447))
        
    def test48(self):
        input = """ b : integer = a[2] ;"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 448))
        
    def test49(self):
        input = """ a : integer ; b : integer = a[2] ;"""
        expect = "Type mismatch in expression: Id(a)"
        self.assertTrue(TestChecker.test(input, expect, 449))
        
    def test50(self):
        input = """ a : array [1,2] of integer ; b : integer = a[2, 3, 5] ;"""
        expect = "Type mismatch in expression: IntegerLit(5)"
        self.assertTrue(TestChecker.test(input, expect, 450))
        
    def test51(self):
        input = """ a : array [1,2] of integer ; b : integer = a[2.2] ;"""
        expect = "Type mismatch in expression: FloatLit(2.2)"
        self.assertTrue(TestChecker.test(input, expect, 451))
        
    def test52(self):
        input = """ a : array [1,2] of integer ; b : integer = a[1 + 2] ;"""
        expect = "Type mismatch in expression: BinExpr(+, IntegerLit(1), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 452))
        
    def test53(self):
        input = """ a : auto = "false" ; b : auto = a :: "true" ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 453))
        
    def test54(self):
        input = """ main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 454))    
        
    def test55(self):
        input = """ x : auto = {{1.0, 2.2}, {3.9, 2.5}, {3.7, 9.0}} ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 455))
        
    def test56(self):
        input = """ x : auto = 1 + {1, 2, 3}; """
        expect = "Type mismatch in expression: ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 456))
        
    def test57(self):
        input = """ main : function integer () {} """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 457))
        
    def test58(self):
        input = """ main : function void (a : integer) {} """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 458))
        
    def test59(self):
        input = """ arr : array [3, 2] of integer = {{{1}, {2}}, {{2}, {3}}, {{3}, {3, 3}}} ; """
        expect = "Type mismatch in expression: ArrayLit([IntegerLit(3), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 459))
        
    def test60(self):
        input = """ arr : array [3, 2] of integer = {{1, 2}, {2, 3}, {3, 3, 4}} ; """
        expect = "Type mismatch in expression: ArrayLit([IntegerLit(3), IntegerLit(3), IntegerLit(4)])"
        self.assertTrue(TestChecker.test(input, expect, 460))
        
    def test61(self):
        input = """ arr : array [3, 2] of integer = {{1, 2}, {2, 3}, {1.2, 1}} ; """
        expect = "Illegal array literal: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, expect, 461))
        
    def test62(self):
        input = """ arr : array [3, 2] of float = {{1.0, 2.0}, {2.0, 3.0}, {1.2, 1.0}} ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 462))
        
    def test63(self):
        input = """ arr : array [3, 2] of float = {{1.0, 2.0}, {2.0, 3.0}, {1.2, 1.0}} ; a : integer = arr[-1] ;  """
        expect = "Type mismatch in expression: UnExpr(-, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 463))
        
    def test64(self):
        input = """ arr : array [3, 2] of float = {{1.0, 2.0}, {2.0, 3.0}, {1.2, 1.0}} ; a : integer = arr[a + 2 + c] ;  """
        expect = "Type mismatch in expression: BinExpr(+, BinExpr(+, Id(a), IntegerLit(2)), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 464))
        
    def test65(self):
        input = """ a : array [1,2] of integer ; b : integer = a[2, 3, 5] ;"""
        expect = "Type mismatch in expression: IntegerLit(5)"
        self.assertTrue(TestChecker.test(input, expect, 474))
        
    def test66(self):
        input = """ a : array [3,2] of float = {{2.0, 3.0}, {3.0, 4.0}, {5.0, 6.6}} ; b : float = a[0, 1] ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 476))
        
    def test67(self):
        input = """ a : array [3,2] of float = {{2.0, 3.0}, {3.0, 4.0}, {5.0, 6.6}} ; b : integer = a[2, 1] ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayCell(a, [IntegerLit(2), IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 477))
        
    def test68(self):
        input = """ a : array [3] of float = {1.0, 2.0, 6.6} ; b : float = a[2] ; main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 478))
    
    def test69(self):
        input = """ x, y, z : float ; main1 : function integer (a : integer, b : float) {} main2 : function integer (c : integer, d : float) {} main3 : function integer (e : integer, f : float) {} main : function void () {}"""
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 469))
        
    def test70(self):
        input = """  
        a : array [2, 2] of float = {{2.0, 3.6}, {5.0, 9.9}} ;
        main : function void () {
            x : float = a[0, 0] ;
            y : float = a[1, 1] ;
            return ;
        } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 470))
        
    def test71(self):
        input = """
        a : array [2, 2] of float = {{1.0, 2.0}, {3.0, 4.4}} ;  
        func : function integer (a : integer, b : float) {
            a = 2 ;
            c : float ;
            c = a[1, 0] ;
            return ;
        } """
        expect = "Type mismatch in expression: Id(a)"
        self.assertTrue(TestChecker.test(input, expect, 471))
        
    def test72(self):
        input = """ 
        func : function integer (a : auto, b : string) {
            a = {2, 3} ;
            b = func1(1, 2) ;
            return ;
        } 
        func1 : function auto (x : auto, y : auto) {}
        """
        expect = "Type mismatch in statement: ReturnStmt()"
        self.assertTrue(TestChecker.test(input, expect, 472))
        
    def test73(self):
        input = """ 
        func : function integer (a : auto, b : string) {
            a = {2, 3} ;
            c : string = func1(2, 3) ;
            return ;
        } 
        func1 : function auto (x : auto, y : auto) {}
        """
        expect = "Type mismatch in statement: ReturnStmt()"
        self.assertTrue(TestChecker.test(input, expect, 473))
        
    def test74(self):
        input = """
        x : array [2, 2] of float = {{1.0, 2.0}, {3.0, 4.4}} ;  
        b : float = x[0, 0] ;
        func : function auto (a : auto, b : string) {
            c : float ;
            return ;
            }
        main : function void () {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 474))
        
    def test75(self):
        input = """
        x : array [2, 2] of float = {{1.0, 2.0}, {3.0, 4.4}} ;  
        b : float = x[0, 0] ;
        func : function auto (a : auto, b : string) {
            c : float ;
            return ;
            }
        main : function void () {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 475))
        
    def test76(self):
        input = """
        func : function integer (a : integer, b : integer) {
            a = 2 ;
            b = 5 ;
            if (a > b) break ;
            else continue ;
            }
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 476))
        
    def test77(self):
        input = """
        func : function float (a : integer, b : integer) {
                x : integer ;
                return func1(1 ,2) ;
            }
        func1 : function auto (x : integer, y : integer) {}
        main : function void () {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 477))
        
    def test78(self):
        input = """
        func : function float (a : integer, b : integer) {
                x : integer ;
                return func1(1 ,2) ;
            }
        func1 : function auto (x : integer, y : integer) {}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 478))
    
    def test79(self):
        input = """
        func : function float (a : integer, b : integer) {
                func1(1, 2) ;
            }
        func1 : function auto (x : auto, y : auto) {}
        main : function void () {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test80(self):
        input = """
        x, y : integer = 2 , 3 ;
        func : function integer (a : integer, b : integer) {
                    while (1 < 9)
                    {
                        if (x > 20) 
                            {
                                a = 2 ;
                                a = 3 ;
                                break ;
                            }
                        else if (x < 15)
                            {
                                b = 2 ;
                                b = 3 ;
                                continue ;
                            }
                        else
                            {
                                a = 2 ;
                                b = a ;
                                break ;
                            }
                    }
            }
        main : function void () {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 480))
        
    def test81(self):
        input = """
        func : function integer (a : integer, b : auto) {
                while (9 < 10) {
                    if (10 > 90) 
                    { a : integer ;}
                    else if (10 > 90) break ;
                    else if (10 > 90) x = 9 ;
                    else if (10 > 90) continue ;
                    else if (10 > 90) break ;
                    else u = 2 ;
                }
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test82(self):
        input = """
        func : function float (a : integer, b : integer) {
                return 1 ;
                return true ;
                {return 2 ; return 2.2 ;} 
            }
        main : function void () {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 482))
        
    def test83(self):
        input = """
        func : function boolean (inherit a : auto, inherit b : auto) inherit func1 {
                super(1, 2) ;
                return true;
            }
        func1 : function auto (inherit c : auto, inherit d : auto) inherit func2 {
                super(3, 4) ;
                return ;
        }
        func2 : function integer (inherit e : auto, inherit f : auto) inherit func {
                super(5, 6) ;
                return 2;
        }
        main : function void () {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 483))
        
    def test84(self):
        input = """
        x : integer = 2 ;
        y : string = "42" ;
        func : function boolean (inherit a : auto, inherit b : auto) inherit func1 {
                super(x, y) ;
                return true;
            }
        func1 : function auto (inherit out c : auto, inherit out d : auto) {
                return ;
        }
        main : function void () {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test85(self):
        input = """
        x : integer = 2 ;
        y : float = 2.1 ;
        func : function auto (inherit a : auto, inherit b : auto) {
                if (x > y) { return "true" ; return false ; }
                else { return "false" ; return true ; }
                return "yes" ;
                return 2 ;
            }
        main : function void () {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 485))
        
    def test86(self):
        input = """
        x : integer = 2 ;
        y : float = 2.1 ;
        func : function auto (inherit a : auto, inherit b : auto) {
                while (0 != 1)
                {
                    if (x > y)
                    {
                        if (x > y)
                        {
                            if (x > y) break;
                            else
                            {
                                x = 3 ;
                                y = 1.2 ;
                                continue ;
                                x = true ;
                            }
                        }
                        else break ;
                    }
                    else a = c ;
                }
            }
        main : function void () {}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 486))
        
    def test87(self):
        input = """
        x : integer = 2 ;
        y : float = 2.1 ;
        func : function auto (inherit a : auto, inherit b : auto) {
            x = func1(func1(func1(1, 2), func1(1, 2)), func1(func1(1, 2), func1(1, 2))) ;
        }
        func1 : function auto (inherit a : auto, inherit b : auto) {
            return 2 ;
        }
        main : function void () {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 487))
        
    def test88(self):
            input = """
            x : integer = 2 ;
            func : function auto (inherit a : auto, inherit b : auto) {
                x = func1(func1(func1(1.1, 2), func1(3, 4)), func1(func1(5, 6), func1(7, 8))) ;
                return ;
            }
            func1 : function auto (a : auto, b : auto) {
                return 2 ;
            }
            main : function void () {}
            """
            expect = "Type mismatch in expression: FuncCall(func1, [IntegerLit(3), IntegerLit(4)])"
            self.assertTrue(TestChecker.test(input, expect, 488))
            
    def test89(self):
            input = """
            func : function auto (inherit a : auto, inherit b : auto) inherit func1 {
                super(func1(func1(1.1, 2), func1(3, 4))) ;
                return ;
            }
            func1 : function auto (inherit x : auto, y : auto) {
                return 2 ;
            }
            """
            expect = "Type mismatch in expression: FuncCall(func1, [IntegerLit(3), IntegerLit(4)])"
            self.assertTrue(TestChecker.test(input, expect, 489))
            
    def test90(self):
            input = """
            func : function auto (inherit a : auto, inherit b : auto) inherit func1 {
                super(func1(func1(1.1, 2.2), func1(3, 4))) ;
                return ;
            }
            func1 : function auto (inherit x : auto, y : auto) {
                return 2 ;
            }
            main : function void () {}
            """
            expect = "[]"
            self.assertTrue(TestChecker.test(input, expect, 490))
            
    def test91(self):
            input = """
            func : function auto (inherit a : auto, inherit b : auto) inherit func1 {
                super(func1(func1(1.1, 2.2), func1(3, 4))) ;
                x = true ;
                return ;
            }
            func1 : function auto (inherit x : auto, y : auto) {
                return 2 ;
            }
            main : function void () {}
            """
            expect = "Type mismatch in statement: AssignStmt(Id(x), BooleanLit(True))"
            self.assertTrue(TestChecker.test(input, expect, 491))
            
    def test92(self):
            input = """
            func : function auto (inherit a : auto, inherit b : auto) inherit func1 {
                super(func1(func1(1.1, 2.2), func1(3, 4))) ;
                y = true ;
                return ;
            }
            func1 : function auto (inherit x : auto, y : auto) {
                return 2 ;
            }
            main : function void () {}
            """
            expect = "Undeclared Identifier: y"
            self.assertTrue(TestChecker.test(input, expect, 492))
            
    def test93(self):
            input = """
            x : float ;
            func : function auto (inherit a : auto, inherit b : auto) {
                x = func1(func1(func1(1.1, 2), func1(3, 4)), func1(func1(5, 6), func1(7, 8))) ;
                return ;
            }
            func1 : function auto (inherit x : auto, y : auto) {
                return 2 ;
            }
            main : function void () {}
            """
            expect = "Type mismatch in expression: FuncCall(func1, [IntegerLit(3), IntegerLit(4)])"
            self.assertTrue(TestChecker.test(input, expect, 493))
            
    def test94(self):
            input = """
            x : float ;
            func : function auto (inherit a : auto, inherit b : auto) {
                x = func1(func1(func1(1.1, 2.2), func1(3, 4)), func1(func1(5, 6), func1(7, 8))) ;
                return ;
            }
            func1 : function auto (inherit x : auto, y : auto) {
                return 2 ;
            }
            main : function void () {}
            """
            expect = "[]"
            self.assertTrue(TestChecker.test(input, expect, 494))

    def test95(self):
            input = """
            func1 : function float (inherit x : auto, y : auto) {
                return 2 ;
            }
            x : float = func1(func1(func1(1, 2), func1(3, 4)), func1(func1(5, 6), func1(7, 8))) ;
            main : function void () {}
            """
            expect = "Type mismatch in expression: FuncCall(func1, [IntegerLit(1), IntegerLit(2)])"
            self.assertTrue(TestChecker.test(input, expect, 495))
            
    def test96(self):
        input = """
        func1 : function auto (inherit x : auto, y : auto) {
            return 2 ;
        }
        x : float = func1(func1(func1(1, 2), func1(3, 4)), func1(func1(5, 6), func1(7, 8))) ;
        main : function void () {}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 496))
        
    def test97(self):
        input = """
        func1 : function auto (inherit x : auto, y : auto) {
            return 2 ;
        }
        x : float = func1(func1(func1(1, "2"), func1(3, 4)), func1(func1(5, 6), func1(7, 8))) ;
        main : function void () {}
        """
        expect = "Type mismatch in expression: IntegerLit(4)"
        self.assertTrue(TestChecker.test(input, expect, 497))
        
    def test98(self):
        input = """
        func1 : function auto (inherit x : auto, y : auto) {
            return 2 ;
        }
        x : float = func1(func1(func1(1, "2"), func1(3, "4")), func1(func1(5, 6), func1(7, 8))) ;
        main : function void () {}
        """
        expect = "Type mismatch in expression: FuncCall(func1, [IntegerLit(3), StringLit(4)])"
        self.assertTrue(TestChecker.test(input, expect, 498))
        
    def test99(self):
        input = """
        func1 : function auto (inherit x : auto, y : auto) {
            return "2" ;
        }
        a: string ;
        x : float = func1(func1(func1("1", "2"), func1("3", "4")), func1(func1(a, "6"), func1(7, 8))) ;
        main : function void () {}
        """
        expect = "Type mismatch in expression: IntegerLit(7)"
        self.assertTrue(TestChecker.test(input, expect, 499))
        
    def test100(self):
        input = """
            func : function auto (x : auto, y : auto) inherit func1 {
                return ;
            }
            func1 : function auto (inherit x : auto, y : auto) {
                return 2 ;
            }
            main : function void () {}
            """
        expect = "Invalid statement in function: func"
        self.assertTrue(TestChecker.test(input, expect, 500))

                                                                                                            