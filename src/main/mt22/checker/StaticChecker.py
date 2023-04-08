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
        return ["IntegerType", "@", ['0']]
    
    def visitFloatType(self, ast, param):
        return ["FloatType", "@", ['0']]
    
    def visitBooleanType(self, ast, param):
        return ["BooleanType", "@", ['0']]
    
    def visitStringType(self, ast, param):
        return ["StringType", "@", ['0']]
    
    def visitArrayType(self, ast, param):
        return ["ArrayType", str(ast.typ), ast.dimensions]
    
    def visitAutoType(self, ast, param):
        return ["AutoType", "@", ['0']]
    
    def visitVoidType(self, ast, param):
        return ["VoidType", "@", ['0']]  
    
    # Data literal
    def visitBinExpr(self, ast, param):
        op = str(ast.op)
        left = ast.left
        right = ast.right
        
        leftValue = self.visit(ast.left, param)
        rightValue = self.visit(ast.right, param)

        if op == "+" or op == "-" or op == "*" or op == "/":
            if leftValue[1] != "IntegerType" and leftValue[1] != "FloatType":
                raise TypeMismatchInExpression(left)
            if rightValue[1] != "IntegerType" and rightValue[1] != "FloatType":
                raise TypeMismatchInExpression(right)
            if leftValue[1] == "IntegerType" and rightValue[1] == "IntegerType":
                typ = "IntegerType"
            else:
                typ = "FloatType"
        elif op == "%":
            if leftValue[1] != "IntegerType":
                raise TypeMismatchInExpression(left)
            if rightValue[1] != "IntegerType":
                raise TypeMismatchInExpression(right)
            typ = "IntegerType"
        elif op == "&&" or op == "||":
            if leftValue[1] != "BooleanType":
                raise TypeMismatchInExpression(left)
            if rightValue[1] != "BooleanType":
                raise TypeMismatchInExpression(right)
            typ = "BooleanType"
        elif op == "==" or op == "!=":
            if leftValue[1] != "IntegerType" and leftValue[1] != "BooleanType":
                raise TypeMismatchInExpression(left)
            if rightValue[1] != "IntegerType" and rightValue[1] != "BooleanType":
                raise TypeMismatchInExpression(right)
            # TODO Xem lai raise loi o left hay right
            if leftValue[1] != rightValue[1]:
                 raise TypeMismatchInExpression(right)
            typ = "BooleanType"
        elif op == "<" or op == ">" or op == "<=" or op == ">=":
            if leftValue[1] != "IntegerType" and leftValue[1] != "FloatType":
                raise TypeMismatchInExpression(left)
            if rightValue[1] != "IntegerType" and rightValue[1] != "FloatType":
                raise TypeMismatchInExpression(right)
            typ = "BooleanType"
        elif op == "::":
            if leftValue[1] != "StringType":
                raise TypeMismatchInExpression(left)
            if rightValue[1] != "StringType":
                raise TypeMismatchInExpression(right)
            typ = "StringType"
        return [op, typ]
    
    def visitUnExpr(self, ast, param):
        op = str(ast.op)
        val = ast.val
        
        valValue = self.visit(ast.val, param)

        if op == "-":
            if valValue[1] != "IntegerType" and valValue[1] != "FloatType":
                raise TypeMismatchInExpression(val)
            typ = valValue[1]
        elif op == "!":
            if valValue[1] != "BooleanType":
                raise TypeMismatchInExpression(val)
            typ = "BooleanType"
        return [op, typ]
    
    def visitId(self, ast, param):
        name = ast.name
        for id in param:
            if name == id[0]:
                return id
        else:
            raise Undeclared(Identifier(), name)
    
    def visitArrayCell(self, ast, param):
        name = ast.name
        cell = ast.cell
        
        for id in param:
            if name == id[0]:
                if id[1] == "ArrayType":
                    for idx in cell:
                        if type(idx) != IntegerLit:
                            raise TypeMismatchInExpression(idx)
                    return ["@", id[2]]
                else:
                    raise TypeMismatchInExpression(name)
        else:
            raise Undeclared(Identifier(), name)
    
    def visitIntegerLit(self, ast, param):
        return ["@", "IntegerType"]
    
    def visitFloatLit(self, ast, param):
        return ["@", "FloatType"]
    
    def visitBooleanLit(self, ast, param):
        return ["@", "BooleanType"]  

    def visitStringLit(self, ast, param):
        return ["@", "StringType"]
    
    def visitArrayLit(self, ast, param):
        explist = ast.explist
        typArr = []
        for exp in explist:
            ele = self.visit(exp, param)
            typArr.append(ele[1])
        # TODO Xem lai raise loi o element ben phai hay element ben trai
        for i in range(len(typArr) - 1):
            if typArr[i] != typArr[i + 1]:
                raise IllegalArrayLiteral(explist[i + 1])
        return ["@", typArr[0]]
    
    # TODO
    def visitFuncCall(self, ast, param): pass
    
    # TODO Exclude subexpr
    
    # Statements
    # TODO
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
        visitRes = self.visit(ast.typ, [])
        typ, array_typ, dim = visitRes[0], visitRes[1], visitRes[2]
        init = ast.init
        
        for id in param:
            if name == id[0]:
                raise Redeclared(Variable(), name)
        
        if init:
            initValue = self.visit(ast.init, param)
            if typ == "IntegerType":
                if initValue[1] != "IntegerType":
                    raise TypeMismatchInExpression(init)
            elif typ == "FloatType":
                if initValue[1] != "IntegerType" and initValue[1] != "FloatType":
                    raise TypeMismatchInExpression(init)
            elif typ == "BooleanType":
                if initValue[1] != "BooleanType":
                    raise TypeMismatchInExpression(init)
            elif typ == "StringType":
                if initValue[1] != "StringType":
                    raise TypeMismatchInExpression(init)
            elif typ == "ArrayType":
                if initValue[1] != array_typ:
                    raise TypeMismatchInExpression(init)
            # TODO
            elif typ == "AutoType":
                pass
        else:
            if typ == "AutoType":
                raise Invalid(Variable(), name)

        return [name, typ, array_typ, dim]
    
    # TODO
    def visitParamDecl(self, ast, param): pass
    
    # TODO
    def visitFuncDecl(self, ast, param): pass
    
    def visitProgram(self, ast, param):
        for decl in ast.decls:
            param += [self.visit(decl, param)]
        # print(param, "\n")