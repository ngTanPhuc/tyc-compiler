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
            update = self.visit(ctx.for_update())  # returns an instace of type Expr (PrefixOp, PostfixOp, or AssignExpr)
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
        """ 
        for_update: for_lhs ASSIGN expr
		| for_lhs (INCREMENT | DECREMENT)
		| (INCREMENT | DECREMENT) for_lhs
		;
        """
        if ctx.ASSIGN():
            lhs = self.visit(ctx.for_lhs())  # returns an instance of type AssignExpr
            rhs = self.visit(ctx.expr())

            return AssignExpr(lhs, rhs)
        elif ctx.getChild(1) == ctx.INCREMENT() or ctx.getChild(1) == ctx.DECREMENT():
            # Postfix unary operation expression (x++, x--)
            operand = self.visit(ctx.for_lhs())  # returns an instance of type Expr
            operator = ctx.getChild(1).getText()
            
            return PostfixOp(operator, operand)
        elif ctx.getChild(0) == ctx.INCREMENT() or ctx.getChild(0) == ctx.DECREMENT():
            # Prefix unary operation expression (++x, --x)
            operator = ctx.getChild(0).getText()
            operand = self.visit(ctx.for_lhs())  # returns an instance of type Expr

            return PrefixOp(operator, operand)
    
    def visitFor_lhs(self, ctx):
        """ for_lhs: ID | expr MEMBER_ACCESS ID; """
        if ctx.MEMBER_ACCESS():  # returns  an instance of type MemberAccess
            obj = self.visit(ctx.expr())
            member = ctx.ID().getText()
            
            return MemberAccess(obj, member)
        else:
            name = ctx.ID().getText()
            return Identifier(name)

    
    def visitSwitch_stmt(self, ctx):
        """ switch_stmt: SWITCH LPAREN expr RPAREN LCURL_BR switch_body RCURL_BR; """
        expr = self.visit(ctx.expr())
        cases = []
        default_case = None

        """ switch_body: switch_case_list (switch_default switch_case_list | ); """
        switch_body = ctx.switch_body()  # NOTE: no need to write visitSwitch_body
        cases += self.visit(switch_body.switch_case_list(0))  # get the first switch_case_list of the switch_body, returns a list
        
        if switch_body.switch_default():  # if the default case is exist
            default_case = self.visit(switch_body.switch_default())  # returns an instance of type DefaultStmt

            # if default exist, then there MIGHT be a 2nd swich_case_list
            if switch_body.switch_case_list(1):
                cases += self.visit(switch_body.switch_case_list(1))
            
        return SwitchStmt(expr, cases, default_case)
    
    # def visitSwitch_body(self, ctx):
    #     return super().visitSwitch_body(ctx)
    
    def visitSwitch_case_list(self, ctx):
        """ switch_case_list: switch_case switch_case_list | ; """
        if ctx.getChildCount() == 0:
            return 0
        else:
            curr_case = self.visit(ctx.switch_case())  # returns an instance of type CaseStmt
            remaining_cases = self.visit(ctx.switch_case_list())

            return [curr_case] + remaining_cases
    
    def visitSwitch_case(self, ctx):
        """ switch_case: CASE case_expression COLON (stmt_list | ); """
        case_expr = self.visit(ctx.case_expression())  # returns an instance of type Expr
        
        if ctx.stmt_list():
            stmt_list = self.visit(ctx.stmt_list())
        else:
            stmt_list = []

        return CaseStmt(case_expr, stmt_list)
    
    def visitCase_expression(self, ctx):
        """ case_expression: (INT_LIT | (ADD | SUB) INT_LIT | LPAREN expr RPAREN | expr); """
        if ctx.INT_LIT():
            val = int(ctx.INT_LIT().getText())
            
            if ctx.SUB():
                val = -val
            
            return IntLiteral(val)
        else:
            return self.visit(ctx.expr())
    
    def visitSwitch_default(self, ctx):
        """ switch_default: DEFAULT COLON (stmt_list | ); """
        if ctx.getChildCount() == 0:
            return None
        else:
            stmt_list = self.visit(ctx.stmt_list())
            
            return DefaultStmt(stmt_list)

    
    def visitBreak_stmt(self, ctx):
        """ break_stmt: BREAK SEMI_COLON; """
        return BreakStmt()
    
    def visitCont_stmt(self, ctx):
        """ cont_stmt: CONTINUE SEMI_COLON; """
        return ContinueStmt()
    
    def visitReturn_stmt(self, ctx):
        """ return_stmt: RETURN (expr | ) SEMI_COLON; """
        if ctx.expr():
            expr = self.visit(ctx.expr())
        else:
            expr = None
        
        return ReturnStmt(expr)
    
    def visitExpr_stmt(self, ctx):
        """ expr_stmt: expr SEMI_COLON; """
        expr = self.visit(ctx.expr())  # returns an instance of type Expr
        return ExprStmt(expr)
    
    def visitExpr(self, ctx):
        """ expr: expr1 ASSIGN expr | expr1; """
        if ctx.ASSIGN():
            lhs = self.visit(ctx.expr1())
            rhs = self.visit(ctx.expr())

            return AssignExpr(lhs, rhs)
        else:
            return self.visit(ctx.expr1())
    
    # Helper function for binary expressions
    def _binary_expr(self, ctx):
        if ctx.getChildCount() == 1:  # recursion
            return self.visit(ctx.getChild(0))  # returns an Expr
        else:
            """ 
            Binary expression stucture: lhs op rhs 
            op: OR | AND, EQUAL | NOT_EQUAL, LESS | LESS_EQUAL | GREATER | GREATER_EQUAL, ADD | SUB, MUL | DIV | MOD
            """
            lhs = self.visit(ctx.getChild(0))  # returns an Expr
            op = ctx.getChild(1).getText()
            rhs = self.visit(ctx.getChild(1))  # returns an Expr

            return BinaryOp(lhs, op, rhs)

    def visitExpr1(self, ctx):
        """ expr: expr1 ASSIGN expr | expr1; """
        return self._binary_expr(ctx)
    
    def visitExpr2(self, ctx):
        """ expr2: expr2 AND expr3 | expr3; """
        return self._binary_expr(ctx)
    
    def visitExpr3(self, ctx):
        """ expr3: expr3 (EQUAL | NOT_EQUAL) expr4 | expr4; """
        return self._binary_expr(ctx)
    
    def visitExpr4(self, ctx):
        """ expr4: expr4 (LESS | LESS_EQUAL | GREATER | GREATER_EQUAL) expr5 | expr5; """
        return self._binary_expr(ctx)
    
    def visitExpr5(self, ctx):
        """ expr5: expr5 (ADD | SUB) expr6 | expr6; """
        return self._binary_expr(ctx)
    
    def visitExpr6(self, ctx):
        """ expr6: expr6 (MUL | DIV | MOD) expr7 | expr7; """
        return self._binary_expr(ctx)

    def visitExpr7(self, ctx):
        """ expr7: (NOT | ADD | SUB) expr7 | expr8; """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        else:
            operator = ctx.getChild(0).getText()
            operand = self.visit(ctx.expr7())  # returns an instance of type Expr

            return PrefixOp(operator, operand)
    
    def visitExpr8(self, ctx):
        """ expr8: (INCREMENT | DECREMENT) expr8 | expr9; """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr9())
        else:
            operator = ctx.getChild(0).getText()
            operand = self.visit(ctx.expr8())  # returns an instance of type Expr

            return PrefixOp(operator, operand)
    
    def visitExpr9(self, ctx):
        """ expr9: expr9 (INCREMENT | DECREMENT) | expr10; """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr10())
        else:
            operator = ctx.getChild(1).getText()
            operand = self.visit(ctx.expr9())  # returns an instance of type Expr

            return PostfixOp(operator, operand)
    
    def visitExpr10(self, ctx):
        """ expr10: expr10 MEMBER_ACCESS ID | expr_primary; """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr_primary())
        else:
            operator = ctx.getChild(1).getText()
            operand = self.visit(ctx.expr10())  # returns an instance of type Expr

            return PostfixOp(operator, operand)
    
    def visitExpr_primary(self, ctx):
        """
        expr_primary: INT_LIT 
                    | FLOAT_LIT 
                    | STRING_LIT 
                    | ID 
                    | LPAREN expr RPAREN 
                    | func_call 
                    | struct_lit;
        """
        if ctx.INT_LIT():
            val = int(ctx.INT_LIT().getText())
            return IntLiteral(val)
        elif ctx.FLOAT_LIT():
            val = float(ctx.FLOAT_LIT())
            return FloatLiteral(val)
        elif ctx.STRING_LIT():
            val = ctx.STRING_LIT().getText()
            return StructLiteral(val)
        elif ctx.ID():
            name = ctx.ID().getText()
            return Identifier(name)
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        elif ctx.struct_lit():
            return self.visit(ctx.struct_lit())
    
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
        """ func_call: ID LPAREN arg_list RPAREN; """
        name = ctx.ID().getText()
        arg_list = self.visit(ctx.arg_list())  # returns a list of Expr
        
        return FuncCall(name, arg_list)
    
    def visitArg_list(self, ctx):
        """ arg_list: args | ; """
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.args())  # return a list of Expr

    def visitArgs(self, ctx):
        if ctx.COMMA():
            curr_arg = self.visit(ctx.expr())  # return an instance of type Expr
            remaining_args = self.visit(ctx.args())  # return a list of 

            return [curr_arg] + remaining_args

    def visitStruct_lit(self, ctx):
        """ struct_lit: LCURL_BR (structmem_list | ) RCURL_BR; """
        if ctx.structmem_list():
            values = self.visit(ctx.structmem_list())  # return a list of Expr
        else:
            values = []
        
        return StructLiteral(values)

    def visitStructmem_list(self, ctx):
        if ctx.COMMA():
            curr_mem_val = self.visit(ctx.expr())  # return an instance of Expr
            remaining_mem_vals = self.visit(ctx.structmem_list())  # return a list of Expr

            return [curr_mem_val] + remaining_mem_vals
        else:
            return [self.visit(ctx.expr())]
    

