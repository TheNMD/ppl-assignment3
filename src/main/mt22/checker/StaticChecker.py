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
        
        if leftValue == "AutoType" and rightValue != "AutoType":
            leftValue = rightValue
            for ele in param:
                if type(ele) == VarDecl and left.name == ele.name:
                    if rightValue == "IntegerType":
                        ele.typ = IntegerType()
                    elif rightValue == "FloatType":
                        ele.typ = FloatType()
                    elif rightValue == "BooleanType":
                        ele.typ = BooleanType()
                    elif rightValue == "StringType":
                        ele.typ = StringType()
        elif leftValue != "AutoType" and rightValue == "AutoType":
            rightValue = leftValue
            for ele in param:
                if type(ele) == VarDecl and right.name == ele.name:
                    if leftValue == "IntegerType":
                        ele.typ = IntegerType()
                    elif leftValue == "FloatType":
                        ele.typ = FloatType()
                    elif leftValue == "BooleanType":
                        ele.typ = BooleanType()
                    elif leftValue == "StringType":
                        ele.typ = StringType()

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
            if type(ele) == VarDecl and name == ele.name:
                return str(ele.typ)
        else:
            raise Undeclared(Identifier(), name)
    
    def visitArrayCell(self, ast, param):
        name = ast.name
        cell = ast.cell
        
        for ele in param:
            if type(ele) == VarDecl and name == ele.name:
                if type(ele.typ) == ArrayType:
                    # TODO Xem lai coi so dim cua arraycell khac so dim cua array thi loi gi
                    for i in range(len(cell)):
                        if type(cell[i]) != IntegerLit:
                            raise TypeMismatchInExpression(cell[i])

                    if len(cell) <= len(ele.typ.dimensions):
                        for i in range(len(cell)):
                            if cell[i].val >= int(ele.typ.dimensions[i]) or cell[i].val < 0:
                                raise TypeMismatchInExpression(cell[i])
                        eleList = self.visit(ele.init, param)
                        res = eleList[cell[0].val]
                        for i in range(1, len(cell)):
                            res = res[cell[i].val]
                        return res
                    
                    elif len(cell) > len(ele.typ.dimensions):
                         raise TypeMismatchInExpression(cell[len(ele.typ.dimensions)])

                else:
                    raise TypeMismatchInExpression(Id(name))
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
        eleArr = []
        for exp in expList:
            ele = self.visit(exp, param)
            eleArr.append(ele)
        
        for i in range(len(eleArr) - 1):
            if type(eleArr[i]) == str and type(eleArr[i]) != str:
                raise IllegalArrayLiteral(expList[i + 1])
            elif type(eleArr[i]) != str and type(eleArr[i]) == str:
                raise IllegalArrayLiteral(expList[i + 1])
        
        if type(eleArr[0]) != str:
            for i in range(len(eleArr) - 1):
                if len(eleArr[i]) != len(eleArr[i + 1]):
                    raise TypeMismatchInExpression(expList[i + 1]) 
            
        return eleArr

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
                elif len(args) < len(ele.paraList):
                     raise TypeMismatchInExpression("")
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
        def checkArrayTyp(self, ast, param):
            expList = ast.explist
            eleArr = []
            for exp in expList:
                if type(exp) != ArrayLit:
                    ele = self.visit(exp, param)
                else:
                    ele = checkArrayTyp(self, exp, param)
                eleArr.append(ele)
            for i in range(len(eleArr) - 1):
                if eleArr[i] != eleArr[i + 1]:
                    if eleArr[i] == "IntegerType" and eleArr[i + 1] == "FloatType" or eleArr[i] == "FloatType" and eleArr[i + 1] == "IntegerType":
                        continue
                    raise IllegalArrayLiteral(expList[i + 1])
            for ele in eleArr:
                if ele == "FloatType":
                    return "FloatType"
            return eleArr[0]
        
        def checkArrayDim(array_lit, dim, counter):
            if counter == len(dim):
                return False
            if len(array_lit) == int(dim[counter]):
                if type(array_lit[0]) == str:
                    return True
                else:
                    return checkArrayDim(array_lit[0], dim, counter + 1)
            else:
                return False
            
        def countArrayDim(array_lit):
            if type(array_lit[0]) == str:
                return [len(array_lit)]
            else:
                return [len(array_lit)] + countArrayDim(array_lit[0])
        
        name = ast.name
        typ, array_typ, dim = self.visit(ast.typ, [])
        init = ast.init
        
        for ele in param:
            if type(ele) == VarDecl and name == ele.name:
                raise Redeclared(Variable(), name)
        
        param += [ast]
        
        if init:
            initValue = self.visit(init, param)
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
                dimRes = checkArrayDim(initValue, dim, 0)
                typRes = checkArrayTyp(self, init, param)
                if dimRes == False:
                    raise TypeMismatchInVarDecl(ast)
                if typRes != array_typ:
                    if array_typ == "FloatType": 
                        if typRes != "IntegerType":
                            raise TypeMismatchInVarDecl(ast)
                    else:
                        raise TypeMismatchInVarDecl(ast)
            elif typ == "AutoType":
                if type(initValue) != str:
                    typ = "ArrayType"
                    array_typ = checkArrayTyp(self, init, param)
                    dim = countArrayDim(initValue)
                    for ele in param:
                        if type(ele) == VarDecl and name == ele.name:
                            if array_typ == "IntegerType":
                                ele.typ = ArrayType(dim, IntegerType())
                            elif array_typ == "FloatType":
                                ele.typ = ArrayType(dim, FloatType())
                            elif array_typ == "BooleanType":
                                ele.typ = ArrayType(dim, BooleanType())
                            elif array_typ == "StringType":
                                ele.typ = ArrayType(dim, StringType())
                else:
                    for ele in param:
                        if type(ele) == VarDecl and name == ele.name:
                            if initValue == "IntegerType":
                                ele.typ = IntegerType()
                            elif initValue == "FloatType":
                                ele.typ = FloatType()
                            elif initValue == "BooleanType":
                                ele.typ = BooleanType()
                            elif initValue == "StringType":
                                ele.typ = StringType()
        else:
            if typ == "AutoType":
                raise Invalid(Variable(), name)
    
    def visitParamDecl(self, ast, param):   
        name = ast.name
        typ, array_typ, dim = self.visit(ast.typ, [])
        out = ast.out
        inherit = ast.inherit
        param += [ast]
        
    def visitFuncDecl(self, ast, param):
        name = ast.name
        rtn_typ, array_typ, dim = self.visit(ast.return_type, [])
        params = ast.params
        inherit = ast.inherit
        body = ast.body
        
        paraList = []
        if params:
            for para in params:
                self.visit(para, paraList)
        
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

        bodyList = []
        bodyList += paraList
        for ele in self.visit(body, []):
            bodyList += self.visit(ele, bodyList)    
        
        # if len(bodyList) > 0:
        #     print(bodyList[1].name)
        
        param += [ast]
        
    def visitProgram(self, ast, param):
        # Loop 1
        prototype = []
        for ele in ast.decls:
            if type(ele) == FuncDecl:
                prototype += [ele]

        param = [prototype]

        # Loop 2
        for ele in ast.decls:
            self.visit(ele, param)
            
        # for ele in param:
        #     print(ele)

