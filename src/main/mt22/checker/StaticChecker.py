from AST import *
from Visitor import Visitor
from StaticError import *
class StaticChecker(Visitor):
    
    def __init__(self, ast):
        self.ast = ast
    
    def check(self):
        self.visit(self.ast, [])
        return ""
    
    # Data type
    def visitIntegerType(self, ast, param):
        return "integer"
    
    def visitFloatType(self, ast, param):
        return "float"
    
    def visitBooleanType(self, ast, param):
        return "boolean"
    
    def visitStringType(self, ast, param):
        return "string"
    
    def visitArrayType(self, ast, param): pass
    
    def visitAutoType(self, ast, param):
        return "auto"
    
    def visitVoidType(self, ast, param): pass  
    
    # Data literal
    def visitBinExpr(self, ast, param): pass
    
    def visitUnExpr(self, ast, param): pass
    
    def visitId(self, ast, param):
        name = ast.name
        for id in param:
            if name == id[0]:
                return id
        else:
            raise Undeclared(Variable(), name)
    
    def visitArrayCell(self, ast, param): pass
    
    def visitIntegerLit(self, ast, param):
        return int(ast.val)
    
    def visitFloatLit(self, ast, param):
        return float(ast.val)
    
    def visitBooleanLit(self, ast, param):
        return bool(ast.val)  

    def visitStringLit(self, ast, param):
        return str(ast.val)
    
    def visitArrayLit(self, ast, param): pass
    
    def visitFuncCall(self, ast, param): pass
    
    # Statements
    def visitAssignStmt(self, ast, param): pass
    
    def visitBlockStmt(self, ast, param): pass
    
    def visitIfStmt(self, ast, param): pass
    
    def visitForStmt(self, ast, param): pass
    
    def visitWhileStmt(self, ast, param): pass
    
    def visitDoWhileStmt(self, ast, param): pass
    
    def visitBreakStmt(self, ast, param): pass
    
    def visitContinueStmt(self, ast, param): pass
    
    def visitReturnStmt(self, ast, param): pass
    
    def visitCallStmt(self, ast, param): pass
    
    # Vardecl        
    def visitVarDecl(self, ast, param):
        name = ast.name
        typ = self.visit(ast.typ, [])
        init = ast.init

        for id in param:
            if name == id[0]:
                raise Redeclared(Variable(), name)
        
        if init:
            initValue = self.visit(ast.init, param)
            if typ == "integer":
                if type(initValue) is not int:
                    if type(initValue) is float or type(initValue) is bool or type(initValue) is str:
                        raise TypeMismatchInExpression(init)
                    elif initValue[1] != "integer":
                        raise TypeMismatchInExpression(init)
            elif typ == "float":
                if type(initValue) is not int and type(initValue) is not float:
                    if type(initValue) is bool or type(initValue) is str:
                        raise TypeMismatchInExpression(init)
            elif typ == "boolean":
                if type(initValue) is not bool:
                    if type(initValue) is int or type(initValue) is float or type(initValue) is str:
                        raise TypeMismatchInExpression(init)
            elif typ == "string":
                if type(initValue) is not str:
                    if type(initValue) is int or type(initValue) is float or type(initValue) is bool:
                        raise TypeMismatchInExpression(init)
            # TODO ArrayType and AutoType
            elif typ == "array":
                pass
            elif typ == "auto":
                pass
            return [name, typ, initValue]
        else:
            if typ == "auto":
                raise Invalid(Variable(), name)
            return [name, typ]
    
    def visitParamDecl(self, ast, param): pass
    
    def visitFuncDecl(self, ast, param): pass
    
    def visitProgram(self, ast, param):
        for decl in ast.decls:
            param += [self.visit(decl, param)]
        # print(param)