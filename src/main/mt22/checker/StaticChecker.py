from AST import *
from Visitor import Visitor
from StaticError import *

def checkArrayTyp(self, ast, param):
    expList = ast.explist
    typArr = []
    for exp in expList:
        if type(exp) != ArrayLit:
            ele = self.visit(exp, param)
        else:
            ele = checkArrayTyp(self, exp, param)
        typArr.append(ele)
    for i in range(len(typArr) - 1):
        if typArr[i] != typArr[i + 1]:
            # if typArr[i] == "IntegerType" and typArr[i + 1] == "FloatType" or typArr[i] == "FloatType" and typArr[i + 1] == "IntegerType":
            #     continue
            raise IllegalArrayLiteral(expList[i + 1])
    # for ele in typArr:
    #     if ele == "FloatType":
    #         return "FloatType"
    return typArr[0]
    
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
                if (type(ele) == ParamDecl or type(ele) == FuncDecl) and left.name == ele.name:
                    if rightValue == "IntegerType":
                        ele.typ = IntegerType()
                    elif rightValue == "FloatType":
                        ele.typ = FloatType()
                    elif rightValue == "BooleanType":
                        ele.typ = BooleanType()
                    elif rightValue == "StringType":
                        ele.typ = StringType()
                    break
        elif leftValue != "AutoType" and rightValue == "AutoType":
            rightValue = leftValue
            for ele in param:
                if (type(ele) == FuncDecl or type(ele) == ParamDecl) and right.name == ele.name:
                    if leftValue == "IntegerType":
                        ele.typ = IntegerType()
                    elif leftValue == "FloatType":
                        ele.typ = FloatType()
                    elif leftValue == "BooleanType":
                        ele.typ = BooleanType()
                    elif leftValue == "StringType":
                        ele.typ = StringType()
                    break
        
        if op == "+" or op == "-" or op == "*" or op == "/":
            if leftValue != "IntegerType" and leftValue != "FloatType" and rightValue != "IntegerType" and rightValue != "FloatType":
                raise TypeMismatchInExpression(ast)
            if leftValue != "IntegerType" and leftValue != "FloatType":
                raise TypeMismatchInExpression(left)
            if rightValue != "IntegerType" and rightValue != "FloatType":
                raise TypeMismatchInExpression(right)
            if leftValue == "IntegerType" and rightValue == "IntegerType":
                res = "IntegerType"
            else:
                res = "FloatType"
        elif op == "%":
            if leftValue != "IntegerType" and rightValue != "IntegerType":
                raise TypeMismatchInExpression(ast)
            if leftValue != "IntegerType":
                raise TypeMismatchInExpression(left)
            if rightValue != "IntegerType":
                raise TypeMismatchInExpression(right)
            res = "IntegerType"
        elif op == "&&" or op == "||":
            if leftValue != "BooleanType" and rightValue != "BooleanType":
                raise TypeMismatchInExpression(ast)
            if leftValue != "BooleanType":
                raise TypeMismatchInExpression(left)
            if rightValue != "BooleanType":
                raise TypeMismatchInExpression(right)
            res = "BooleanType"
        elif op == "==" or op == "!=":
            if leftValue != "IntegerType" and leftValue != "BooleanType" and rightValue != "IntegerType" and rightValue != "BooleanType":
                raise TypeMismatchInExpression(ast)
            if leftValue != "IntegerType" and leftValue != "BooleanType":
                raise TypeMismatchInExpression(left)
            if rightValue != "IntegerType" and rightValue != "BooleanType":
                raise TypeMismatchInExpression(right)
            # TODO Xem lai raise loi o left hay right
            if leftValue != rightValue:
                 raise TypeMismatchInExpression(ast)
            res = "BooleanType"
        elif op == "<" or op == ">" or op == "<=" or op == ">=":
            if leftValue != "IntegerType" and leftValue != "FloatType" and rightValue != "IntegerType" and rightValue != "FloatType":
                raise TypeMismatchInExpression(ast)
            if leftValue != "IntegerType" and leftValue != "FloatType":
                raise TypeMismatchInExpression(left)
            if rightValue != "IntegerType" and rightValue != "FloatType":
                raise TypeMismatchInExpression(right)
            res = "BooleanType"
        elif op == "::":
            if leftValue != "StringType" and rightValue != "StringType":
                raise TypeMismatchInExpression(ast)
            if leftValue != "StringType":
                raise TypeMismatchInExpression(left)
            if rightValue != "StringType":
                print(rightValue)
                raise TypeMismatchInExpression(right)
            res = "StringType"
        return res
    
    def visitUnExpr(self, ast, param):
        op = str(ast.op)
        val = ast.val
        
        valValue = self.visit(ast.val, param)

        if op == "-":
            if valValue != "IntegerType" and valValue != "FloatType":
                if valValue == "AutoType":
                    for ele in param:
                        if (type(ele) == FuncDecl or type(ele) == ParamDecl) and val.name == ele.name:
                            ele.typ = IntegerType()
                            break
                    return "IntegerType"
                else:
                    raise TypeMismatchInExpression(val)
            res = valValue
        elif op == "!":
            if valValue != "BooleanType":
                if valValue == "AutoType":
                    for ele in param:
                        if (type(ele) == FuncDecl or type(ele) == ParamDecl) and val.name == ele.name:
                            ele.typ = BooleanType()
                            break
                    return "BooleanType"
                else:
                    raise TypeMismatchInExpression(val)
            res = "BooleanType"
        return res
    
    def visitId(self, ast, param):
        name = ast.name

        for ele in param:
            if (type(ele) == VarDecl or type(ele) == ParamDecl) and name == ele.name:
                if type(ele.typ) == ArrayType:
                    return ["ArrayType", str(ele.typ.typ), ele.typ.dimensions]
                return str(ele.typ)
        else:
            raise Undeclared(Identifier(), name)
    
    def visitArrayCell(self, ast, param):
        name = ast.name
        cell = ast.cell
        
        for ele in param:
            if (type(ele) == VarDecl or type(ele) == ParamDecl) and name == ele.name:
                if type(ele.typ) == ArrayType:
                    for i in range(len(cell)):
                        if type(cell[i]) != IntegerLit:
                            raise TypeMismatchInExpression(cell[i])

                    if len(cell) <= len(ele.typ.dimensions):
                        for i in range(len(cell)):
                            if cell[i].val >= int(ele.typ.dimensions[i]) or cell[i].val < 0:
                                raise TypeMismatchInExpression(cell[i])
                        
                        eleList = self.visit(ele.init, param)
                        typ = eleList[cell[0].val]
                        for i in range(1, len(cell)):
                            typ = typ[cell[i].val]
                        
                        return typ
                    
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
        typArr = []
        for exp in expList:
            typ = self.visit(exp, param)
            typArr.append(typ)
        
        for i in range(len(typArr) - 1):
            if type(typArr[i]) == str and type(typArr[i]) != str:
                raise IllegalArrayLiteral(expList[i + 1])
            elif type(typArr[i]) != str and type(typArr[i]) == str:
                raise IllegalArrayLiteral(expList[i + 1])
        
        if type(typArr[0]) != str:
            for i in range(len(typArr) - 1):
                if len(typArr[i]) != len(typArr[i + 1]):
                    raise TypeMismatchInExpression(expList[i + 1]) 
            
        return typArr

    def visitFuncCall(self, ast, param):
        name = ast.name
        args = ast.args

        for ele in param:
            if type(ele) == FuncDecl and name == ele.name:
                
                paraList = []
                if ele.params:
                    for para in ele.params:
                        paraList += [self.visit(para, paraList)]
                
                # TODO Xem lai coi so arg khac so para thi loi gi
                if len(args) == len(paraList):
                    argList = []
                    for i in range(len(args)):
                        argList += [self.visit(args[i], param)]
                    for i in range(len(args)):
                        if type(paraList[i].typ) == IntegerType:
                            if argList[i] != "IntegerType":
                                if argList[i] == "AutoType":
                                    for ele in param:
                                        if type(ele) == FuncDecl and args[i].name == ele.name:
                                            ele.return_type = IntegerType()
                                            break
                                else:
                                    raise TypeMismatchInExpression(args[i])
                        elif type(paraList[i].typ) == FloatType:
                            if argList[i] != "IntegerType" and argList[i] != "FloatType":
                                if argList[i] == "AutoType":
                                    for ele in param:
                                        if type(ele) == FuncDecl and args[i].name == ele.name:
                                            ele.return_type = FloatType()
                                            break
                                else:
                                    raise TypeMismatchInExpression(args[i])
                        elif type(paraList[i].typ) == BooleanType:
                            if argList[i] != "BooleanType":
                                if argList[i] == "AutoType":
                                    for ele in param:
                                        if type(ele) == FuncDecl and args[i].name == ele.name:
                                            ele.return_type = BooleanType()
                                            break
                                else:
                                    raise TypeMismatchInExpression(args[i])
                        elif type(paraList[i].typ) == StringType:
                            if argList[i] != "StringType":
                                if argList[i] == "AutoType":
                                    for ele in param:
                                        if type(ele) == FuncDecl and args[i].name == ele.name:
                                            ele.return_type = StringType()
                                            break
                                else:
                                    raise TypeMismatchInExpression(args[i])
                        elif type(paraList[i].typ) == ArrayType:
                            raise TypeMismatchInExpression(args[i])
                        elif type(paraList[i].typ) == AutoType:
                            for ele in param:
                                if type(ele) == FuncDecl and name == ele.name:
                                    if type(argList[i]) == str:
                                        if argList[i] == "IntegerType":
                                            ele.params[i].typ = IntegerType()
                                        elif argList[i] == "FloatType":
                                            ele.params[i].typ = FloatType()
                                        elif argList[i] == "BooleanType":
                                            ele.params[i].typ = BooleanType()
                                        elif argList[i] == "StringType":
                                            ele.params[i].typ = StringType()
                                        elif argList[i] == "AutoType": 
                                            pass
                                        elif argList[i] == "VoidType": 
                                            raise TypeMismatchInExpression(args[i])
                                    else:
                                        array_typ = argList[i][1]
                                        dim = argList[i][2]
                                        if array_typ == "IntegerType":
                                            ele.params[i].typ = ArrayType(dim, IntegerType())
                                        elif array_typ == "FloatType":
                                            ele.params[i].typ = ArrayType(dim, FloatType())
                                        elif array_typ == "BooleanType":
                                            ele.params[i].typ = ArrayType(dim, BooleanType())
                                        elif array_typ == "StringType":
                                            ele.params[i].typ = ArrayType(dim, StringType())
                                    break
                        elif type(paraList[i].typ) == VoidType:
                            raise TypeMismatchInExpression(args[i])
                    
                elif len(args) > len(paraList):
                    raise TypeMismatchInExpression(args[len(paraList)])
                elif len(args) < len(paraList):
                     raise TypeMismatchInExpression("")
                 
                if type(ele.return_type) == IntegerType:
                    return "IntegerType"
                if type(ele.return_type) == FloatType:
                    return "FloatType"
                if type(ele.return_type) == BooleanType:
                    return "BooleanType"
                if type(ele.return_type) == StringType:
                    return "StringType"
                if type(ele.return_type) == ArrayType:
                    return ["ArrayType", ele.return_type.typ, ele.return_type.dimensions]
                if type(ele.return_type) == AutoType:
                    return "AutoType"
                elif type(ele.return_type) == VoidType:
                    raise TypeMismatchInExpression(ast)
                
        else:
            raise Undeclared(Function(), name)
    
    # Statements
    def visitAssignStmt(self, ast, param):
        lhs = ast.lhs
        rhs = ast.rhs

        id = self.visit(lhs, param)
        value = self.visit(rhs, param)
        
        if id == "IntegerType":
            if value != "IntegerType":
                if value == "AutoType":
                    for ele in param:
                        if type(ele) == FuncDecl and rhs.name == ele.name:
                            ele.return_type = IntegerType()
                            break
                else:
                    raise TypeMismatchInStatement(ast)
        elif id == "FloatType":
            if value != "IntegerType" and value != "FloatType":
                if value == "AutoType":
                    for ele in param:
                        if type(ele) == FuncDecl and rhs.name == ele.name:
                            ele.return_type = FloatType()
                            break
                else:
                    raise TypeMismatchInStatement(ast)
        elif id == "BooleanType":
            if value != "BooleanType":
                if value == "AutoType":
                    for ele in param:
                        if type(ele) == FuncDecl and rhs.name == ele.name:
                            ele.return_type = BooleanType()
                            break
                else:
                    raise TypeMismatchInStatement(ast)
        elif id == "StringType":
            if value != "StringType":
                if value == "AutoType":
                    for ele in param:
                        if type(ele) == FuncDecl and rhs.name == ele.name:
                            ele.return_type = StringType()
                            break
                else:
                    raise TypeMismatchInStatement(ast)
        elif id == "ArrayType":
            raise TypeMismatchInStatement(ast)
        elif id == "AutoType":
            if type(value) != str:
                array_typ = checkArrayTyp(self, rhs, param)
                dim = countArrayDim(value)
                for ele in param:
                    if type(ele) == ParamDecl and lhs.name == ele.name:
                        if array_typ == "IntegerType":
                            ele.return_type = ArrayType(dim, IntegerType())
                        elif array_typ == "FloatType":
                            ele.return_type = ArrayType(dim, FloatType())
                        elif array_typ == "BooleanType":
                            ele.return_type = ArrayType(dim, BooleanType())
                        elif array_typ == "StringType":
                            ele.return_type = ArrayType(dim, StringType())
                        break
            else:
                for ele in param:
                    if (type(ele) == VarDecl or type(ele) == ParamDecl) and lhs.name == ele.name:
                        if value == "IntegerType":
                            ele.typ = IntegerType()
                        elif value == "FloatType":
                            ele.typ = FloatType()
                        elif value == "BooleanType":
                            ele.typ = BooleanType()
                        elif value == "StringType":
                            ele.typ = StringType()
                        break
        elif id == "VoidType":
            raise TypeMismatchInStatement(ast)
        
        return ast
    
    def visitBlockStmt(self, ast, param):
        body = ast.body
        local_evn = param.copy()
        stmtList = []

        if body:
            for i in range(len(body)):
                if type(body[i]) == VarDecl:
                    for j in range(i + 1, len(body)):
                        if type(body[j]) == VarDecl and body[j].name == body[i].name:
                            raise Redeclared(Variable(), body[j].name)
            
            for ele in body:
                if type(ele) == VarDecl:
                    local_evn += [self.visit(ele, local_evn[::-1])]
                else:
                    stmtList += [self.visit(ele, local_evn[::-1])]
        
        return ast
    
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
        
        if init:
            initValue = self.visit(init, param)
            # TODO Xem lai TypeMismatchInVarDecl raise o ast hay init
            if typ == "IntegerType":
                if initValue != "IntegerType":
                    if initValue == "AutoType":
                        for ele in param:
                            if type(ele) == FuncDecl and init.name == ele.name:
                                ele.return_type = IntegerType()
                                break
                    else:
                        raise TypeMismatchInVarDecl(ast)
            elif typ == "FloatType":
                if initValue != "IntegerType" and initValue != "FloatType":
                    if initValue == "AutoType":
                        for ele in param:
                            if type(ele) == FuncDecl and init.name == ele.name:
                                ele.return_type = FloatType()
                                break
                    else:
                        raise TypeMismatchInVarDecl(ast)
            elif typ == "BooleanType":
                if initValue != "BooleanType":
                    if initValue == "AutoType":
                        for ele in param:
                            if type(ele) == FuncDecl and init.name == ele.name:
                                ele.return_type = BooleanType()
                                break
                    else: 
                        raise TypeMismatchInVarDecl(ast)
            elif typ == "StringType":
                if initValue != "StringType":
                    if initValue == "AutoType":
                        for ele in param:
                            if type(ele) == FuncDecl and init.name == ele.name:
                                ele.return_type = FloatType()
                                break
                    else: 
                        raise TypeMismatchInVarDecl(ast)
            elif typ == "ArrayType":
                if initValue == "AutoType":
                    for ele in param:
                        if type(ele) == FuncDecl and init.name == ele.name:
                            if array_typ == "IntegerType":
                                ele.return_type = ArrayType(dim, IntegerType())
                            elif array_typ == "FloatType":
                                ele.return_type = ArrayType(dim, FloatType())
                            elif array_typ == "BooleanType":
                                ele.return_type = ArrayType(dim, BooleanType())
                            elif array_typ == "StringType":
                                ele.return_type = ArrayType(dim, StringType())
                            break
                else:
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
                    if initValue[0] == "ArrayType":
                        array_typ = initValue[1]
                        dim = initValue[2]
                    else:
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
                            break
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
                            break
            elif typ == "VoidType":
                raise TypeMismatchInVarDecl(ast)
        else:
            if typ == "AutoType":
                raise Invalid(Variable(), name)
        
        return ast
    
    def visitParamDecl(self, ast, param):   
        name = ast.name
        typ, array_typ, dim = self.visit(ast.typ, [])
        out = ast.out
        inherit = ast.inherit
        
        for ele in param:
            if name == ele.name:
                raise Redeclared(Parameter(), name)
        
        return ast
        
    def visitFuncDecl(self, ast, param):
        name = ast.name
        rtn_typ, array_typ, dim = self.visit(ast.return_type, [])
        params = ast.params
        inherit = ast.inherit
        body = ast.body
        
        paraList = []
        if params:
            for para in params:
                paraList += [self.visit(para, paraList)]
                
        if inherit:
            for ele in param[0]:
                if inherit == ele.name:
                    father = ele
                    break
            else:
                raise Undeclared(Function(), name)
            # print(father)
        else:
            
            for body_ele in body.body:  
                if type(body_ele) == VarDecl:
                    for para_ele in paraList:
                        if para_ele.name == body_ele.name:
                            raise Redeclared(Variable(), body_ele.name)
            
            self.visit(body, param + paraList)
                    
        return ast
        
    def visitProgram(self, ast, param):
        # Loop 1
        prototype = []
        for ele in ast.decls:
            if type(ele) == FuncDecl:
                prototype += [ele]
        
        param = [prototype]
        
        for i in range(len(ast.decls)):
            for j in range(i + 1, len(ast.decls)):
                if type(ast.decls[j]) == type(ast.decls[i]) and ast.decls[j].name == ast.decls[i].name:
                    if type(ast.decls[j]) == VarDecl:
                        raise Redeclared(Variable(), ast.decls[j].name)
                    else:
                        raise Redeclared(Function(), ast.decls[j].name)
        
        # Loop 2
        for ele in ast.decls:
            param += [self.visit(ele, param)]
        
        # for ele in prototype:
        #     print(len(ele.params))
        #     if ele.name == "main" and len(ele.params) == 0 and ele.return_type == VoidType():
        #         break
        # else:
        #     raise NoEntryPoint()
        
        # prototype = [FuncDecl0, FuncDecl1, FuncDecl2, ...]
        # param = [prototype, Decl0, Decl1, Decl2, ...]
        # for ele in param:
        #     print(ele)

