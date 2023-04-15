from AST import *
from Visitor import Visitor
from StaticError import *

class VariableDeclaration:
    def __init__(self, name, typ, array_typ, dim):
        self.name = name
        self.typ = typ
        self.array_typ = array_typ
        self.dim = dim

class ParameterDeclaration:
    def __init__(self, name, typ, array_typ, dim, out, inherit):
        self.name = name
        self.typ = typ
        self.array_typ = array_typ
        self.dim = dim
        self.out = out
        self.inherit = inherit
        
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
        return ast.explist

    def visitFuncCall(self, ast, param):
        name = ast.name
        args = ast.args
        for ele in param:
            if name == ele.name and ele.typ == "FunctionType":
                if ele.rtn_typ == "VoidType":
                    raise TypeMismatchInExpression(ast)
                # TODO Xem lai coi so arg khac so para thi loi gi
                if len(args) != len(ele.paraList):
                    raise TypeMismatchInExpression(ast)
                for i in range(len(args)):
                    arg = self.visit(args[i], [])
                    para = ele.paraList[i][1]
                    if arg != para:
                        if para == "FloatType" and arg == "IntegerType":
                            continue
                        raise TypeMismatchInExpression(args[i])
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
            
        param += [VariableDeclaration(name, typ, array_typ, dim)]
        
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
            # TODO Xem lai TypeMismatchInVarDecl quang o dau
                if typ == "IntegerType":
                    if initValue != "IntegerType":
                        raise TypeMismatchInExpression(init)
                elif typ == "FloatType":
                    if initValue != "IntegerType" and initValue != "FloatType":
                        raise TypeMismatchInExpression(init)
                elif typ == "BooleanType":
                    if initValue != "BooleanType":
                        raise TypeMismatchInExpression(init)
                elif typ == "StringType":
                    if initValue != "StringType":
                        raise TypeMismatchInExpression(init)
                elif typ == "ArrayType":
                    tempArr = []
                    for exp in initValue:
                        ele = self.visit(exp, param)
                        tempArr.append(ele)
                    for i in range(len(tempArr) - 1):
                        if tempArr[i] != tempArr[i + 1]:
                            if tempArr[i] != array_typ: 
                                raise IllegalArrayLiteral(initValue[i])
                            elif tempArr[i + 1] != array_typ:
                                raise IllegalArrayLiteral(initValue[i + 1])
                    if tempArr[0] != array_typ:
                        raise TypeMismatchInExpression(init)
                elif typ == "AutoType":
                    if initValue == "AutoType":
                        raise TypeMismatchInExpression(init)
                    param[-1].typ = initValue
        else:
            if typ == "AutoType":
                raise Invalid(Variable(), name)
    
    def visitParamDecl(self, ast, param):
        name = ast.name
        typ, array_typ, dim = self.visit(ast.typ, [])
        out = ast.out
        inherit = ast.inherit
        
        for ele in param:
            if name == ele.name and ele.typ != "FunctionType":
                raise Redeclared(Parameter(), name)
        
        param += [ParameterDeclaration(name, typ, array_typ, dim, out, inherit)]
        
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
            for ele in param:
                if inherit == ele.name and ele.typ == "FunctionType":
                    inheritList = ele.paraList
                    break
            else:
                raise Undeclared(Function(), name)
            tempList = []
            if params:
                for para in params:
                    self.visit(para, tempList)
            paraList = []
            for i in tempList:
                paraList += [[i.name, i.typ, i.inherit]]
            for i in range(len(inheritList)):
                for j in range(len(paraList)):
                    if inheritList[i][0] == paraList[j][0]:
                        # TODO Xem lai keyword inherit o parameter
                        if paraList[j][2]:
                            if inheritList[i][1] != paraList[j][1]:
                                raise Invalid(Parameter(), paraList[j][0])
                        else:
                            raise Invalid(Parameter(), paraList[j][0])
                        
            accessibleList = []
            for i in param:
                if i.typ == "FunctionType":
                    accessibleList += [[i.name, i.rtn_typ]]
                else:
                    accessibleList += [[i.name, i.typ]]
            
            accessibleList += inheritList + paraList
        else:
            tempList = []
            if params:
                for para in params:
                    self.visit(para, tempList)
            paraList = []
            for i in tempList:
                paraList += [[i.name, i.typ]]
        
            accessibleList = []
            for i in param:
                if i.typ == "FunctionType":
                    accessibleList += [[i.name, i.rtn_typ]]
                else:
                    accessibleList += [[i.name, i.typ]]
            
            accessibleList += paraList
        
        # TODO rtn_typ la auto
        
        bodyList = []
        for ele in self.visit(body, []):
            self.visit(ele, bodyList)    
        
        if len(bodyList) > 0:
            print(bodyList[1].name)
        
        param += [FunctionDeclaration(name, "FunctionType", rtn_typ, array_typ, dim, inherit, paraList, accessibleList)]
        
    def visitProgram(self, ast, param):
        for decl in ast.decls:
            self.visit(decl, param)
        
        # for ele in param:
        #     print(f"Name: {ele.name}")
        #     print(f"Type: {ele.typ}")
        #     if ele.typ == "FunctionType":
        #         print(f"Return type: {ele.rtn_typ}")
        #         print(f"Parameter List: {ele.paraList}")
        #         print(f"Accessible List: {ele.accessibleList}")
        #     print("////////////////////////////////////////////////////")