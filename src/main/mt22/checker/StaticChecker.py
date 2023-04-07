from AST import *
from Visitor import Visitor
from StaticError import *
class StaticChecker(Visitor):
    
    def __init__(self, ast):
        self.ast = ast
    
    def check(self):
        return self.visit(ast=self.ast, param=[])
    
    def visitProgram(self, ast, param):
        decls = ast.decls
        for decl in decls:
            param += [self.visit(decl, param)]
        return ""
            
    def visitVarDecl(self, ast, param):
        name, typ, init = ast.name, ast.typ, ast.init
        if name in param:
            raise Redeclared(kind=Variable(), identifier=name)
        # TODO Undeclared
        if init:
            # TODO init la BiExpr, UnExpr, ArrayCell, FuncCall, ID
            if type(typ) is IntegerType:
                if type(init) is not IntegerLit:
                    raise TypeMismatchInExpression(init)
            elif type(typ) is FloatType:
                if type(init) is not IntegerLit and type(init) is not FloatLit:
                    raise TypeMismatchInExpression(init)
            elif type(typ) is BooleanType:
                if type(init) is not BooleanLit:
                    raise TypeMismatchInExpression(init)
            elif type(typ) is StringType:
                if type(init) is not StringLit:
                    raise TypeMismatchInExpression(init)
            elif type(typ) is ArrayType:
                pass
            elif type(typ) is AutoType:
                pass
            # TODO Xem lai VoidType o ASTGeneration
        else:
            if type(typ) is AutoType:
                raise Invalid(kind=Variable(), name=name)
        return ast.name
    
    def visitIntegerType(self, ast, param): pass
    def visitFloatType(self, ast, param): pass
    def visitBooleanType(self, ast, param): pass
    def visitStringType(self, ast, param): pass
    def visitArrayType(self, ast, param): pass
    def visitAutoType(self, ast, param): pass
    def visitVoidType(self, ast, param): pass
    
    def visitBinExpr(self, ast, param): pass
    def visitUnExpr(self, ast, param): pass
    def visitId(self, ast, param): pass
    def visitArrayCell(self, ast, param): pass
    def visitIntegerLit(self, ast, param): pass
    def visitFloatLit(self, ast, param): pass
    def visitStringLit(self, ast, param): pass
    def visitBooleanLit(self, ast, param): pass
    def visitArrayLit(self, ast, param): pass
    def visitFuncCall(self, ast, param): pass
