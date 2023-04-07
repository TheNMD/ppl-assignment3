import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test1(self):
        input = """x,y,z,a,b,c: array [1,2,3] of integer; a,b,c: array [4,6,7] of float;"""
        expect = """Program([
	VarDecl(x, ArrayType([1, 2, 3], IntegerType))
	VarDecl(y, ArrayType([1, 2, 3], IntegerType))
	VarDecl(z, ArrayType([1, 2, 3], IntegerType))
	VarDecl(a, ArrayType([1, 2, 3], IntegerType))
	VarDecl(b, ArrayType([1, 2, 3], IntegerType))
	VarDecl(c, ArrayType([1, 2, 3], IntegerType))
	VarDecl(a, ArrayType([4, 6, 7], FloatType))
	VarDecl(b, ArrayType([4, 6, 7], FloatType))
	VarDecl(c, ArrayType([4, 6, 7], FloatType))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test2(self):
        input = """a, b, c: array[3,4] of integer = {1,2,3}, {}, {};"""
        expect = """Program([
	VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(b, ArrayType([3, 4], IntegerType), ArrayLit([]))
	VarDecl(c, ArrayType([3, 4], IntegerType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test3(self):
        input = """x, y, z: float = 1.2, 3e12, 1_33.33e-23;"""
        expect = """Program([
	VarDecl(x, FloatType, FloatLit(1.2))
	VarDecl(y, FloatType, FloatLit(3000000000000.0))
	VarDecl(z, FloatType, FloatLit(1.3333e-21))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test4(self):
        input = """x, y, z: boolean = true, false, true;"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	VarDecl(y, BooleanType, BooleanLit(False))
	VarDecl(z, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))
        
    def test5(self):
        input = """x, y : integer = func(1,2,3), func1() ;"""
        expect = """Program([
	VarDecl(x, IntegerType, FuncCall(func, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(y, IntegerType, FuncCall(func1, []))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test6(self):
        input = """x, y : integer = arr[0, 1, 2], arr1[4, 5, 6] ;"""
        expect = """Program([
	VarDecl(x, IntegerType, ArrayCell(arr, [IntegerLit(0), IntegerLit(1), IntegerLit(2)]))
	VarDecl(y, IntegerType, ArrayCell(arr1, [IntegerLit(4), IntegerLit(5), IntegerLit(6)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
        
    def test7(self):
        input = """x, y : integer = a, b ;"""
        expect = """Program([
	VarDecl(x, IntegerType, Id(a))
	VarDecl(y, IntegerType, Id(b))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
 
    def test8(self):
        input = """x : string = "abc" ;"""
        expect = """Program([
	VarDecl(x, StringType, StringLit(abc))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
 
    def test9(self):
        input = """x : string = ("abc"::"cde")::"xyz" ;"""
        expect = """Program([
	VarDecl(x, StringType, BinExpr(::, BinExpr(::, StringLit(abc), StringLit(cde)), StringLit(xyz)))
])"""
        self.assertTrue(TestAST.test(input, expect, 309)) 
  
    def test10(self):
        input = """x : boolean = (a == 9) > (5 == 8) ;"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(>, BinExpr(==, Id(a), IntegerLit(9)), BinExpr(==, IntegerLit(5), IntegerLit(8))))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
         
    def test11(self):
        input = """x : boolean = a || b || c || d && e ;"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(&&, BinExpr(||, BinExpr(||, BinExpr(||, Id(a), Id(b)), Id(c)), Id(d)), Id(e)))
])"""
        self.assertTrue(TestAST.test(input, expect, 311)) 
  
    def test12(self):
        input = """x : float = 1 * a - 2.33e-32 / 33 + b % 33;"""
        expect = """Program([
	VarDecl(x, FloatType, BinExpr(+, BinExpr(-, BinExpr(*, IntegerLit(1), Id(a)), BinExpr(/, FloatLit(2.33e-32), IntegerLit(33))), BinExpr(%, Id(b), IntegerLit(33))))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))   
 
    def test13(self):
        input = """a,b,c: array[3,4,5] of integer = {},{{},{}}, {{{},{}},{}};"""
        expect = """Program([
	VarDecl(a, ArrayType([3, 4, 5], IntegerType), ArrayLit([]))
	VarDecl(b, ArrayType([3, 4, 5], IntegerType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(c, ArrayType([3, 4, 5], IntegerType), ArrayLit([ArrayLit([ArrayLit([]), ArrayLit([])]), ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))    
  
    def test14(self):
        input = """a,b,c: array[3,4,5] of integer = {1,2,3},{{1,2},{3,4}}, {{{1,22},{33,4}},{77,88}};"""
        expect = """Program([
	VarDecl(a, ArrayType([3, 4, 5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(b, ArrayType([3, 4, 5], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)])]))
	VarDecl(c, ArrayType([3, 4, 5], IntegerType), ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(22)]), ArrayLit([IntegerLit(33), IntegerLit(4)])]), ArrayLit([IntegerLit(77), IntegerLit(88)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314)) 
  
    def test15(self):
        """Simple program"""
        input = """main: function void () {
                
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
        
    def test16(self):
        """Simple program"""
        input = """main: function void (inherit a : integer, out b : float, inherit out c : boolean) {
                int1: integer = a + b / c;
                int2: integer = 1 + 3 - 8 ;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [InheritParam(a, IntegerType), OutParam(b, FloatType), InheritOutParam(c, BooleanType)], None, BlockStmt([VarDecl(int1, IntegerType, BinExpr(+, Id(a), BinExpr(/, Id(b), Id(c)))), VarDecl(int2, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(3)), IntegerLit(8)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test17(self):
        """Simple program"""
        input = """main: function void () {
                if (a == 9) b = 7 ;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(9)), AssignStmt(Id(b), IntegerLit(7)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
        
    def test18(self):
        """Simple program"""
        input = """main: function void () {
                if (a == 9) b = 7 ;
                else if (c == 9) b = 5 ;
                else b = 20 ;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(9)), AssignStmt(Id(b), IntegerLit(7)), IfStmt(BinExpr(==, Id(c), IntegerLit(9)), AssignStmt(Id(b), IntegerLit(5)), AssignStmt(Id(b), IntegerLit(20))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test19(self):
        """Simple program"""
        input = """foo: function void (inherit a: integer, inherit out b: float) inherit bar {}
        main: function void () {
        {

        }
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test20(self):
        """Simple program"""
        input = """main: function void () {
                if (a == 9)
                {
                        for (i = 5, i < 10, i + 1) a = a + i;
                }
                else if (c == 9)
                {
                        i : integer = 23 ;
                        while (i < 5) i = i + 1 ;
                }
                else b = 20 ;
                return ;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(9)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(5)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(a), BinExpr(+, Id(a), Id(i))))]), IfStmt(BinExpr(==, Id(c), IntegerLit(9)), BlockStmt([VarDecl(i, IntegerType, IntegerLit(23)), WhileStmt(BinExpr(<, Id(i), IntegerLit(5)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))]), AssignStmt(Id(b), IntegerLit(20)))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test21(self):
        """More complex program"""
        input = """main: function void (a : array [1,2] of integer, b : string) {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, ArrayType([1, 2], IntegerType)), Param(b, StringType)], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
        
    def test22(self):
        """More complex program"""
        input = """main: function array [2,3] of string () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, ArrayType([2, 3], StringType), [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))
        
    def test23(self):
        """More complex program"""
        input = """func1 : function auto (out a : array [3,8] of integer, inherit b : float) {
            randfloat : float = 1_332.33e-23 ;
            randarr : array [7] of string ;
            return 2233;
            }
        func2 : function void (c : string, out d : array [2,3] of boolean) inherit func1 {
            if(a == 5) c = a % 7 ;
            else d = a / 8 ;
            randarr = arr1[1+1,3_3/3,5%4] + 332 - arr2[9/3]  ;
            return;
            }"""
        expect = """Program([
	FuncDecl(func1, AutoType, [OutParam(a, ArrayType([3, 8], IntegerType)), InheritParam(b, FloatType)], None, BlockStmt([VarDecl(randfloat, FloatType, FloatLit(1.33233e-20)), VarDecl(randarr, ArrayType([7], StringType)), ReturnStmt(IntegerLit(2233))]))
	FuncDecl(func2, VoidType, [Param(c, StringType), OutParam(d, ArrayType([2, 3], BooleanType))], func1, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(7))), AssignStmt(Id(d), BinExpr(/, Id(a), IntegerLit(8)))), AssignStmt(Id(randarr), BinExpr(-, BinExpr(+, ArrayCell(arr1, [BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(/, IntegerLit(33), IntegerLit(3)), BinExpr(%, IntegerLit(5), IntegerLit(4))]), IntegerLit(332)), ArrayCell(arr2, [BinExpr(/, IntegerLit(9), IntegerLit(3))]))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
        
    def test24(self):
        """More complex program"""
        input = """func1 : function float (c : string, out d : boolean) {
            if(a == 5) c = a % 7 ;
            else if (a == 4) for (i = 8, i < 20, i / 2) { c = c + 1 ; }
            return 1.223e20 ;
            }"""
        expect = """Program([
	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(7))), IfStmt(BinExpr(==, Id(a), IntegerLit(4)), ForStmt(AssignStmt(Id(i), IntegerLit(8)), BinExpr(<, Id(i), IntegerLit(20)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))])))), ReturnStmt(FloatLit(1.223e+20))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
        
    def test25(self):
        """More complex program"""
        input = """func1 : function float (c : string, out d : boolean) {
            if(a == 7) c = a % 7 ;
            else while (i < 20) { c = c + 1 ; }
            }"""
        expect = """Program([
	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(7)), AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(7))), WhileStmt(BinExpr(<, Id(i), IntegerLit(20)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test26(self):
        """More complex program"""
        input = """func1 : function float (c : string, out d : boolean) {
                arr1, arr2, arr3 : array [2,2,2_3] of boolean = {}, {{},{}}, {{{{{}}}}} ;
            }"""
        expect = """Program([
	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([VarDecl(arr1, ArrayType([2, 2, 23], BooleanType), ArrayLit([])), VarDecl(arr2, ArrayType([2, 2, 23], BooleanType), ArrayLit([ArrayLit([]), ArrayLit([])])), VarDecl(arr3, ArrayType([2, 2, 23], BooleanType), ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
        
    def test27(self):
        """More complex program"""
        input = """res : float = sin(a,b) / cos(c,d) ;"""
        expect = """Program([
	VarDecl(res, FloatType, BinExpr(/, FuncCall(sin, [Id(a), Id(b)]), FuncCall(cos, [Id(c), Id(d)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
        
    def test28(self):
        """More complex program"""
        input = """main1 : function string () {
            do {a = a / 9 ;}
            while (a > 100) ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(a), IntegerLit(100)), BlockStmt([AssignStmt(Id(a), BinExpr(/, Id(a), IntegerLit(9)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
        
    def test29(self):
        """More complex program"""
        input = """main1 : function string () {
            bool = "abc\\t" != "abc\t" ;
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(bool), BinExpr(!=, StringLit(abc\\t), StringLit(abc	))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
        
    def test30(self):
        """More complex program"""
        input = """main1 : function string () {
            while(a < 23)
            do {a = a / 9 ;}
            while (a > 100) ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(23)), DoWhileStmt(BinExpr(>, Id(a), IntegerLit(100)), BlockStmt([AssignStmt(Id(a), BinExpr(/, Id(a), IntegerLit(9)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
        
    def test31(self):
        """More complex program"""
        input = """main1 : function string () {
            bool = 7 - 9 < 4 - 6 ;
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(bool), BinExpr(<, BinExpr(-, IntegerLit(7), IntegerLit(9)), BinExpr(-, IntegerLit(4), IntegerLit(6)))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))
        
    def test32(self):
        """More complex program"""
        input = """main1 : function string () {
            str = 7 - 9 * 4 - 6 ;
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(str), BinExpr(-, BinExpr(-, IntegerLit(7), BinExpr(*, IntegerLit(9), IntegerLit(4))), IntegerLit(6))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test33(self):
        """More complex program"""
        input = """main1 : function string () {
            str = (8 < 9) || (4 > 6) ;
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(str), BinExpr(||, BinExpr(<, IntegerLit(8), IntegerLit(9)), BinExpr(>, IntegerLit(4), IntegerLit(6)))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
        
    def test34(self):
        """More complex program"""
        input = """main1 : function string () {
            bool = ((1 < 2) < 3) < 4 ;
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(bool), BinExpr(<, BinExpr(<, BinExpr(<, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
        
    def test35(self):
        """More complex program"""
        input = """main1 : function string () {
            str = (("abc" :: "cde") :: "123") :: "456" ;
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(str), BinExpr(::, BinExpr(::, BinExpr(::, StringLit(abc), StringLit(cde)), StringLit(123)), StringLit(456))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
        
    def test36(self):
        """More complex program"""
        input = """ a : string = "213123213\\'" ;  """
        expect = """Program([
	VarDecl(a, StringType, StringLit(213123213\\'))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
        
    def test37(self):
        """More complex program"""
        input = """_A330xr : integer ;"""
        expect = """Program([
	VarDecl(_A330xr, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
        
    def test38(self):
        """More complex program"""
        input = """str : string = "\ttoo(;_;)many(;_;)test(;_;)cases(;_;)\t" ;"""
        expect = """Program([
	VarDecl(str, StringType, StringLit(	too(;_;)many(;_;)test(;_;)cases(;_;)	))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
        
    def test39(self):
        """More complex program"""
        input = """main1 : function array [2,2] of string (inherit a : array [2,3] of string, out b : array [3,3] of boolean) {
            while(a < 23)
            do {a = a / 9 ;}
            while (a > 100) ;
            }"""
        expect = """Program([
	FuncDecl(main1, ArrayType([2, 2], StringType), [InheritParam(a, ArrayType([2, 3], StringType)), OutParam(b, ArrayType([3, 3], BooleanType))], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(23)), DoWhileStmt(BinExpr(>, Id(a), IntegerLit(100)), BlockStmt([AssignStmt(Id(a), BinExpr(/, Id(a), IntegerLit(9)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
        
    def test40(self):
        """More complex program"""
        input = """main1 : function array [2,2] of string () {
                if(a < 4)
                {
                        while(a < 23)
                        {
                                for (i = 8, i < 20, i / 2) {c = c + 1 ; }
                        }
                }
                return; 
            }"""
        expect = """Program([
	FuncDecl(main1, ArrayType([2, 2], StringType), [], None, BlockStmt([IfStmt(BinExpr(<, Id(a), IntegerLit(4)), BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(23)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(8)), BinExpr(<, Id(i), IntegerLit(20)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))]))]))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))
        
    def test41(self):
        """More complex program"""
        input = """main1 : function array [2,2] of string () {
                return 0;
                return;
                return 1; 
            }"""
        expect = """Program([
	FuncDecl(main1, ArrayType([2, 2], StringType), [], None, BlockStmt([ReturnStmt(IntegerLit(0)), ReturnStmt(), ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))
        
    def test42(self):
        """More complex program"""
        input = """func1 : function void (c : string, out d : boolean) {
                printInteger(a);
                readInteger();
            }"""
        expect = """Program([
	FuncDecl(func1, VoidType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([CallStmt(printInteger, Id(a)), CallStmt(readInteger, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test43(self):
        """More complex program"""
        input = """func1 : function void (c : string, out d : boolean) {
                writeFloat(a);
                readFloat();
                printBoolean(a);
                readBoolean();
                printString(a);
                readString();
                preventDefault();
                super(b);
            }"""
        expect = """Program([
	FuncDecl(func1, VoidType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([CallStmt(writeFloat, Id(a)), CallStmt(readFloat, ), CallStmt(printBoolean, Id(a)), CallStmt(readBoolean, ), CallStmt(printString, Id(a)), CallStmt(readString, ), CallStmt(preventDefault, ), CallStmt(super, Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))
        
    def test44(self):
        """More complex program"""
        input = """func1 : function void (c : string, out d : boolean) { 
            do { for (i = 7, i < 13, i + 1) printInteger(i) ; }
            while (True) ;
            }"""
        expect = """Program([
	FuncDecl(func1, VoidType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([DoWhileStmt(Id(True), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(7)), BinExpr(<, Id(i), IntegerLit(13)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printInteger, Id(i)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))
        
    def test45(self):
        """More complex program"""
        input = """func1 : function float (c : string, out d : boolean) {
            a,b,c : integer = 1,2,3 ;
            }"""
        expect = """Program([
	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType, IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))
        
    def test46(self):
        """More complex program"""
        input = """a,b,c : array [2_7,3] of float = 1,2,3 ;"""
        expect = """Program([
	VarDecl(a, ArrayType([27, 3], FloatType), IntegerLit(1))
	VarDecl(b, ArrayType([27, 3], FloatType), IntegerLit(2))
	VarDecl(c, ArrayType([27, 3], FloatType), IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
        
    def test47(self):
        """More complex program"""
        input = """randfloat,b : float = 1_332.33e-23,.332e3 ;"""
        expect = """Program([
	VarDecl(randfloat, FloatType, FloatLit(1.33233e-20))
	VarDecl(b, FloatType, FloatLit(332.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))
        
    def test48(self):
        """More complex program"""
        input = """abc : string = "ddxxdw"::"eerxxz" ; """
        expect = """Program([
	VarDecl(abc, StringType, BinExpr(::, StringLit(ddxxdw), StringLit(eerxxz)))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))
        
    def test49(self):
        """More complex program"""
        input = """abc : float = a[22,3] / b[8-8,9/3] % c[8%2, 1*7] ; """
        expect = """Program([
	VarDecl(abc, FloatType, BinExpr(%, BinExpr(/, ArrayCell(a, [IntegerLit(22), IntegerLit(3)]), ArrayCell(b, [BinExpr(-, IntegerLit(8), IntegerLit(8)), BinExpr(/, IntegerLit(9), IntegerLit(3))])), ArrayCell(c, [BinExpr(%, IntegerLit(8), IntegerLit(2)), BinExpr(*, IntegerLit(1), IntegerLit(7))])))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
        
    def test50(self):
        """More complex program"""
        input = """abc, cde : float = a[22,3] / b[8-8,9/3] % c[8%2, 1*7], abc ; """
        expect = """Program([
	VarDecl(abc, FloatType, BinExpr(%, BinExpr(/, ArrayCell(a, [IntegerLit(22), IntegerLit(3)]), ArrayCell(b, [BinExpr(-, IntegerLit(8), IntegerLit(8)), BinExpr(/, IntegerLit(9), IntegerLit(3))])), ArrayCell(c, [BinExpr(%, IntegerLit(8), IntegerLit(2)), BinExpr(*, IntegerLit(1), IntegerLit(7))])))
	VarDecl(cde, FloatType, Id(abc))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
        
    def test51(self):
        """More complex program"""
        input = """main1 : function string () {
            for (i = k, i != 50, increase(i)) printInteger(i) ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), Id(k)), BinExpr(!=, Id(i), IntegerLit(50)), FuncCall(increase, [Id(i)]), CallStmt(printInteger, Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
        
    def test52(self):
        """More complex program"""
        input = """main1 : function string () { arr : array [2,3] of integer = {a,b,func(c,d,e)} ; }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([VarDecl(arr, ArrayType([2, 3], IntegerType), ArrayLit([Id(a), Id(b), FuncCall(func, [Id(c), Id(d), Id(e)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test53(self):
        """More complex program"""
        input = """main1 : function string () { return {a,b,func(c,d,e)} ; }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([ReturnStmt(ArrayLit([Id(a), Id(b), FuncCall(func, [Id(c), Id(d), Id(e)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))
        
    def test54(self):
        """More complex program"""
        input = """main1 : function string () { return arr[.22/17, 11e3, 7_2.04] ; }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([ReturnStmt(ArrayCell(arr, [BinExpr(/, FloatLit(0.22), IntegerLit(17)), FloatLit(11000.0), FloatLit(72.04)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
        
    def test55(self):
        """More complex program"""
        input = """main1 : function string () { {} {} {{}{}} return; }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([BlockStmt([]), BlockStmt([]), BlockStmt([BlockStmt([]), BlockStmt([])]), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))
        
    def test56(self):
        """More complex program"""
        input = """main1 : function string () {
            if (a < 5) 
                if (b < 5) 
                    if (c < 5) d = 5 ; 
                    else e = 5 ; 
                else f = 5 ; 
            else g = 5 ; 
}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([IfStmt(BinExpr(<, Id(a), IntegerLit(5)), IfStmt(BinExpr(<, Id(b), IntegerLit(5)), IfStmt(BinExpr(<, Id(c), IntegerLit(5)), AssignStmt(Id(d), IntegerLit(5)), AssignStmt(Id(e), IntegerLit(5))), AssignStmt(Id(f), IntegerLit(5))), AssignStmt(Id(g), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
        
    def test57(self):
        """More complex program"""
        input = """main1 : function string () {
            if (a < 5) 
                if (b < 5) 
                    if (c < 5) d = 5 ; 
                    else if (true) e = 5 ; 
                else if (true) f = 5 ; 
            else if (false) g = 5 ; 
}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([IfStmt(BinExpr(<, Id(a), IntegerLit(5)), IfStmt(BinExpr(<, Id(b), IntegerLit(5)), IfStmt(BinExpr(<, Id(c), IntegerLit(5)), AssignStmt(Id(d), IntegerLit(5)), IfStmt(BooleanLit(True), AssignStmt(Id(e), IntegerLit(5)), IfStmt(BooleanLit(True), AssignStmt(Id(f), IntegerLit(5)), IfStmt(BooleanLit(False), AssignStmt(Id(g), IntegerLit(5))))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))
        
    def test58(self):
        """More complex program"""
        input = """main1 : function string () { res = 10 + ----func2(22) ; }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(res), BinExpr(+, IntegerLit(10), UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, FuncCall(func2, [IntegerLit(22)])))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))
        
    def test59(self):
        """More complex program"""
        input = """main1 : function string () { res = true && !!!!func2(22) ; }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(res), BinExpr(&&, BooleanLit(True), UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, FuncCall(func2, [IntegerLit(22)])))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
        
    def test60(self):
        """More complex program"""
        input = """main1 : function string () { res = 3 > !!--func2(22) ; }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(res), BinExpr(>, IntegerLit(3), UnExpr(!, UnExpr(!, UnExpr(-, UnExpr(-, FuncCall(func2, [IntegerLit(22)])))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))
        
    def test61(self):
        """More complex program"""
        input = """main1 : function string () {} main2 : function boolean () inherit main1 {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
	FuncDecl(main2, BooleanType, [], main1, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))
        
    def test62(self):
        """More complex program"""
        input = """main1 : function string () {
            for(i = 0, i < 20, i + 1)
            {
                if(i % 6 == 3) continue ;
                else if (i == 18) break ;
            }
            return;
        }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(20)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(6)), IntegerLit(3)), ContinueStmt(), IfStmt(BinExpr(==, Id(i), IntegerLit(18)), BreakStmt()))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test63(self):
        """More complex program"""
        input = """boo1,boo2,boo3 : boolean = true,false,false||true ;"""
        expect = """Program([
	VarDecl(boo1, BooleanType, BooleanLit(True))
	VarDecl(boo2, BooleanType, BooleanLit(False))
	VarDecl(boo3, BooleanType, BinExpr(||, BooleanLit(False), BooleanLit(True)))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))
        
    def test64(self):
        """More complex program"""
        input = """func1 : function integer (c : string, out d : boolean) {
            for(i = 0, i < 100, i + 1)
                for(j = i, j < 100, j + 1)
                    if(arr[i,j] == true) return 220 ;
            return int1 ;
            }"""
        expect = """Program([
	FuncDecl(func1, IntegerType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), Id(i)), BinExpr(<, Id(j), IntegerLit(100)), BinExpr(+, Id(j), IntegerLit(1)), IfStmt(BinExpr(==, ArrayCell(arr, [Id(i), Id(j)]), BooleanLit(True)), ReturnStmt(IntegerLit(220))))), ReturnStmt(Id(int1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))
        
    def test65(self):
        """More complex program"""
        input = """func1 : function integer (c : string, out d : boolean) {
            int1 : array [2,2] of integer = {{-9 + 7 * 122, 9 - -9},{a[3] * 7, caltrand(2, b, 5)}} ; 
            return int1 ;
            }"""
        expect = """Program([
	FuncDecl(func1, IntegerType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([VarDecl(int1, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([BinExpr(+, UnExpr(-, IntegerLit(9)), BinExpr(*, IntegerLit(7), IntegerLit(122))), BinExpr(-, IntegerLit(9), UnExpr(-, IntegerLit(9)))]), ArrayLit([BinExpr(*, ArrayCell(a, [IntegerLit(3)]), IntegerLit(7)), FuncCall(caltrand, [IntegerLit(2), Id(b), IntegerLit(5)])])])), ReturnStmt(Id(int1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))
        
    def test66(self):
        """More complex program"""
        input = """func1 : function integer (c : string, out d : boolean) {
            int1 : integer = -9 + 7 * 122 ; 
            return int1 ;
        }"""
        expect = """Program([
	FuncDecl(func1, IntegerType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([VarDecl(int1, IntegerType, BinExpr(+, UnExpr(-, IntegerLit(9)), BinExpr(*, IntegerLit(7), IntegerLit(122)))), ReturnStmt(Id(int1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))
        
    def test67(self):
        """More complex program"""
        input = """func1 : function float (c : string, out d : boolean) {
            boo1 : boolean = !abc[2] && cde[0,1] ; 
            return boo1 ;
        }"""
        expect = """Program([
	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([VarDecl(boo1, BooleanType, BinExpr(&&, UnExpr(!, ArrayCell(abc, [IntegerLit(2)])), ArrayCell(cde, [IntegerLit(0), IntegerLit(1)]))), ReturnStmt(Id(boo1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))
        
    def test68(self):
        """More complex program"""
        input = """boolrand : boolean = (a > b) || (c != d) || (x % 2 == 0) && false ;"""
        expect = """Program([
	VarDecl(boolrand, BooleanType, BinExpr(&&, BinExpr(||, BinExpr(||, BinExpr(>, Id(a), Id(b)), BinExpr(!=, Id(c), Id(d))), BinExpr(==, BinExpr(%, Id(x), IntegerLit(2)), IntegerLit(0))), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))
        
    def test69(self):
        """More complex program"""
        input = """main1 : function string () {
                {
                    {
                        {
                            {
                                return "123" :: "abc\t\\t" ;
                            }
                        }   
                    }
                }
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([ReturnStmt(BinExpr(::, StringLit(123), StringLit(abc	\\t)))])])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))
        
    def test70(self):
        """More complex program"""
        input = """main1 : function string () {
            if(true)
                {
                    b : integer = 788 ;
                    for (i = 2, i < randint, i - 1) if(i == -2) return i ;
                }
            else
                {
                    c : float = 788.33e-23 ;
                    do { if(j > -9) { j = j + 1 ; } } 
                    while (j < 20);
                }
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([VarDecl(b, IntegerType, IntegerLit(788)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), Id(randint)), BinExpr(-, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(i), UnExpr(-, IntegerLit(2))), ReturnStmt(Id(i))))]), BlockStmt([VarDecl(c, FloatType, FloatLit(7.8833e-21)), DoWhileStmt(BinExpr(<, Id(j), IntegerLit(20)), BlockStmt([IfStmt(BinExpr(>, Id(j), UnExpr(-, IntegerLit(9))), BlockStmt([AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))
        
    def test71(self):
        """More complex program"""
        input = """str : string = "{c}Y4enROD$$$!h%-~~V{9p>kXS6Ib>05" ;"""
        expect = """Program([
	VarDecl(str, StringType, StringLit({c}Y4enROD$$$!h%-~~V{9p>kXS6Ib>05))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))
        
    def test72(self):
        """More complex program"""
        input = """func1 : function string (inherit c : string, inherit out d : string) {
            a : string = (c :: d) :: "abc" ;
            }"""
        expect = """Program([
	FuncDecl(func1, StringType, [InheritParam(c, StringType), InheritOutParam(d, StringType)], None, BlockStmt([VarDecl(a, StringType, BinExpr(::, BinExpr(::, Id(c), Id(d)), StringLit(abc)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test73(self):
        """More complex program"""
        input = """func1 : function string (inherit c : string, inherit out d : string) {
            temp : integer = 0 ;
            for (i = 0, i < 10, i + 1) 
            {
                if (i % 2) temp = temp + i ;
                else temp = temp + 1 ;
            }
            return temp ;
        }"""
        expect = """Program([
	FuncDecl(func1, StringType, [InheritParam(c, StringType), InheritOutParam(d, StringType)], None, BlockStmt([VarDecl(temp, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(%, Id(i), IntegerLit(2)), AssignStmt(Id(temp), BinExpr(+, Id(temp), Id(i))), AssignStmt(Id(temp), BinExpr(+, Id(temp), IntegerLit(1))))])), ReturnStmt(Id(temp))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))
        
    def test74(self):
        """More complex program"""
        input = """func1 : function string (inherit c : string, inherit out d : string) {
            temp : integer = 0 ;
            return ftemp ;
            }
            func2 : function float (a : integer, out b : integer) {
            return func1(2,3,5) ;   
        }"""
        expect = """Program([
	FuncDecl(func1, StringType, [InheritParam(c, StringType), InheritOutParam(d, StringType)], None, BlockStmt([VarDecl(temp, IntegerType, IntegerLit(0)), ReturnStmt(Id(ftemp))]))
	FuncDecl(func2, FloatType, [Param(a, IntegerType), OutParam(b, IntegerType)], None, BlockStmt([ReturnStmt(FuncCall(func1, [IntegerLit(2), IntegerLit(3), IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))
        
    def test75(self):
        """More complex program"""
        input = """ int1 : integer = randfunc("yes",false,8_6, 9 / 2,b,arr[4,5,8%2]) ;"""
        expect = """Program([
	VarDecl(int1, IntegerType, FuncCall(randfunc, [StringLit(yes), BooleanLit(False), IntegerLit(86), BinExpr(/, IntegerLit(9), IntegerLit(2)), Id(b), ArrayCell(arr, [IntegerLit(4), IntegerLit(5), BinExpr(%, IntegerLit(8), IntegerLit(2))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))
        
    def test76(self):
        """More complex program"""
        input = """int1 : integer = randfunc({},{{}},{{},{}}) ;"""
        expect = """Program([
	VarDecl(int1, IntegerType, FuncCall(randfunc, [ArrayLit([]), ArrayLit([ArrayLit([])]), ArrayLit([ArrayLit([]), ArrayLit([])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))
        
    def test77(self):
        """More complex program"""
        input = """int1 : integer = randfunc(randfunc1(),randfunc2(1,2),randfunc3(rand(5))) ;"""
        expect = """Program([
	VarDecl(int1, IntegerType, FuncCall(randfunc, [FuncCall(randfunc1, []), FuncCall(randfunc2, [IntegerLit(1), IntegerLit(2)]), FuncCall(randfunc3, [FuncCall(rand, [IntegerLit(5)])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))
        
    def test78(self):
        """More complex program"""
        input = """func1: function void()
                    {
                        {
                            {
                                {
                                    arr: array[5] of integer;
                                    return arr ;
                                }
                            }
                        }
                    }"""
        expect = """Program([
	FuncDecl(func1, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([BlockStmt([VarDecl(arr, ArrayType([5], IntegerType)), ReturnStmt(Id(arr))])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))
        
    def test79(self):
        """More complex program"""
        input = """ a : string  = -234 - s / f / 20;
                    b : float = !8 - -10.1 + !32e-32; """
        expect = """Program([
	VarDecl(a, StringType, BinExpr(-, UnExpr(-, IntegerLit(234)), BinExpr(/, BinExpr(/, Id(s), Id(f)), IntegerLit(20))))
	VarDecl(b, FloatType, BinExpr(+, BinExpr(-, UnExpr(!, IntegerLit(8)), UnExpr(-, FloatLit(10.1))), UnExpr(!, FloatLit(3.2e-31))))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))
        
    def test80(self):
        """More complex program"""
        input = """main1 : function string () { _a : integer = __9b ; }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([VarDecl(_a, IntegerType, Id(__9b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))
        
    def test81(self):
        """More complex program"""
        input = """ _a : integer = __9b ; """
        expect = """Program([
	VarDecl(_a, IntegerType, Id(__9b))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))
        
    def test82(self):
        """More complex program"""
        input = """main1 : function auto () {
            do 
                {                
                    while (b < 100)
                        do {}
                        while (c == 100) ;
                }
            while (a > 100) ;
        }"""
        expect = """Program([
	FuncDecl(main1, AutoType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(a), IntegerLit(100)), BlockStmt([WhileStmt(BinExpr(<, Id(b), IntegerLit(100)), DoWhileStmt(BinExpr(==, Id(c), IntegerLit(100)), BlockStmt([])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test83(self):
        """More complex program"""
        input = """main1 : function auto () {
            for (i = 100, i < 100, i + 1)
                for (j = i, j < 1000, j + 1)
                    if (arr[i,j,i+j]) return 1;
                    else return 0 ;
        }"""
        expect = """Program([
	FuncDecl(main1, AutoType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(100)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), Id(i)), BinExpr(<, Id(j), IntegerLit(1000)), BinExpr(+, Id(j), IntegerLit(1)), IfStmt(ArrayCell(arr, [Id(i), Id(j), BinExpr(+, Id(i), Id(j))]), ReturnStmt(IntegerLit(1)), ReturnStmt(IntegerLit(0)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))
        
    def test84(self):
        """More complex program"""
        input = """int1 : integer = (((7 - 9))) * ((8)) - b[2,3,4] ; """
        expect = """Program([
	VarDecl(int1, IntegerType, BinExpr(-, BinExpr(*, BinExpr(-, IntegerLit(7), IntegerLit(9)), IntegerLit(8)), ArrayCell(b, [IntegerLit(2), IntegerLit(3), IntegerLit(4)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))
        
    def test85(self):
        """More complex program"""
        input = """func1 : function float (c : string, out d : boolean) {
            if(a == 5) c = a % 7 ;
            else if (a == 4) for (i = 8, i < 20, i / 2) {c = c + 1 ; }
            return 1.223e20 ;
            }"""
        expect = """Program([
	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(7))), IfStmt(BinExpr(==, Id(a), IntegerLit(4)), ForStmt(AssignStmt(Id(i), IntegerLit(8)), BinExpr(<, Id(i), IntegerLit(20)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))])))), ReturnStmt(FloatLit(1.223e+20))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))
        
    def test86(self):
        """More complex program"""
        input = """func1 : function integer (c : string, out d : boolean) {
            if(a == 5) c = a % 7 ;
            else if (a == 4) d = a / 8 ;
            else randarr = "integer" - 9 * 44 * 5 + c - d ;
            return 0;
            }"""
        expect = """Program([
	FuncDecl(func1, IntegerType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(7))), IfStmt(BinExpr(==, Id(a), IntegerLit(4)), AssignStmt(Id(d), BinExpr(/, Id(a), IntegerLit(8))), AssignStmt(Id(randarr), BinExpr(-, BinExpr(+, BinExpr(-, StringLit(integer), BinExpr(*, BinExpr(*, IntegerLit(9), IntegerLit(44)), IntegerLit(5))), Id(c)), Id(d))))), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))
        
    def test87(self):
        """More complex program"""
        input = """arr1 : array [2,3] of string = {{a,b,c},{1,2,3},{}} ; """
        expect = """Program([
	VarDecl(arr1, ArrayType([2, 3], StringType), ArrayLit([ArrayLit([Id(a), Id(b), Id(c)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))
        
    def test88(self):
        """More complex program"""
        input = """arr : array [1,2,3,4_55] of string = {{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}} ;"""
        expect = """Program([
	VarDecl(arr, ArrayType([1, 2, 3, 455], StringType), ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([])])])])])])])])])])])])])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))
        
    def test89(self):
        """More complex program"""
        input = """main1 : function string () {{{{{{{{{{{{}}}}}}}}}}}}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])])])])])])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))
        
    def test90(self):
        """More complex program"""
        input = """main1 : function string () {
            for (i = k, i != 50, decrease(i)) a = super(i) ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), Id(k)), BinExpr(!=, Id(i), IntegerLit(50)), FuncCall(decrease, [Id(i)]), AssignStmt(Id(a), FuncCall(super, [Id(i)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))
        
    def test91(self):
        """More complex program"""
        input = """main1 : function string () {
                return 1/2/3/4/5/6 ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([ReturnStmt(BinExpr(/, BinExpr(/, BinExpr(/, BinExpr(/, BinExpr(/, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)), IntegerLit(5)), IntegerLit(6)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))
        
    def test92(self):
        """More complex program"""
        input = """main1 : function string () {
                	str1, str2: string = "abcdef","";
	                if (true || false) return str1::str2 ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([VarDecl(str1, StringType, StringLit(abcdef)), VarDecl(str2, StringType, StringLit()), IfStmt(BinExpr(||, BooleanLit(True), BooleanLit(False)), ReturnStmt(BinExpr(::, Id(str1), Id(str2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test93(self):
        """More complex program"""
        input = """main1 : function string () {
            bool = !(!(!(1)));
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(bool), UnExpr(!, UnExpr(!, UnExpr(!, IntegerLit(1))))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))
        
    def test94(self):
        """More complex program"""
        input = """main1 : function string () {
            bool = !(-(!(1)));
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(bool), UnExpr(!, UnExpr(-, UnExpr(!, IntegerLit(1))))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))
        
    def test95(self):
        """More complex program"""
        input = """main1 : function string () {
            arr = arr[arr[1],arr[2],arr[1+2,3+4]];
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayCell(arr, [ArrayCell(arr, [IntegerLit(1)]), ArrayCell(arr, [IntegerLit(2)]), ArrayCell(arr, [BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(+, IntegerLit(3), IntegerLit(4))])])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
        
    def test96(self):
        """More complex program"""
        input = """ randfloat : float = 1_332.33e-23 % arr[2,33,2] ;
                    randarr : array [1,3,5] of string = "string" ;"""
        expect = """Program([
	VarDecl(randfloat, FloatType, BinExpr(%, FloatLit(1.33233e-20), ArrayCell(arr, [IntegerLit(2), IntegerLit(33), IntegerLit(2)])))
	VarDecl(randarr, ArrayType([1, 3, 5], StringType), StringLit(string))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
        
    def test97(self):
        """More complex program"""
        input = """main1 : function string () { if ( a > b) break ; else continue ;}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BreakStmt(), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))
        
    def test98(self):
        """More complex program"""
        input = """main1 : function string () { return Super(Super(Super(func1()))) ; }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([ReturnStmt(FuncCall(Super, [FuncCall(Super, [FuncCall(Super, [FuncCall(func1, [])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))
        
    def test99(self):
        """More complex program"""
        input = """main1 : function string () { return {} ; }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([ReturnStmt(ArrayLit([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))
        
    def test100(self):
        """More complex program"""
        input = """a : integer = 1 + 2 ;"""
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, IntegerLit(1), IntegerLit(2)))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))