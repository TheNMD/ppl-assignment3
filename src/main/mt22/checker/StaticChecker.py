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

        if name == "readInteger":
            if len(args) != 0:
                raise TypeMismatchInExpression(args[0])
            return "VoidType"
        elif name == "printInteger":
            if len(args) == 0:
                raise TypeMismatchInExpression("")
            elif len(args) == 1:
                pass
            elif len(args) > 1:
                raise TypeMismatchInExpression(args[1])
            return "VoidType"
        elif name == "readFloat":
            if len(args) != 0:
                raise TypeMismatchInExpression(args[0])
            return "VoidType"
        elif name == "writeFloat":
            if len(args) == 0:
                raise TypeMismatchInExpression("")
            elif len(args) == 1:
                pass
            elif len(args) > 1:
                raise TypeMismatchInExpression(args[1])
            return "VoidType"
        elif name == "readBoolean":
            if len(args) != 0:
                raise TypeMismatchInExpression(args[0])
            return "VoidType"
        elif name == "printBoolean":
            if len(args) == 0:
                raise TypeMismatchInExpression("")
            elif len(args) == 1:
                pass
            elif len(args) > 1:
                raise TypeMismatchInExpression(args[1])
            return "VoidType"
        elif name == "readString":
            if len(args) != 0:
                raise TypeMismatchInExpression(args[0])
            return "VoidType"
        elif name == "printString":
            if len(args) == 0:
                raise TypeMismatchInExpression("")
            elif len(args) == 1:
                pass
            elif len(args) > 1:
                raise TypeMismatchInExpression(args[1])
            return "VoidType"
        elif name == "super":
            raise TypeMismatchInExpression(ast)
        elif name == "preventDefault":
            raise TypeMismatchInExpression(ast)
        else:
            for idx in param:
                if type(idx) == FuncDecl and name == idx.name:
                    
                    paraList = []
                    if idx.params:
                        for para in idx.params:
                            paraList += [self.visit(para, paraList)]
                    
                    # TODO Xem lai coi so arg khac so para thi loi gi
                    if len(args) == len(paraList):
                        argList = []
                        for i in range(len(args)):
                            argList += [self.visit(args[i], param)]
                        for i in range(len(args)):
                            if paraList[i].out and type(args[i]) != Id:
                                raise TypeMismatchInExpression(args[i])
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
                    
                    if type(idx.return_type) == IntegerType:
                        return "IntegerType"
                    if type(idx.return_type) == FloatType:
                        return "FloatType"
                    if type(idx.return_type) == BooleanType:
                        return "BooleanType"
                    if type(idx.return_type) == StringType:
                        return "StringType"
                    if type(idx.return_type) == ArrayType:
                        return ["ArrayType", idx.return_type.typ, idx.return_type.dimensions]
                    if type(idx.return_type) == AutoType:
                        return "AutoType"
                    elif type(idx.return_type) == VoidType:
                        raise TypeMismatchInExpression(ast)
                    
            else:
                raise Undeclared(Function(), name)
    
    # Statements
    def visitAssignStmt(self, ast, param):
        lhs = ast.lhs
        rhs = ast.rhs

        id = self.visit(lhs, param)
        if type(rhs) == FuncCall:
            value = self.visit(rhs, param + param[-1])
        else:
            value = self.visit(rhs, param)
        if id == "IntegerType":
            if value != "IntegerType":
                if value == "AutoType":
                    if type(rhs) == FuncDecl:
                        for ele in param[-1]:
                            if type(ele) == FuncDecl and rhs.name == ele.name:
                                ele.return_type = IntegerType()
                                break
                    else:
                        for ele in param:
                            if type(ele) == ParamDecl and rhs.name == ele.name:
                                ele.typ = IntegerType()
                                break
                else:
                    raise TypeMismatchInStatement(ast)
        elif id == "FloatType":
            if value != "IntegerType" and value != "FloatType":
                if value == "AutoType":
                    if type(rhs) == FuncDecl:
                        for ele in param[-1]:
                            if type(ele) == FuncDecl and rhs.name == ele.name:
                                ele.return_type = FloatType()
                                break
                    else:
                        for ele in param:
                            if type(ele) == ParamDecl and rhs.name == ele.name:
                                ele.typ = FloatType()
                                break
                else:
                    raise TypeMismatchInStatement(ast)
        elif id == "BooleanType":
            if value != "BooleanType":
                if value == "AutoType":
                    if type(rhs) == FuncDecl:
                        for ele in param[-1]:
                            if type(ele) == FuncDecl and rhs.name == ele.name:
                                ele.return_type = BooleanType()
                                break
                    else:
                        for ele in param:
                            if type(ele) == ParamDecl and rhs.name == ele.name:
                                ele.typ = BooleanType()
                                break
                else:
                    raise TypeMismatchInStatement(ast)
        elif id == "StringType":
            if value != "StringType":
                if value == "AutoType":
                    if type(rhs) == FuncDecl:
                        for ele in param[-1]:
                            if type(ele) == FuncDecl and rhs.name == ele.name:
                                ele.return_type = StringType()
                                break
                    else:
                        for ele in param:
                            if type(ele) == ParamDecl and rhs.name == ele.name:
                                ele.typ = StringType()
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
        if type(local_evn[0]) != VarDecl and type(local_evn[0]) != ParamDecl and type(local_evn[0]) != FuncDecl and type(local_evn[0]) != str:
            local_evn = local_evn[::-1]
        if body:
            for i in range(len(body)):
                if type(body[i]) == VarDecl:
                    for j in range(i + 1, len(body)):
                        if type(body[j]) == VarDecl and body[j].name == body[i].name:
                            raise Redeclared(Variable(), body[j].name)
            
            for ele in body:
                if type(ele) == VarDecl:
                    if type(ele.init) == FuncCall:
                        local_evn.insert(0, self.visit(ele, local_evn + local_evn[-1]))
                    else:
                        local_evn.insert(0, self.visit(ele, local_evn))
                else:
                    self.visit(ele, local_evn)
        
        return ast
    
    def visitIfStmt(self, ast, param):
        cond = ast.cond
        tstmt = ast.tstmt
        fstmt = ast.fstmt
        
        condition = self.visit(cond, param)
        
        if condition != "BooleanType":
            raise TypeMismatchInStatement(ast)
        
        if fstmt:
            try:
                self.visit(tstmt, param)
            except Exception as true_e:
                if type(true_e) == MustInLoop:
                    try:
                        self.visit(fstmt, param)
                    except Exception as false_e:
                        if type(false_e) == MustInLoop:
                            raise true_e
                        else:
                            raise Exception(true_e, false_e)
                    else:
                        raise true_e
                else:
                    raise true_e
            else:
                try:
                    self.visit(fstmt, param)
                except Exception as false_e:
                    raise false_e
                else:
                    return ast
        else:
            try:
                self.visit(tstmt, param)
            except Exception as false_e:
                raise false_e
            else:
                return ast
        
    def visitForStmt(self, ast, param):
        init = ast.init
        cond = ast.cond
        stmt = ast.stmt
        upd = ast.upd
        
        init_rhs = self.visit(init.rhs, param)
        if init_rhs != "IntegerType":
            raise TypeMismatchInStatement(ast)
        init_lhs = VarDecl(init.lhs.name, IntegerType(), init.rhs)

        loop_evn = param.copy()
        loop_evn.insert(0, init_lhs)
        
        condition = self.visit(cond, loop_evn)
        if condition != "BooleanType":
            raise TypeMismatchInStatement(ast)

        try:
            self.visit(stmt, loop_evn)
        except Exception as e:
            if len(e.args) == 2 and type(e.args[0]) == MustInLoop:
                if type(e.args[1]) == Redeclared or type(e.args[1]) == Undeclared or type(e.args[1]) == Invalid or type(e.args[1]) == TypeMismatchInVarDecl or type(e.args[1]) == TypeMismatchInExpression or type(e.args[1]) == TypeMismatchInStatement or type(e.args[1]) == IllegalArrayLiteral or type(e.args[1]) == InvalidStatementInFunction:
                    error = e.args[1]
                else:
                    error = e.args[1].args
                    while type(error[0]) == MustInLoop:
                        if type(error[1]) == Redeclared or type(error[1]) == Undeclared or type(error[1]) == Invalid or type(error[1]) == TypeMismatchInVarDecl or type(error[1]) == TypeMismatchInExpression or type(error[1]) == TypeMismatchInStatement or type(error[1]) == IllegalArrayLiteral or type(error[1]) == InvalidStatementInFunction:
                            error = error[1]
                            break
                        else: 
                            error = error[1].args
                raise error
            else:
                if type(e) == MustInLoop:
                    pass
                else:
                    raise e
        
        update = self.visit(upd, loop_evn)
        if update != "IntegerType":
            raise TypeMismatchInStatement(ast)
        
        return ast
        
    def visitWhileStmt(self, ast, param):
        cond = ast.cond
        stmt = ast.stmt
        
        condition = self.visit(cond, param)
        if condition != "BooleanType":
            raise TypeMismatchInStatement(ast)
        
        try:
            self.visit(stmt, param)
        except Exception as e:
            if len(e.args) == 2 and type(e.args[0]) == MustInLoop:
                if type(e.args[1]) == Redeclared or type(e.args[1]) == Undeclared or type(e.args[1]) == Invalid or type(e.args[1]) == TypeMismatchInVarDecl or type(e.args[1]) == TypeMismatchInExpression or type(e.args[1]) == TypeMismatchInStatement or type(e.args[1]) == IllegalArrayLiteral or type(e.args[1]) == InvalidStatementInFunction:
                    error = e.args[1]
                else:
                    error = e.args[1].args
                    while type(error[0]) == MustInLoop:
                        if type(error[1]) == Redeclared or type(error[1]) == Undeclared or type(error[1]) == Invalid or type(error[1]) == TypeMismatchInVarDecl or type(error[1]) == TypeMismatchInExpression or type(error[1]) == TypeMismatchInStatement or type(error[1]) == IllegalArrayLiteral or type(error[1]) == InvalidStatementInFunction:
                            error = error[1]
                            break
                        else: 
                            error = error[1].args
                raise error
            else:
                if type(e) == MustInLoop:
                    pass
                else:
                    raise e

        return ast
    
    def visitDoWhileStmt(self, ast, param):
        cond = ast.cond
        stmt = ast.stmt
        
        try:
            self.visit(stmt, param)
        except Exception as e:
            if len(e.args) == 2 and type(e.args[0]) == MustInLoop:
                if type(e.args[1]) == Redeclared or type(e.args[1]) == Undeclared or type(e.args[1]) == Invalid or type(e.args[1]) == TypeMismatchInVarDecl or type(e.args[1]) == TypeMismatchInExpression or type(e.args[1]) == TypeMismatchInStatement or type(e.args[1]) == IllegalArrayLiteral or type(e.args[1]) == InvalidStatementInFunction:
                    error = e.args[1]
                else:
                    error = e.args[1].args
                    while type(error[0]) == MustInLoop:
                        if type(error[1]) == Redeclared or type(error[1]) == Undeclared or type(error[1]) == Invalid or type(error[1]) == TypeMismatchInVarDecl or type(error[1]) == TypeMismatchInExpression or type(error[1]) == TypeMismatchInStatement or type(error[1]) == IllegalArrayLiteral or type(error[1]) == InvalidStatementInFunction:
                            error = error[1]
                            break
                        else: 
                            error = error[1].args
                raise error
            else:
                if type(e) == MustInLoop:
                    pass
                else:
                    raise e
                
        condition = self.visit(cond, param)
        if condition != "BooleanType":
            raise TypeMismatchInStatement(ast)
    
        return ast
    
    def visitBreakStmt(self, ast, param):
        raise MustInLoop(ast)
    
    def visitContinueStmt(self, ast, param):
        raise MustInLoop(ast)
    
    def visitReturnStmt(self, ast, param):
        expr = ast.expr
        
        if expr:
            if type(expr) == FuncCall:
                return_typ = self.visit(expr, param[-1])
            else:
                return_typ = self.visit(expr, param)
        else:
            return_typ = "VoidType"
        
        for ele in param:
            if type(ele) == str:
                name = ele
                break
        for ele in param[-1]:
            if ele.name == name:
                if type(return_typ) == str:
                    if return_typ == "IntegerType":
                        if type(ele.return_type) != IntegerType and type(ele.return_type) != FloatType:
                            if type(ele.return_type) == AutoType:
                                ele.return_type = IntegerType()
                                break
                            else:
                                raise TypeMismatchInStatement(ast)
                    elif return_typ == "FloatType":
                        if type(ele.return_type) != FloatType:
                            if type(ele.return_type) == AutoType:
                                ele.return_type = FloatType()
                                break
                            else:
                                raise TypeMismatchInStatement(ast)
                    elif return_typ == "BooleanType":
                        if type(ele.return_type) != BooleanType:
                            if type(ele.return_type) == AutoType:
                                ele.return_type = BooleanType()
                                break
                            else:
                                raise TypeMismatchInStatement(ast)
                    elif return_typ == "StringType":
                        if type(ele.return_type) != StringType:
                            if type(ele.return_type) == AutoType:
                                ele.return_type = StringType()
                                break
                            else:
                                raise TypeMismatchInStatement(ast)
                    elif return_typ == "AutoType":
                        for idx in param[-1]:
                            if expr.name == idx.name:
                                if type(ele.return_type) == IntegerType:
                                    idx.return_type = IntegerType()
                                elif type(ele.return_type) == FloatType:
                                    idx.return_type = FloatType()
                                elif type(ele.return_type) == BooleanType:
                                    idx.return_type = BooleanType()
                                elif type(ele.return_type) == StringType:
                                    idx.return_type = StringType()
                                break
                    elif return_typ == "VoidType":
                        if type(ele.return_type) != VoidType:
                            if type(ele.return_type) == AutoType:
                                ele.return_type = VoidType()
                                break
                            else:
                                raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
                break

        return ast
    
    def visitCallStmt(self, ast, param):
        name = ast.name
        args = ast.args
        
        
        for idx in param[-1]:
            if name == idx.name:
                paraList = []
                if idx.params:
                    for para in idx.params:
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
                                    for ele in param + param[-1]:
                                        if type(ele) == FuncDecl and args[i].name == ele.name:
                                            ele.return_type = IntegerType()
                                            break
                                else:
                                    raise TypeMismatchInExpression(args[i])
                        elif type(paraList[i].typ) == FloatType:
                            if argList[i] != "IntegerType" and argList[i] != "FloatType":
                                if argList[i] == "AutoType":
                                    for ele in param + param[-1]:
                                        if type(ele) == FuncDecl and args[i].name == ele.name:
                                            ele.return_type = FloatType()
                                            break
                                else:
                                    raise TypeMismatchInExpression(args[i])
                        elif type(paraList[i].typ) == BooleanType:
                            if argList[i] != "BooleanType":
                                if argList[i] == "AutoType":
                                    for ele in param + param[-1]:
                                        if type(ele) == FuncDecl and args[i].name == ele.name:
                                            ele.return_type = BooleanType()
                                            break
                                else:
                                    raise TypeMismatchInExpression(args[i])
                        elif type(paraList[i].typ) == StringType:
                            if argList[i] != "StringType":
                                if argList[i] == "AutoType":
                                    for ele in param + param[-1]:
                                        if type(ele) == FuncDecl and args[i].name == ele.name:
                                            ele.return_type = StringType()
                                            break
                                else:
                                    raise TypeMismatchInExpression(args[i])
                        elif type(paraList[i].typ) == ArrayType:
                            raise TypeMismatchInExpression(args[i])
                        elif type(paraList[i].typ) == AutoType:
                            for ele in param + param[-1]:
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
                            pass
                    
                elif len(args) > len(paraList):
                    raise TypeMismatchInExpression(args[len(paraList)])
                elif len(args) < len(paraList):
                     raise TypeMismatchInExpression("")

                if type(idx.return_type) == AutoType:
                    idx.return_type = VoidType()
                break
                
        else:
            raise Undeclared(Function(), name)

        return ast
        
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
                            elif type(ele) == ParamDecl and init.name == ele.name:
                                ele.typ = IntegerType()
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
                            elif type(ele) == ParamDecl and init.name == ele.name:
                                ele.typ = FloatType()
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
                            elif type(ele) == ParamDecl and init.name == ele.name:
                                ele.typ = BooleanType()
                                break
                    else: 
                        raise TypeMismatchInVarDecl(ast)
            elif typ == "StringType":
                if initValue != "StringType":
                    if initValue == "AutoType":
                        for ele in param:
                            if type(ele) == FuncDecl and init.name == ele.name:
                                ele.return_type = StringType()
                                break
                            elif type(ele) == ParamDecl and init.name == ele.name:
                                ele.typ = StringType()
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
                        elif type(ele) == ParamDecl and init.name == ele.name:
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
                    parent = ele
                    break
            else:
                raise Undeclared(Function(), inherit)
            
            fist_stmt = body.body[0]
            if parent.params:
                if type(fist_stmt) == FuncCall:
                    if fist_stmt.name == "super":
                        pass
                    else:
                        raise InvalidStatementInFunction(name)
                else:
                    raise InvalidStatementInFunction(name)
            else:
                print(fist_stmt)
            
            for body_ele in body.body:  
                if type(body_ele) == VarDecl:
                    for para_ele in paraList:
                        if para_ele.name == body_ele.name:
                            raise Redeclared(Variable(), body_ele.name)
        else:
            for body_ele in body.body:  
                if type(body_ele) == VarDecl:
                    for para_ele in paraList:
                        if para_ele.name == body_ele.name:
                            raise Redeclared(Variable(), body_ele.name)
            try:
                self.visit(body, param + paraList + [name])
            except Exception as e:
                if len(e.args) == 2 and type(e.args[0]) == MustInLoop:
                    raise e.args[0]
                else:
                    raise e

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
        
        # print(param[2].return_type)
        # print(param[1].params[0].typ)
        
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

