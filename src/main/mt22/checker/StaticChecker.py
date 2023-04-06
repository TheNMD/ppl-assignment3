from Visitor import Visitor


class StaticChecker(Visitor):
    
    def visitProgram(self,ctx:Visitor.visitProgram,o:object):
        obj = []
        for decl in ctx.decl:
            obj += [self.visit(decl, obj)]
            
    def visitVarDecl(self,ctx:Visitor.visitVarDecl,o:object):
        name = ctx.name
        if name in o:
            raise Redeclared(name)
        return name