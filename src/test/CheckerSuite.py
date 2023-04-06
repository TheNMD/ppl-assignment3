import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test1(self):
        input = """x : integer ;"""
        expect = "None"
        self.assertTrue(TestChecker.test(input, expect, 401))