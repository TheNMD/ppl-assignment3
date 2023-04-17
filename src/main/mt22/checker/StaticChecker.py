from AST import *
from Visitor import Visitor
from StaticError import *

class VariableDeclaration:
    def __init__(self, name, typ, array_typ, dim, accessibleList):
        self.name = name
        self.typ = typ
        self.array_typ = array_typ
        self.dim = dim
        self.accessibleList = accessibleList

class ParameterDeclaration:
    def __init__(self, name, typ, array_typ, dim, out, inherit, accessibleList):
        self.name = name
        self.typ = typ
        self.array_typ = array_typ
        self.dim = dim
        self.out = out
        self.inherit = inherit
        self.accessibleList = accessibleList
        
class FunctionDeclaration:
    def __init__(self, name, typ, rtn_typ, array_typ, dim, inherit, paraList, accessibleList):
        self.name = name
        self.typ = typ
        self.rtn_typ = rtn_typ
        self.array_typ = array_typ
        self.dim = dim
        self.inherit = inherit
        self.paraList = paraList
        self.accessibleList = accessibleList

def checkArrayLit(array_lit, dim, counter, array_typ, ast):
    if counter == len(dim):
        return False
    if len(array_lit) == int(dim[counter]):
        for i in array_lit:
            if type(i) == str:
                if array_typ == "FloatType":
                    if i != "IntegerType" and i != "FloatType":
                        return False
                    return True
                else:
                    if i != array_typ:
                        return False
                    return True
            else:
                return checkArrayLit(i, dim, counter + 1, array_typ, ast)
    else:
        return False
    
class StaticChecker(Visitor):
    
    def __init__(self, ast):
        self.ast = ast
    
    def check(self):
        self.visit(self.ast, [])
        return ""
    
    # Data type
    def visitIntegerType(self, ast, param):
        return "IntegerType", None, None
    
    def visitFloatType(self, ast, param):
        return "FloatType", None, None
    
    def visitBooleanType(self, ast, param):
        return "BooleanType", None, None
    
    def visitStringType(self, ast, param):
        return "StringType", None, None
    
    def visitArrayType(self, ast, param):
        return "ArrayType", str(ast.typ), ast.dimensions
    
    def visitAutoType(self, ast, param):
        return "AutoType", None, None
    
    def visitVoidType(self, ast, param):
        return "VoidType", None, None  
    
    # Data literal
    def visitBinExpr(self, ast, param):
        op = str(ast.op)
        left = ast.left
        right = ast.right
        
        leftValue = self.visit(ast.left, param)
        rightValue = self.visit(ast.right, param)
        
        if leftValue == "AutoType":
            TypeMismatchInExpression(left)
        elif rightValue == "AutoType":
            TypeMismatchInExpression(right)
        elif  leftValue == "FAutoType" and rightValue == "FAutoType":
            # TODO Xem lai raise loi nhu the nao khi left va right deu la FAutoType
            raise TypeMismatchInExpression(ast)
        elif leftValue == "FAutoType" and rightValue != "FAutoType":
            leftValue = rightValue
            for ele in param:
                if ele.name == left.name and ele.typ == "FunctionType":
                    ele.rtn_typ = rightValue
        elif leftValue != "FAutoType" and rightValue == "FAutoType":
            rightValue = leftValue
            for ele in param:
                if ele.name == right.name and ele.typ == "FunctionType":
                    ele.rtn_typ = leftValue

        if op == "+" or op == "-" or op == "*" or op == "/":
            if leftValue != "IntegerType" and leftValue != "FloatType":
                raise TypeMismatchInExpression(left)
            if rightValue != "IntegerType" and rightValue != "FloatType":
                raise TypeMismatchInExpression(right)
            if leftValue == "IntegerType" and rightValue == "IntegerType":
                res = "IntegerType"
            else:
                res = "FloatType"
        elif op == "%":
            if leftValue != "IntegerType":
                raise TypeMismatchInExpression(left)
            if rightValue != "IntegerType":
                raise TypeMismatchInExpression(right)
            res = "IntegerType"
        elif op == "&&" or op == "||":
            if leftValue != "BooleanType":
                raise TypeMismatchInExpression(left)
            if rightValue != "BooleanType":
                raise TypeMismatchInExpression(right)
            res = "BooleanType"
        elif op == "==" or op == "!=":
            if leftValue != "IntegerType" and leftValue != "BooleanType":
                raise TypeMismatchInExpression(left)
            if rightValue != "IntegerType" and rightValue != "BooleanType":
                raise TypeMismatchInExpression(right)
            # TODO Xem lai raise loi o left hay right
            if leftValue != rightValue:
                 raise TypeMismatchInExpression(right)
            res = "BooleanType"
        elif op == "<" or op == ">" or op == "<=" or op == ">=":
            if leftValue != "IntegerType" and leftValue != "FloatType":
                raise TypeMismatchInExpression(left)
            if rightValue != "IntegerType" and rightValue != "FloatType":
                raise TypeMismatchInExpression(right)
            res = "BooleanType"
        elif op == "::":
            if leftValue != "StringType":
                raise TypeMismatchInExpression(left)
            if rightValue != "StringType":
                raise TypeMismatchInExpression(right)
            res = "StringType"
        return res
    
    def visitUnExpr(self, ast, param):
        op = str(ast.op)
        val = ast.val
        
        valValue = self.visit(ast.val, param)

        if op == "-":
            if valValue != "IntegerType" and valValue != "FloatType":
                raise TypeMismatchInExpression(val)
            res = valValue
        elif op == "!":
            if valValue != "BooleanType":
                raise TypeMismatchInExpression(val)
            res = "BooleanType"
        return res
    
    def visitId(self, ast, param):
        name = ast.name
        
        if type(param[-1]) == str:
            param = param[:-1]
        
        for ele in param:
            if name == ele.name and ele.typ != "FunctionType":
                return ele.typ
        else:
            raise Undeclared(Identifier(), name)
    
    def visitArrayCell(self, ast, param):
        name = ast.name
        cell = ast.cell
        
        for ele in param:
            if name == ele.name and ele.typ != "FunctionType":
                if ele.typ == "ArrayType":
                    for idx in cell:
                        if type(idx) != IntegerLit:
                            raise TypeMismatchInExpression(idx)
                    return ele.array_typ
                else:
                    raise TypeMismatchInExpression(name)
        else:
            raise Undeclared(Identifier(), name)
    
    def visitIntegerLit(self, ast, param):
        return "IntegerType"
    
    def visitFloatLit(self, ast, param):
        return "FloatType"
    
    def visitBooleanLit(self, ast, param):
        return "BooleanType" 

    def visitStringLit(self, ast, param):
        return "StringType"
    
    def visitArrayLit(self, ast, param):
        expList = ast.explist
        tempArr = []
        for exp in expList:
            ele = self.visit(exp, param)
            tempArr.append(ele)
        for i in range(len(tempArr) - 1):
            if type(tempArr[i]) == str:
                if tempArr[i] != tempArr[i + 1]:
                    if tempArr[i] == "IntegerType" and tempArr[i + 1] == "FloatType" or tempArr[i] == "FloatType" and tempArr[i + 1] == "IntegerType":
                        continue
                    raise IllegalArrayLiteral(ast)
            else:
                if len(tempArr[i]) != len(tempArr[i + 1]):
                    raise TypeMismatchInExpression(expList[i + 1]) 
        return tempArr

    def visitFuncCall(self, ast, param):
        name = ast.name
        args = ast.args
        for ele in param:
            if name == ele.name and ele.typ == "FunctionType":
                if ele.rtn_typ == "VoidType":
                    raise TypeMismatchInExpression(ast)
                # TODO Xem lai coi so arg khac so para thi loi gi
                if len(args) == len(ele.paraList):
                    for i in range(len(args)):
                        arg = self.visit(args[i], [])
                        para = ele.paraList[i].typ
                        if arg != para:
                            if para == "FloatType" and arg == "IntegerType":
                                continue
                            raise TypeMismatchInExpression(args[i])
                elif len(args) > len(ele.paraList):
                    for i in range(len(ele.paraList)):
                        arg = self.visit(args[i], [])
                        para = ele.paraList[i].typ
                        if arg != para:
                            if para == "FloatType" and arg == "IntegerType":
                                continue
                            raise TypeMismatchInExpression(args[i])
                    raise TypeMismatchInExpression(args[len(ele.paraList)])
                elif len(args) < len(ele.paraList): pass
                if ele.rtn_typ == "AutoType":
                    return "FAutoType"
                return ele.rtn_typ
        else:
            raise Undeclared(Function(), name)
    
    # Statements
    def visitAssignStmt(self, ast, param): pass
    
    def visitBlockStmt(self, ast, param):
        body = ast.body
        if body:
            return body
        return []
    
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
        typ, array_typ, dim = self.visit(ast.typ, [])
        init = ast.init
        
        for ele in param:
            if name == ele.name and ele.typ != "FunctionType":
                raise Redeclared(Variable(), name)
        
        accessibleList = []
        for ele in param:
            accessibleList += [ele]

        param += [VariableDeclaration(name, typ, array_typ, dim, accessibleList)]
        
        if init:
            initValue = self.visit(ast.init, param)
            if initValue == "AutoType":
                raise TypeMismatchInExpression(init)
            elif initValue == "FAutoType":
                initValue = typ
                for ele in param:
                    if init.name == ele.name and ele.typ == "FunctionType":
                        ele.rtn_typ = initValue
            else:
            # TODO Xem lai TypeMismatchInVarDecl raise o ast hay init
                if typ == "IntegerType":
                    if initValue != "IntegerType":
                        raise TypeMismatchInVarDecl(ast)
                elif typ == "FloatType":
                    if initValue != "IntegerType" and initValue != "FloatType":
                        raise TypeMismatchInVarDecl(ast)
                elif typ == "BooleanType":
                    if initValue != "BooleanType":
                        raise TypeMismatchInVarDecl(ast)
                elif typ == "StringType":
                    if initValue != "StringType":
                        raise TypeMismatchInVarDecl(ast)
                elif typ == "ArrayType":
                    res = checkArrayLit(initValue, dim, 0, array_typ, ast)
                    if res == False:
                        raise TypeMismatchInVarDecl(ast)
                elif typ == "AutoType":
                    if initValue == "AutoType":
                        raise TypeMismatchInVarDecl(ast)
                    param[-1].typ = initValue
        else:
            if typ == "AutoType":
                raise Invalid(Variable(), name)
            
        return []
    
    def visitParamDecl(self, ast, param):
        name = ast.name
        typ, array_typ, dim = self.visit(ast.typ, [])
        out = ast.out
        inherit = ast.inherit
        
        for ele in param:
            if name == ele.name and ele.typ != "FunctionType":
                raise Redeclared(Parameter(), name)
        
        accessibleList = []
        for ele in param:
            accessibleList += [ele]

        return [ParameterDeclaration(name, typ, array_typ, dim, out, inherit, accessibleList)]
        
    def visitFuncDecl(self, ast, param):
        name = ast.name
        rtn_typ, array_typ, dim = self.visit(ast.return_type, [])
        params = ast.params
        inherit = ast.inherit
        body = ast.body
    
        for ele in param:
            if name == ele.name and ele.typ == "FunctionType":
                raise Redeclared(Function(), name)
        
        if inherit:
        # TODO Xem lai keyword inherit o parameter
            for ele in param:
                if inherit == ele.name and ele.typ == "FunctionType":
                    inheritList = ele.paraList
                    break
            else:
                raise Undeclared(Function(), name)
        else:
            pass
        
        paraList = []
        if params:
            for para in params:
                paraList += self.visit(para, paraList)
        
        accessibleList = []
        for ele in param:
            accessibleList += [ele]
        
        accessibleList += paraList
        
        bodyList = []
        bodyList += paraList
        for ele in self.visit(body, []):
            bodyList += self.visit(ele, bodyList)    
        
        # if len(bodyList) > 0:
        #     print(bodyList[1].name)
        
        return [FunctionDeclaration(name, "FunctionType", rtn_typ, array_typ, dim, inherit, paraList, accessibleList)]
        
    def visitProgram(self, ast, param):
        for decl in ast.decls:
            param += self.visit(decl, param)
            
        # for ele in param:
        #     if ele.name == "main" and ele.typ == "FunctionType":
        #         break
        # else:
        #     raise NoEntryPoint()
        
        # for ele in param:
        #     print(f"Name: {ele.name}")
        #     print(f"Type: {ele.typ}")
        #     print(f"Accessible List: {ele.accessibleList}")
        #     if ele.typ == "FunctionType":
        #         print(f"Return type: {ele.rtn_typ}")
        #         print(f"Parameter List: {ele.paraList}")
        #     print("////////////////////////////////////////////////////")