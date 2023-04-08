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
    def visitBinExpr(self, ast, param):
        op = str(ast.op)
        left = ast.left
        right = ast.right
        # print(left, "  ", right)
        
        leftValue = self.visit(ast.left, param)
        rightValue = self.visit(ast.right, param)
        # print(leftValue, "  ", rightValue)

        if op == "+" or op == "-" or op == "*" or op == "/":
            if leftValue[1] != "integer" and leftValue[1] != "float":
                raise TypeMismatchInExpression(left)
            if rightValue[1] != "integer" and rightValue[1] != "float":
                raise TypeMismatchInExpression(right)
            if leftValue[1] == "integer" and rightValue[1] == "integer":
                typ = "integer"
            else:
                typ = "float"
        elif op == "%":
            if leftValue[1] != "integer":
                raise TypeMismatchInExpression(left)
            if rightValue[1] != "integer":
                raise TypeMismatchInExpression(right)
            typ = "integer"
        elif op == "&&" or op == "||":
            if leftValue[1] != "boolean":
                raise TypeMismatchInExpression(left)
            if rightValue[1] != "boolean":
                raise TypeMismatchInExpression(right)
            typ = "boolean"
        elif op == "==" or op == "!=":
            if leftValue[1] != "integer" and leftValue[1] != "boolean":
                raise TypeMismatchInExpression(left)
            if rightValue[1] != "integer" and rightValue[1] != "boolean":
                raise TypeMismatchInExpression(right)
            # TODO Xem lai coi raise loi o left hay right
            if leftValue[1] != rightValue[1]:
                 raise TypeMismatchInExpression(right)
            typ = "boolean"
        elif op == "<" or op == ">" or op == "<=" or op == ">=":
            if leftValue[1] != "integer" and leftValue[1] != "float":
                raise TypeMismatchInExpression(left)
            if rightValue[1] != "integer" and rightValue[1] != "float":
                raise TypeMismatchInExpression(right)
            typ = "boolean"
        elif op == "::":
            if leftValue[1] != "string":
                raise TypeMismatchInExpression(left)
            if rightValue[1] != "string":
                raise TypeMismatchInExpression(right)
            typ = "string"
        return [op, typ]
    
    def visitUnExpr(self, ast, param):
        op = str(ast.op)
        val = ast.val
        # print(val)
        
        valValue = self.visit(ast.val, param)
        # print(valValue)

        if op == "-":
            if valValue[1] != "integer" and valValue[1] != "float":
                raise TypeMismatchInExpression(val)
            typ = valValue[1]
        elif op == "!":
            if valValue[1] != "boolean":
                raise TypeMismatchInExpression(val)
            typ = "boolean"
        return [op, typ]
    
    def visitId(self, ast, param):
        name = ast.name
        for id in param:
            if name == id[0]:
                return id
        else:
            raise Undeclared(Variable(), name)
    
    def visitArrayCell(self, ast, param): pass
    
    def visitIntegerLit(self, ast, param):
        return [str(ast.val), "integer"]
    
    def visitFloatLit(self, ast, param):
        return [str(ast.val), "float"]
    
    def visitBooleanLit(self, ast, param):
        return [str(ast.val), "boolean"]  

    def visitStringLit(self, ast, param):
        return [str(ast.val), "string"]
    
    def visitArrayLit(self, ast, param): pass
    
    def visitFuncCall(self, ast, param): pass
    
    # TODO Xem lai subexpr
    
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
            # print(initValue)
            if typ == "integer":
                if initValue[1] != "integer":
                    raise TypeMismatchInExpression(init)
            elif typ == "float":
                if initValue[1] != "integer" and initValue[1] != "float":
                    raise TypeMismatchInExpression(init)
            elif typ == "boolean":
                if initValue[1] != "boolean":
                    raise TypeMismatchInExpression(init)
            elif typ == "string":
                if initValue[1] != "string":
                    raise TypeMismatchInExpression(init)
            # TODO ArrayType and AutoType
            elif typ == "array":
                pass
            elif typ == "auto":
                pass
        else:
            if typ == "auto":
                raise Invalid(Variable(), name)
            
        return [name, typ]
    
    def visitParamDecl(self, ast, param): pass
    
    def visitFuncDecl(self, ast, param): pass
    
    def visitProgram(self, ast, param):
        for decl in ast.decls:
            param += [self.visit(decl, param)]
        # print(param, "\n")