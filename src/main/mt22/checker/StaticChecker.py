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
        if init:
            # TODO init la BinExpr, UnExpr, ArrayCell, FuncCall, ID
            if type(typ) is IntegerType:
                if type(init) is FloatLit or type(init) is BooleanLit or type(init) is StringLit:
                    raise TypeMismatchInExpression(init)
                if type(init) is BinExpr:
                    pass
                elif type(init) is UnExpr:
                    pass
                elif type(init) is Id:
                    pass
                elif type(init) is ArrayCell:
                    pass
                elif type(init) is FuncCall:
                    pass
            elif type(typ) is FloatType:
                if type(init) is BooleanLit or type(init) is StringLit:
                    raise TypeMismatchInExpression(init)
                if type(init) is BinExpr:
                    pass
                elif type(init) is UnExpr:
                    pass
                elif type(init) is Id:
                    pass
                elif type(init) is ArrayCell:
                    pass
                elif type(init) is FuncCall:
                    pass
            elif type(typ) is BooleanType:
                if type(init) is IntegerLit or type(init) is FloatLit or type(init) is StringLit:
                    raise TypeMismatchInExpression(init)
                if type(init) is BinExpr:
                    pass
                elif type(init) is UnExpr:
                    pass
                elif type(init) is Id:
                    pass
                elif type(init) is ArrayCell:
                    pass
                elif type(init) is FuncCall:
                    pass
            elif type(typ) is StringType:
                if type(init) is IntegerLit or type(init) is FloatLit or type(init) is BooleanLit:
                    raise TypeMismatchInExpression(init)
                if type(init) is BinExpr:
                    pass
                elif type(init) is UnExpr:
                    pass
                elif type(init) is Id:
                    pass
                elif type(init) is ArrayCell:
                    pass
                elif type(init) is FuncCall:
                    pass
            elif type(typ) is ArrayType:
                pass
            elif type(typ) is AutoType:
                pass
        else:
            if type(typ) is AutoType:
                raise Invalid(kind=Variable(), name=name)
        return ast.name
    
    # def visit(self, ast, param):
    #     return ast.accept(self, param)

    # def visitIntegerType(self, ast, param): pass
    # def visitFloatType(self, ast, param): pass
    # def visitBooleanType(self, ast, param): pass
    # def visitStringType(self, ast, param): pass
    # def visitArrayType(self, ast, param): pass
    # def visitAutoType(self, ast, param): pass
    # def visitVoidType(self, ast, param): pass

    # def visitBinExpr(self, ast, param): pass
    # def visitUnExpr(self, ast, param): pass
    # def visitId(self, ast, param): pass
    # def visitArrayCell(self, ast, param): pass
    # def visitIntegerLit(self, ast, param): pass
    # def visitFloatLit(self, ast, param): pass
    # def visitStringLit(self, ast, param): pass
    # def visitBooleanLit(self, ast, param): pass
    # def visitArrayLit(self, ast, param): pass
    # def visitFuncCall(self, ast, param): pass

    # def visitAssignStmt(self, ast, param): pass
    # def visitBlockStmt(self, ast, param): pass
    # def visitIfStmt(self, ast, param): pass
    # def visitForStmt(self, ast, param): pass
    # def visitWhileStmt(self, ast, param): pass
    # def visitDoWhileStmt(self, ast, param): pass
    # def visitBreakStmt(self, ast, param): pass
    # def visitContinueStmt(self, ast, param): pass
    # def visitReturnStmt(self, ast, param): pass
    # def visitCallStmt(self, ast, param): pass

    # def visitVarDecl(self, ast, param): pass
    # def visitParamDecl(self, ast, param): pass
    # def visitFuncDecl(self, ast, param): pass

    # def visitProgram(self, ast, param): pass
