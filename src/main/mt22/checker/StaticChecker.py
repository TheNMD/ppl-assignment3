from Visitor import Visitor
from StaticError import *

class StaticChecker(Visitor):
    
    def __init__(self, ast):
        self.ast = ast
    
    def check(self):
        return self.visitProgram(self.ast, [])
    
    def visitProgram(self, ast, param):
        obj = []
        # print(ast.decls)
        # raise Redeclared(kind=Variable(),identifier=name)
        return ""
            
    # def visitVarDecl(self, ast, param):
    #     name = ast.name
    #     if name in param:
    #         raise Redeclared(kind=Variable(),identifier=name)
    #     return name