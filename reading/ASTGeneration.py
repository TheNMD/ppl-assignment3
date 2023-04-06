from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *

class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program([decl for decl in self.visit(ctx.declist())])
    def visitDeclist(self, ctx: MT22Parser.DeclistContext):
        if ctx.declist(): 
            return self.visit(ctx.decl()) + self.visit(ctx.declist())
        return self.visit(ctx.decl())
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.vardecl(): 
            return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())
    
    # Variable declaration
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.middle():
            idvaluelist = [ctx.ID().getText()] + self.visit(ctx.middle()) + [self.visit(ctx.expr())]
            size = len(idvaluelist)
            if size % 2 == 0:
                vartyp = idvaluelist[int(size / 2 - 1)]
                dimenlist = idvaluelist[int(size / 2)]
                res = []
                for i in range(0, int(size / 2 - 1)):
                    id = idvaluelist[i]
                    value = idvaluelist[int(size / 2 + 1 + i)]
                    res += [VarDecl(id, ArrayType(dimenlist, vartyp), value)]
                return res
            else:
                vartyp = idvaluelist[int((size - 1) / 2)]
                res = []
                for i in range(0, int((size - 1) / 2)):
                    id = idvaluelist[i]
                    value = idvaluelist[int((size - 1) / 2 + 1 + i)]
                    res += [VarDecl(id, vartyp, value)]
                return res
        else:
            idlist = self.visit(ctx.idlist())
            vartyp = self.visit(ctx.vartyp())
            if ctx.dimenlist():
                dimenlist = self.visit(ctx.dimenlist())
                return [VarDecl(id, ArrayType(dimenlist, vartyp)) for id in idlist]
            return [VarDecl(id, vartyp) for id in idlist]
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.ids():
            return [ctx.ID().getText()] + self.visit(ctx.ids())
        return [ctx.ID().getText()]
    def visitIds(self, ctx: MT22Parser.IdsContext):
        if ctx.ids():
            return [ctx.ID().getText()] + self.visit(ctx.ids())
        return []
    def visitVartyp(self, ctx: MT22Parser.VartypContext):
        if ctx.KWINT():
            return IntegerType()
        elif ctx.KWFLOAT():
            return FloatType()
        elif ctx.KWBOO():
            return BooleanType()
        elif ctx.KWSTR():
            return StringType()
        return AutoType()
    def visitDimenlist(self, ctx: MT22Parser.DimenlistContext):
        if ctx.dimens():
            return [ctx.LITINT().getText()] + self.visit(ctx.dimens())
        return [ctx.LITINT().getText()]
    def visitDimens(self, ctx: MT22Parser.DimensContext):
        if ctx.dimens():
            return [ctx.LITINT().getText()] + self.visit(ctx.dimens())
        return []
    def visitMiddle(self, ctx: MT22Parser.MiddleContext):
        if ctx.middle():
            return [ctx.ID().getText()] + self.visit(ctx.middle()) + [self.visit(ctx.expr())]
        else:
            if ctx.dimenlist():
                return [self.visit(ctx.vartyp())] + [self.visit(ctx.dimenlist())]
            return [self.visit(ctx.vartyp())]
    
    # Function declaration
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        funcproto = self.visit(ctx.funcproto())
        name = funcproto[0]
        return_typ = funcproto[1]
        params = funcproto[2]
        inherit = funcproto[3]
        dimenlist = funcproto[4]
        body = self.visit(ctx.funcbody())
        if dimenlist:
            return [FuncDecl(name, ArrayType(dimenlist, return_typ), params, inherit, body)]
        return [FuncDecl(name, return_typ, params, inherit, body)]
    def visitFuncproto(self, ctx: MT22Parser.FuncprotoContext):
        name = ctx.ID()[0].getText()
        type = self.visit(ctx.functyp())
        para = self.visit(ctx.paradecl())
        inherit = None
        if ctx.KWINHERIT():
            inherit = ctx.ID()[1].getText()
        dimenlist = None    
        if ctx.dimenlist():
            dimenlist = self.visit(ctx.dimenlist())
        return [name, type, para, inherit, dimenlist]
    def visitFunctyp(self, ctx: MT22Parser.FunctypContext):
        if ctx.KWINT():
            return IntegerType()
        elif ctx.KWFLOAT():
            return FloatType()
        elif ctx.KWBOO():
            return BooleanType()
        elif ctx.KWSTR():
            return StringType()
        elif ctx.KWAUTO():
            return AutoType()
        return VoidType()
    def visitParadecl(self, ctx: MT22Parser.ParadeclContext):
        return self.visit(ctx.paralist())
    def visitParalist(self, ctx: MT22Parser.ParalistContext):
        if ctx.para():
            return self.visit(ctx.para()) + self.visit(ctx.paras())
        return []
    def visitParas(self, ctx: MT22Parser.ParasContext):
        if ctx.para():
            return self.visit(ctx.para()) + self.visit(ctx.paras())
        return []
    def visitPara(self, ctx: MT22Parser.ParaContext):
        name = ctx.ID().getText()
        vartyp = self.visit(ctx.vartyp())
        inherit = False
        if ctx.KWINHERIT():
            inherit = True
        out = False
        if ctx.KWOUT():
            out = True
        if ctx.dimenlist():
            dimenlist = self.visit(ctx.dimenlist())
            return [ParamDecl(name, ArrayType(dimenlist, vartyp), out, inherit)]
        return [ParamDecl(name, vartyp, out, inherit)]
    def visitParalist(self, ctx: MT22Parser.ParalistContext):
        if ctx.para():
            return self.visit(ctx.para()) + self.visit(ctx.paras())
        return []
    def visitFuncbody(self, ctx: MT22Parser.FuncbodyContext):
        return self.visit(ctx.blockstmt())
    def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
        return BlockStmt(self.visit(ctx.bodylist()))
    def visitBodylist(self, ctx: MT22Parser.BodylistContext):
        if ctx.body():
            return self.visit(ctx.body()) + self.visit(ctx.bodylist())
        return []
    def visitBody(self, ctx: MT22Parser.BodyContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.stmt():
            return [self.visit(ctx.stmt())]
        elif ctx.ifstmt():
            return [self.visit(ctx.ifstmt())]
        elif ctx.forstmt():
            return [self.visit(ctx.forstmt())]
        elif ctx.whilestmt():
            return [self.visit(ctx.whilestmt())]
        elif ctx.blockstmt():
            return [self.visit(ctx.blockstmt())]
        return []
    
    # Statements
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        if ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        elif ctx.dowhilestmt():
            return self.visit(ctx.dowhilestmt())
        elif ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        elif ctx.continuestmt():
            return self.visit(ctx.continuestmt())
        elif ctx.rtnstmt():
            return self.visit(ctx.rtnstmt())
        return self.visit(ctx.callstmt())
    def visitIfstmt(self, ctx: MT22Parser.IfstmtContext):
        if ctx.matchstmt():
            return self.visit(ctx.matchstmt())
        return self.visit(ctx.unmatchstmt())
    def visitMatchstmt(self, ctx: MT22Parser.MatchstmtContext):
        if ctx.KWIF():
            cond = self.visit(ctx.expr())
            tstmt = self.visit(ctx.matchstmt()[0])
            fstmt = self.visit(ctx.matchstmt()[1])
            return IfStmt(cond, tstmt, fstmt)
        if ctx.stmt():
            return self.visit(ctx.stmt())
        elif ctx.forstmt():
            return self.visit(ctx.forstmt())
        elif ctx.whilestmt():
            return self.visit(ctx.whilestmt())
        return self.visit(ctx.blockstmt())      
    def visitUnmatchstmt(self, ctx: MT22Parser.UnmatchstmtContext):
        cond = self.visit(ctx.expr())
        if ctx.KWELSE():
            tstmt = self.visit(ctx.matchstmt())
            fstmt = self.visit(ctx.unmatchstmt())
            return IfStmt(cond, tstmt, fstmt)
        tstmt = self.visit(ctx.ifstmt())
        fstmt = None     
        return IfStmt(cond, tstmt, fstmt)
    def visitForstmt(self, ctx: MT22Parser.ForstmtContext): #TODO
        init = self.visit(ctx.assignstmt())
        cond = self.visit(ctx.expr()[0])
        upd = self.visit(ctx.expr()[1])
        if ctx.stmt():
            stmt = self.visit(ctx.stmt())
        elif ctx.ifstmt():
            stmt = self.visit(ctx.ifstmt())
        elif ctx.forstmt():
            stmt = self.visit(ctx.forstmt())
        elif ctx.whilestmt():
            stmt = self.visit(ctx.whilestmt())
        else:
            stmt = self.visit(ctx.blockstmt())
        return ForStmt(init, cond, upd, stmt)
    def visitWhilestmt(self, ctx: MT22Parser.WhilestmtContext):
        cond = self.visit(ctx.expr())
        if ctx.stmt():
            stmt = self.visit(ctx.stmt())
        elif ctx.ifstmt():
            stmt = self.visit(ctx.ifstmt())
        elif ctx.forstmt():
            stmt = self.visit(ctx.forstmt())
        elif ctx.whilestmt():
            stmt = self.visit(ctx.whilestmt())
        else:
            stmt = self.visit(ctx.blockstmt())
        return WhileStmt(cond, stmt)
    def visitAssignstmt(self, ctx: MT22Parser.AssignstmtContext):
        if ctx.idxop(): 
            lhs = ArrayCell(ctx.ID().getText(), self.visit(ctx.idxop()))
        else:
            lhs = Id(ctx.ID().getText())
        rhs = self.visit(ctx.expr())
        return AssignStmt(lhs, rhs)
    def visitDowhilestmt(self, ctx: MT22Parser.DowhilestmtContext):
        cond = self.visit(ctx.expr())
        stmt = self.visit(ctx.blockstmt())
        return DoWhileStmt(cond, stmt)
    def visitBreakstmt(self, ctx: MT22Parser.BreakstmtContext):
        return BreakStmt()
    def visitContinuestmt(self, ctx: MT22Parser.ContinuestmtContext):
        return ContinueStmt()
    def visitRtnstmt(self, ctx: MT22Parser.RtnstmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt()
    def visitCallstmt(self, ctx: MT22Parser.CallstmtContext):
        if ctx.specialfunc():
            namearg = self.visit(ctx.specialfunc())
            return CallStmt(namearg[0], namearg[1])
        name = ctx.ID().getText()
        arg = []
        if ctx.exprlist():
            arg =  self.visit(ctx.exprlist())
        return CallStmt(name, arg)
        
    # Expressions
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.exprs():
            return [self.visit(ctx.expr())] + self.visit(ctx.exprs())
        return [self.visit(ctx.expr())]
    def visitExprs(self, ctx: MT22Parser.ExprsContext):
        if ctx.exprs():
            return [self.visit(ctx.expr())] + self.visit(ctx.exprs())
        return []
    def visitExpr(self, ctx: MT22Parser.ExprContext): #TODO
        if ctx.CONCATOP():
            return BinExpr(ctx.CONCATOP(), self.visit(ctx.expr1()[0]), self.visit(ctx.expr1()[1]))
        return self.visit(ctx.expr1()[0])
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.EQLOP():
            return BinExpr(ctx.EQLOP(), self.visit(ctx.expr2()[0]), self.visit(ctx.expr2()[1])) 
        elif ctx.DIFOP():
            return BinExpr(ctx.DIFOP(), self.visit(ctx.expr2()[0]), self.visit(ctx.expr2()[1])) 
        elif ctx.LARGEOP():
            return BinExpr(ctx.LARGEOP(), self.visit(ctx.expr2()[0]), self.visit(ctx.expr2()[1])) 
        elif ctx.LEQLOP():
            return BinExpr(ctx.LEQLOP(), self.visit(ctx.expr2()[0]), self.visit(ctx.expr2()[1])) 
        elif ctx.SMALLOP():
            return BinExpr(ctx.SMALLOP(), self.visit(ctx.expr2()[0]), self.visit(ctx.expr2()[1])) 
        elif ctx.SEQLOP():
            return BinExpr(ctx.SEQLOP(), self.visit(ctx.expr2()[0]), self.visit(ctx.expr2()[1]))
        return self.visit(ctx.expr2()[0])
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.ANDOP():
            return BinExpr(ctx.ANDOP(), self.visit(ctx.expr2()), self.visit(ctx.expr3())) 
        elif ctx.OROP():
            return BinExpr(ctx.OROP(), self.visit(ctx.expr2()), self.visit(ctx.expr3())) 
        return self.visit(ctx.expr3())
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.ADDOP():
            return BinExpr(ctx.ADDOP(), self.visit(ctx.expr3()), self.visit(ctx.expr4())) 
        elif ctx.SUBOP():
            return BinExpr(ctx.SUBOP(), self.visit(ctx.expr3()), self.visit(ctx.expr4())) 
        return self.visit(ctx.expr4())
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.MULOP():
            return BinExpr(ctx.MULOP(), self.visit(ctx.expr4()), self.visit(ctx.expr5())) 
        elif ctx.DIVOP():
            return BinExpr(ctx.DIVOP(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        elif ctx.MODOP():
            return BinExpr(ctx.MODOP(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))  
        return self.visit(ctx.expr5())
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.EXCOP():
            return UnExpr(ctx.EXCOP(), self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.SUBOP():
            return UnExpr(ctx.SUBOP(), self.visit(ctx.expr6()))
        return self.visit(ctx.operand())
    def visitOperand(self, ctx: MT22Parser.OperandContext):
        if ctx.LITINT():
            return IntegerLit(int(ctx.LITINT().getText()))
        elif ctx.LITFLOAT():
            res = ctx.LITFLOAT().getText()
            if res[0] == "." and (res[1] == "e" or res[1] == "E"):
                return FloatLit(float(0.0))
            return FloatLit(float(res))
        elif ctx.litboo():
            return self.visit(ctx.litboo())
        elif ctx.LITSTR():
            return StringLit(str(ctx.LITSTR().getText()))
        elif ctx.ID():
            if ctx.idxop():
                return ArrayCell(ctx.ID().getText(), self.visit(ctx.idxop()))
            return Id(ctx.ID().getText())
        elif ctx.funccall():
            return self.visit(ctx.funccall())
        elif ctx.subexpr():
            return self.visit(ctx.subexpr())
        elif ctx.litarr():
            return self.visit(ctx.litarr())
        elif ctx.specialfunc():
            namearg = self.visit(ctx.specialfunc())
            return FuncCall(namearg[0], namearg[1])
    def visitLitboo(self, ctx: MT22Parser.LitbooContext):
        if ctx.KWTRUE():
            return BooleanLit(True)
        return BooleanLit(False)
    def visitIdxop(self, ctx: MT22Parser.IdxopContext):
        return self.visit(ctx.celllist())
    def visitCelllist(self, ctx: MT22Parser.CelllistContext):
        if ctx.cells():
            return [self.visit(ctx.expr())] + self.visit(ctx.cells())
        return [self.visit(ctx.expr())]
    def visitCells(self, ctx: MT22Parser.CellsContext):
        if ctx.cells():
            return [self.visit(ctx.expr())] + self.visit(ctx.cells())
        return []
    def visitFunccall(self, ctx: MT22Parser.FunccallContext):
        if ctx.exprlist():
            return FuncCall(ctx.ID().getText(), self.visit(ctx.exprlist()))
        return FuncCall(ctx.ID().getText(), [])
    def visitSubexpr(self, ctx: MT22Parser.SubexprContext):
        return self.visit(ctx.expr())
    def visitLitarr(self, ctx: MT22Parser.LitarrContext):
        if ctx.exprlist():
            return ArrayLit(self.visit(ctx.exprlist()))
        return ArrayLit([])
    def visitSpecialfunc(self, ctx: MT22Parser.SpecialfuncContext):
        name = ctx.getChild(0).getText()
        arg = []
        if ctx.exprlist():
            arg = self.visit(ctx.exprlist())
        return [name, arg]