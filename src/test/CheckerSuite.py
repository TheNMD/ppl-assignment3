import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test1(self):
        input = "Program([],BinOp("+",IntLit(3),BoolLit(True)))"
        expect = "Type Mismatch In Expression: BinOp("+",IntLit(3),BoolLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 301))