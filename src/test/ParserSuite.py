import unittest
from TestUtils import TestParser
class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """x : integer"""
        expect = "Error on line 1 col 11: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 201))
        input = """xyxx : array [2] of string ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
        input = """arrstrcv : float = 11_32_.3_232 ;"""
        expect = "Error on line 1 col 24: _"
        self.assertTrue(TestParser.test(input, expect, 203))
        input = """arr : array [3,2] of float = {{1,2},{3,4},{5,8}} ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
        input = """func1 : function auto (out a : integer, b : float) {
            randfloat : float = 1_332.33e-23 ;
            randarr : array [1,3,5] of string ;
            randstring : string = "hololo\\txxewaazh\\f\\b" ;
            return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
        input = """int1, int2, int3 : float = 1.22e332, 1_332_443.e-1223, 0.3322e0 ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
        input = """a, b, c, d: integer = 3, 4, 6 ;"""
        expect = "Error on line 1 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 207))
        input = """a, b, c: integer = 3, 4, 5, 6 ;"""
        expect = "Error on line 1 col 26: ,"
        self.assertTrue(TestParser.test(input, expect, 208))
        input = """arr1, arr2 : array [3,2] of float = {{1,2},{3,4},{5,8}}, {{0,0},{2,3},{9,9}} ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 210))
        input = """test: boolean = x < 0 && y > 1 ;"""
        expect = "Error on line 1 col 27: >"
        self.assertTrue(TestParser.test(input, expect, 211))
        input = """boo1 : boolean = true || true || true || true && false && false ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
        input = """func1 : function auto (out a : integer, b : float) {
            randfloat : float = 1_332.33e-23 ;
            randarr : array [1,3_,5] of string ;
            return;"""
        expect = "Error on line 3 col 32: _"
        self.assertTrue(TestParser.test(input, expect, 213))
        input = """func1 : function auto (out a : integer, b : float) {
            randfloat : float = 1_332.33e-23 ;
            return;"""
        expect = "Error on line 3 col 19: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 214))
        input = """func1 : function auto (out a : integer, b : float) {
            randfloat : float = 1_332.33e-23 ;
            randarr : array [7] of string ;
            return 2233;
            }
            func2 : function void (c : string, out d : boolean) {
            if(a == 5) c = a % 7 ;
            else d = a / 8 ;
            randarr : array [1,3_3,5] of boolean ;
            return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        input = """func1 : function integer (c : string, out d : boolean) {
            if(a == 5) c = a % 7 ;
            else if (a == 4) d = a / 8 ;
            else randarr : integer = 9 * 44 * 5 + c - d ;
            return 0;
            }"""
        expect = "Error on line 4 col 25: :"
        self.assertTrue(TestParser.test(input, expect, 216))
        input = """func1 : function void (c : string, out d : boolean) {
            if(true) printInteger(a) ;
            else a = readInteger() ;
            }"""
        expect = "Error on line 3 col 21: readInteger"
        self.assertTrue(TestParser.test(input, expect, 217))
        input = """func1 : function float (c : string, out d : boolean) {
            if(a == 5) c = a % 7 ;
            else if (a == 4) for (i = 8, i < 20, i / 2) {c = c + 1 ; }
            return 1.223e20 ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
        input = """func1 : function void (c : string, out d : boolean) { 
            do { for (i = 7, i < 13, i + 1) printInteger(i) ; }
            while (True) ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
        input = """func1 : function float (c : string, out d : boolean) {
            a,b,c,d : integer = 1,2,3 ;
            return a ;
            }"""
        expect = "Error on line 2 col 38: ;"
        self.assertTrue(TestParser.test(input, expect, 220))
        input = """func1 : function float (c : string, out d : boolean) {
            a,b,c : integer = 1,2,3,4 ;
            return a ;
            }"""
        expect = "Error on line 2 col 35: ,"
        self.assertTrue(TestParser.test(input, expect, 221))
        input = """func1 : function float (c : string, out d : boolean) {
            a,b,c : array [2_,3] of float ;
            return a ;
            }"""
        expect = "Error on line 2 col 28: _"
        self.assertTrue(TestParser.test(input, expect, 222))
        input = """func1 : function float (c : string, out d : boolean) {
            a,b : array [2,3] of float = {{2.e12, 111_22.33}, {4.42e-23, 223}, {44., 7E23}}, {{99.223e32, 77__99e-2},{8_0_0_8.2233, 66.e1},{70_77, 0}} ;
            return a ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
        input = """int1 : integer = (7 - 9) * 8 - b[2,3,4] % 18 ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
        input = """boolrand : boolean = (a > b) || (c != d) || (x % 2 == 0) && false ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
        input = """func1 : function float (c : string, out d : boolean) {
            arr1 : array [2,3] of string = {{},{}} ; 
            return arr1 ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
        input = """func1 : function float (c : string, out d : boolean) {
            arr1 : array [2,3] of string = {{},{} ; 
            return arr1 ;
            }"""
        expect = "Error on line 2 col 50: ;"
        self.assertTrue(TestParser.test(input, expect, 227))
        input = """func1 : function float (c : string, out d : boolean) {
            boo1 : boolean = !abc[2] && cde[0,1] ; 
            return boo1 ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
        input = """func1 : function integer (c : string, out d : boolean) {
            int1 : integer = -9 + 7 * 122 ; 
            return int1 ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
        input = """func1 : function integer (c : string, out d : boolean) {
            int1 : array [2,2] of integer = {{-9 + 7 * 122, 9 - -9},{a[3] * 7, caltrand(2, b, 5)}} ; 
            return int1 ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        input = """str : string = "" ; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
        input = """func1 : function integer (c : string, out d : boolean) {
            for(i = 0, i < 100, i + 1)
                for(j = i, j < 100, j + 1)
                    if(arr[i,j] == true) return 220 ;
            return int1 ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
        input = """func1 : function integer (c : string, out d : boolean) {
            if(a % 5 == 1) b = 1 ;
            else if (a % 5 == 2) b = 2 ;
            else if (a % 5 == 3) b = 3 ;
            else do
            {
                for (i = 0, i < 100, i + 1) arr[i] = false ;
            }
            while (false) ;
            return a ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
        input = """func1 : function integer (c : string, out d : boolean) {
            a = 9b ;
            return a ;
            }"""
        expect = "Error on line 2 col 17: b"
        self.assertTrue(TestParser.test(input, expect, 234))
        input = """func1 : function integer (c : string, out d : boolean) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
        input = """int1 : integer"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 236))
        input = """arr : array [1,2,3,4_55] of string = {{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}} ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
        input = """flt1 : float = 155_66.e-13 + 0e-23 ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
        input = """func1 : function float () {
            readInteger() ;
            printInteger(213213) ;
            readFloat() ;
            writeFloat() ;
            readBoolean() ;
            printBoolean() ;
            readString() ;
            printString() ;
            super();
            preventDefault();
            }"""
        expect = "Error on line 5 col 23: )"
        self.assertTrue(TestParser.test(input, expect, 239))
        input = """super() ;"""
        expect = "Error on line 1 col 0: super"
        self.assertTrue(TestParser.test(input, expect, 240))
        input = """a : integer = 9 / 5 \n\t\f\b;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
        input = """int1 : integer = ((())) ;"""
        expect = "Error on line 1 col 20: )"
        self.assertTrue(TestParser.test(input, expect, 242))
        input = """str : string = "\\t\\b\\"\\r" ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
        input =  """func1 : function integer (inherit c : string, inherit out d : boolean) {
            return c ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
        input = """func1 : function string (inherit c : string, inherit out d : string) {
            a : string = c :: d :: "abc" ;
            }"""
        expect = "Error on line 2 col 32: ::"
        self.assertTrue(TestParser.test(input, expect, 245))
        input = """func1 : function string (inherit c : string, inherit out d : string) {
            a : string = c :: (d :: "abc") ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
        input = """func1 : function string (inherit c : string, inherit out d : string) {
            a : string = ("cde" :: c) :: (d :: "abc") ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 248))
        input ="""func1 : function string (inherit c : string, inherit out d : string) {
            a : float = (!a || false) != (-b < c) ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
        input = """str1 : string = "\\t\\"\\n\t" :: "\t\t\tssset\\r"; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
        input = """func1 : function string (inherit c : string, inherit out d : string) {
            for (i = 0, i < 10, i = i + 1) printInteger(i) ;
            }"""
        expect = "Error on line 2 col 34: ="
        self.assertTrue(TestParser.test(input, expect, 251))
        input = """func1 : function string (inherit c : string, inherit out d : string) {
            temp : integer = 0 ;
            for (i = 0, i < 10, i + 1) if (i % 2) temp = temp + i ;
            return temp ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
        input = """func1 : function string (inherit c : string, inherit out d : string) {
            temp : integer = 0 ;
            for (i = 0, i < 10, i + 1) 
            {
                if (i % 2) temp = temp + i ;
                else temp = temp + 1 ;
            }
            return temp ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
        input = """func1 : function string (inherit c : string, inherit out d : string) {
            temp : integer = 0 ;
            return ftemp ;
            }
            func2 : function float (a : integer, out b : integer) {
            return func1(2,3,5) ;   
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
        input = """int1 : integer = randfunc(a,6,8_6, 9 / 2, arr[3,4,6/4,7%23]) ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
        input = """func1 : function string (inherit c : string, inherit out d : string) {
            temp : array [2,2] of string = {{a,a},{d,d}} ;
            int1 : integer = 0 ;
            return temp[int1, int1] ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
        input = """temp : integer = 12 ;
        func1 : function string (inherit c : string, inherit out d : string) {
            temp : array [2,2] of string ;
            temp[0,1] = "randtrfck\t" ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
        input = """main : function void () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
        input = """main1 : function string () {
            printInteger(arr[2,b,3,c]) ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
        input = """main1 : function string () {
            printInteger(func1(2,3,4), func2(a,b,c), func3("sss", "oop")) ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
        input = """int0 : array [22 of float ;"""
        expect = "Error on line 1 col 17: of"
        self.assertTrue(TestParser.test(input, expect, 263))
        input = """9a : integer = b ;"""
        expect = "Error on line 1 col 0: 9"
        self.assertTrue(TestParser.test(input, expect, 264))
        input = """while : string = "ddxxee\t\t\t\t\\\"" ;"""
        expect = "Error on line 1 col 0: while"
        self.assertTrue(TestParser.test(input, expect, 265))
        input = """_a : integer = __9b ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
        input = """main1 : function string () {
            for(i = 0, i < 20, i + 1)
            {
                if(i % 6 == 3) continue ;
                else if (i == 18) break ;
            }
            return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))
        input = """int1 : int = 7 + 12 ;"""
        expect = "Error on line 1 col 7: int"
        self.assertTrue(TestParser.test(input, expect, 268))
        input = """boo1,boo2,boo3 : boolean = true,false,false||true ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
        input = """main1 : function string () {
            func1() + func2(22);
            }"""
        expect = "Error on line 2 col 20: +"
        self.assertTrue(TestParser.test(input, expect, 270))
        input = """main1 : function string () {
            temp = printBoolean();
            }"""
        expect = "Error on line 2 col 19: printBoolean"
        self.assertTrue(TestParser.test(input, expect, 271))
        input = """flt : float = 32223.44e ;"""
        expect = "Error on line 1 col 22: e"
        self.assertTrue(TestParser.test(input, expect, 272))
        input = """flt : float = 032223.44e23 ;"""
        expect = "Error on line 1 col 15: 32223.44e23"
        self.assertTrue(TestParser.test(input, expect, 273))
        input = """Auto : integer ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
        input = """int0 : Integer ;"""
        expect = "Error on line 1 col 7: Integer"
        self.assertTrue(TestParser.test(input, expect, 275))
        input = """str : string = "{c}Y4enROD$$$!h%-~~V{9p>kXS6Ib>05" ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
        input = """str : string = "\ttoo(;_;)many(;_;)test(;_;)cases(;_;)\t" ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
        input = """_A330xr : integer ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
        input = """a,b,c : array [5,6] of string = {},{},{} ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
        input = """res : float = sin(a,b) / cos(c,d) ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 281))
        input = """main1 : function string () {
            do a = a / 9 ;
            while (a > 100) ;
            }"""
        expect = "Error on line 2 col 15: a"
        self.assertTrue(TestParser.test(input, expect, 282))
        input = """main1 : function string () 
            do {a = a / 9 ;}
            while (a > 100) ;
            }"""
        expect = "Error on line 2 col 12: do"
        self.assertTrue(TestParser.test(input, expect, 283))
        input = """main1 : function string () {
            do {a = a / 9 ;}
            while (a > 100) ;
            """
        expect = "Error on line 4 col 12: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 284))
        input = """main1 : function string () {
            for (i = k, i != 50, increase(i)) printInteger(i) ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
        input = """int223 : array [2,2,2] of boolean = {{{true,false},{true,true}},{{false, false},{false, true}}} ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
        input = """int223 : array [2,2,2] of boolean = {{{true,false},{true,true}},{false, false},{false, true}}} ;"""
        expect = "Error on line 1 col 93: }"
        self.assertTrue(TestParser.test(input, expect, 287))
        input = """int223 : array [2,2,2] of boolean = {{{true,False},{True,true}},{{false, false},{False, true}}} ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
        input = """main1 : function string () {
            while(a < 23)
            do {a = a / 9 ;}
            while (a > 100) ;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
        input = """strstr : string = "\\"\\"\\'\\\\" ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))
        input = """main1 : function string () {
            bool = "abc\\t" != "abc\t" ;
            return ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
        input = """main1 : function string () {
            bool = 7 - 9 < 4 - 6 ;
            return ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))
        input =  """main1 : function string () {
            str = 7 - 9 * 4 - 6 ;
            return ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
        input = """main1 : function string () {
            str = (8 < 9) || (4 > 6) ;
            return ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
        input = """main1 : function string () {
            boo = 8 < 9 || 4 > 6 ;
            return ;
            }"""
        expect = "Error on line 2 col 29: >"
        self.assertTrue(TestParser.test(input, expect, 295))
        input = """main1 : function string () {
            bool = 1 < 2 < 3 < 4 ;
            return ;
            }"""
        expect = "Error on line 2 col 25: <"
        self.assertTrue(TestParser.test(input, expect, 296))
        input = """main1 : function string () {
            bool = ((1 < 2) < 3) < 4 ;
            return ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
        input = """main1 : function string () {
            str = "abc" :: "cde" :: "123" :: "456" ;
            return ;
            }"""
        expect = "Error on line 2 col 33: ::"
        self.assertTrue(TestParser.test(input, expect, 298))
        input = """main1 : function string () {
            str = (("abc" :: "cde") :: "123") :: "456" ;
            return ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))
        input =  """ a : string = "213123213\\'" ;  """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))


