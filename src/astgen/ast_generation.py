"""
AST Generation module for TyC programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from functools import reduce
from build.TyCVisitor import TyCVisitor
from build.TyCParser import TyCParser
from src.utils.nodes import *


class ASTGeneration(TyCVisitor):
    """AST Generation visitor for TyC language."""

    def visitProgram(self, ctx):
        """ program: decl_list EOF; """
        decl_list = self.visit(ctx.decl_list())  # returns a list
        return Program(decl_list)
    
    def visitDecl_list(self, ctx):
        """ decl_list: decl decl_list | ; """
        if ctx.getChildCount() == 0:
            return []
        else:
            decl = self.visit(ctx.decl())
            return [decl] + self.visit(ctx.decl_list())
    
    def visitDecl(self, ctx):
        """ decl: struct_decl | func_decl; """
        if ctx.struct_decl():
            return self.visit(ctx.struct_decl())
        else:
            return self.visit(ctx.func_decl())
    
    def visitStruct_decl(self, ctx):
        """ struct_decl: STRUCT ID LCURL_BR member_list RCURL_BR SEMI_COLON; """
        name = ctx.ID().getText()
        member_list = self.visit(ctx.member_list)
        return StructDecl(name, member_list)
    
    def visitMember_list(self, ctx):
        """ member_list: member member_list | ; """
        if ctx.getChildCount() == 0:
            return []
        else:
            member = self.visit(ctx.member())
            return [member] + self.visit(ctx.member_list)
    
    def visitMember(self, ctx):
        """ member: typ ID SEMI_COLON; """
        member_type = self.visit(ctx.typ())  # visit typ node and return an instance of class Type in nodes.py
        name = ctx.ID().getText()
        return MemberDecl(member_type, name)
        
    def visitFunc_decl(self, ctx):
        """ func_decl: (typ | VOID | ) ID param_decl body; """
        if ctx.typ():
            return_type = self.visit(ctx.typ())  # visit typ node and return an instance of class Type in nodes.py
        elif ctx.VOID():
            return_type = VoidType()  # this class is declared in nodes.py
        else:
            return_type = None
            
        name = ctx.ID().getText()
        params = self.visit(ctx.param_decl())  # returns a list
        body = self.visit(ctx.body())  # returns the BlockStmt instance
        
        return FuncDecl(return_type, name, params, body)
    
    def visitParam_decl(self, ctx):
        """ param_decl: LPAREN param_list RPAREN; """
        return self.visit(ctx.param_list())  # returns a list
    
    def visitParam_list(self, ctx):
        """ param_list: param_prime | ; """
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.param_prime())
    
    def visitParam_prime(self, ctx):
        """ param_prime: param COMMA param_prime | param; """
        if ctx.COMMA():
            param_list = [self.visit(ctx.param())] + self.visit(ctx.param_prime())
        else:
            param_list = [self.visit(ctx.param())]
        
        return param_list
    
    def visitParam(self, ctx):
        """ param: typ ID; """
        param_type = self.visit(ctx.typ())  # visit typ node and return an instance of class Type in nodes.py
        name = ctx.ID().getText()

        return Param(param_type, name)

    def visitBody(self, ctx):
        """ body: LCURL_BR stmt_list RCURL_BR; """
        stmt_list = self.visit(ctx.stmt_list())  # returns a list
        return BlockStmt(stmt_list)
    
    def visitStmt_list(self, ctx):
        """ stmt_list: stmt_prime | ; """
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.stmt_prime())  # returns a list
    
    def visitStmt_prime(self, ctx):
        """ stmt_prime: stmt stmt_prime | stmt; """
        if ctx.getChildCount() == 1:
            stmt_list = [self.visit(ctx.stmt())]
        else:
            stmt_list = [self.visit(ctx.stmt())] + self.visit(ctx.stmt_prime())
        
        return stmt_list
    
    def visitStmt(self, ctx):
        """ 
        stmt: (
            var_decl 
            | block_stmt 
            | if_stmt 
            | whl_stmt 
            | for_stmt 
            | switch_stmt 
            | break_stmt 
            | cont_stmt 
            | return_stmt 
            | expr_stmt
        );
        """
        return self.visit(ctx.getChild(0))  # return the first (only) child
    
    def visitVar_decl(self, ctx):
        """ var_decl: (typ | AUTO) ID (ASSIGN expr | ) SEMI_COLON; """
        if ctx.typ():
            var_type = self.visit(ctx.typ())  # visit typ node and return an instance of class Type in nodes.py
        elif ctx.AUTO():
            var_type = None
        
        name = ctx.ID().getText()

        if ctx.ASSIGN():
            init_value = self.visit(ctx.expr())  # visit expr node and return an instance of class Expr in nodes.py
        else:
            init_value = None

        return VarDecl(var_type, name, init_value)
    
    def visitBlock_stmt(self, ctx):
        """ block_stmt: LCURL_BR stmt_list RCURL_BR; """
        stmt_list = self.visit(ctx.stmt_list())  # returns a list
        return BlockStmt(stmt_list)
    
    def visitIf_stmt(self, ctx):
        """ if_stmt: IF LPAREN expr RPAREN stmt (ELSE stmt | ); """
        condition = self.visit(ctx.expr())  # returns an instance of type Expr
        if ctx.ELSE():
            then_stmt = self.visit(ctx.stmt(0))  # returns the 1st instance of type Stmt
            else_stmt = self.visit(ctx.stmt(1))  # returns the 2nd instance of type Stmt
        else:
            then_stmt = self.visit(ctx.stmt(0))
            else_stmt = None
        
        return IfStmt(condition, then_stmt, else_stmt)
    
    def visitWhl_stmt(self, ctx):
        """ whl_stmt: WHILE LPAREN expr RPAREN stmt; """
        condition = self.visit(ctx.expr())
        body = self.visit(ctx.stmt())

        return WhileStmt(condition, body)
    
    def visitFor_stmt(self, ctx):
        """ for_stmt: FOR LPAREN for_init (expr | ) SEMI_COLON (for_update | ) RPAREN stmt; """
        init = self.visit(ctx.for_init())  # VarDecl | ExprStmt | None

        if ctx.expr():
            condition = self.visit(ctx.expr())  # returns an instance of type Expr
        else:
            condition = None

        if ctx.for_update():
            update = self.visit(ctx.for_update())  # returns an instace of type Expr
        else:
            update = None

        return ForStmt(init, condition, update)
    
    def visitFor_init(self, ctx):
        """ for_init: var_decl | expr_stmt | SEMI_COLON; """
        if ctx.var_decl():
            return self.visit(ctx.var_decl())  # returns an instance of type VarDecl
        elif ctx.expr_stmt():
            return self.visit(ctx.expr_stmt())  # returns an instance of type ExprStmt
        else:
            return None
    
    def visitFor_update(self, ctx):
        """ for_update: for_assign | for_increment_decrement; """
        if ctx.for_assign():
            return self.visit(ctx.for_assign())  # returns an instance of type Expr
        else:
            return self.visit(ctx.for_increment_decrement())  # returns an instance of type Expr
    
    def visitFor_assign(self, ctx):
        """ for_assign: ID ASSIGN expr; """
        # !!! NOTE: đang làm nửa chừng chỗ: nên xóa for_assign, for_increment_decrement vì <update> của ForStmt trong nodes.py nhận kiểu Expr mà kiểu Expr là lớp cha của tất cả các kiểu Expr
    
    def visitFor_increment_decrement(self, ctx):
        return super().visitFor_increment_decrement(ctx)
    
    def visitLeft_increment_decrement(self, ctx):
        return super().visitLeft_increment_decrement(ctx)
    
    def visitRight_increment_decrement(self, ctx):
        return super().visitRight_increment_decrement(ctx)
    
    def visitSwitch_stmt(self, ctx):
        return super().visitSwitch_stmt(ctx)
    
    def visitSwitch_body(self, ctx):
        return super().visitSwitch_body(ctx)
    
    def visitSwitch_case_list(self, ctx):
        return super().visitSwitch_case_list(ctx)
    
    def visitSwitch_case(self, ctx):
        return super().visitSwitch_case(ctx)
    
    def visitCase_expression(self, ctx):
        return super().visitCase_expression(ctx)
    
    def visitSwitch_default(self, ctx):
        return super().visitSwitch_default(ctx)
    
    def visitBreak_stmt(self, ctx):
        return super().visitBreak_stmt(ctx)
    
    def visitCont_stmt(self, ctx):
        return super().visitCont_stmt(ctx)
    
    def visitReturn_stmt(self, ctx):
        return super().visitReturn_stmt(ctx)
    
    def visitExpr_stmt(self, ctx):
        return super().visitExpr_stmt(ctx)
    
    def visitExpr(self, ctx):
        return super().visitExpr(ctx)
    
    def visitExpr1(self, ctx):
        return super().visitExpr1(ctx)
    
    def visitExpr2(self, ctx):
        return super().visitExpr2(ctx)
    
    def visitExpr3(self, ctx):
        return super().visitExpr3(ctx)
    
    def visitExpr4(self, ctx):
        return super().visitExpr4(ctx)
    
    def visitExpr5(self, ctx):
        return super().visitExpr5(ctx)
    
    def visitExpr6(self, ctx):
        return super().visitExpr6(ctx)
    
    def visitExpr7(self, ctx):
        return super().visitExpr7(ctx)
    
    def visitExpr8(self, ctx):
        return super().visitExpr8(ctx)
    
    def visitExpr9(self, ctx):
        return super().visitExpr9(ctx)
    
    def visitExpr10(self, ctx):
        return super().visitExpr10(ctx)
    
    def visitExpr_primary(self, ctx):
        return super().visitExpr_primary(ctx)
    
    def visitTyp(self, ctx):
        """ typ: INT | FLOAT | STRING | ID; """
        # Returns an instance of the class Type in nodes.py
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        else:
            return StructType(ctx.ID().getText())
    
    def visitFunc_call(self, ctx):
        return super().visitFunc_call(ctx)
    
    def visitArg_list(self, ctx):
        return super().visitArg_list(ctx)

    def visitArgs(self, ctx):
        return super().visitArgs(ctx)

    def visitStruct_lit(self, ctx):
        return super().visitStruct_lit(ctx)

    def visitStructmem_list(self, ctx):
        return super().visitStructmem_list(ctx)
    

