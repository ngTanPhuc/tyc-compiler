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

    # program: decl_list EOF;
    def visitProgram(self, ctx):
        return super().visitProgram(ctx)
    
    def visitDecl_list(self, ctx):
        return super().visitDecl_list(ctx)
    
    def visitDecl(self, ctx):
        return super().visitDecl(ctx)
    
    def visitStruct_decl(self, ctx):
        return super().visitStruct_decl(ctx)
    
    def visitMember_list(self, ctx):
        return super().visitMember_list(ctx)
    
    def visitMember(self, ctx):
        return super().visitMember(ctx)
    
    def visitFunc_decl(self, ctx):
        return super().visitFunc_decl(ctx)
    
    def visitParam_decl(self, ctx):
        return super().visitParam_decl(ctx)
    
    def visitParam_list(self, ctx):
        return super().visitParam_list(ctx)
    
    def visitParam_prime(self, ctx):
        return super().visitParam_prime(ctx)
    
    def visitParam(self, ctx):
        return super().visitParam(ctx)

    def visitBody(self, ctx):
        return super().visitBody(ctx)
    
    def visitStmt_list(self, ctx):
        return super().visitStmt_list(ctx)
    
    def visitStmt_prime(self, ctx):
        return super().visitStmt_prime(ctx)
    
    def visitStmt(self, ctx):
        return super().visitStmt(ctx)
    
    def visitVar_decl(self, ctx):
        return super().visitVar_decl(ctx)
    
    def visitBlock_stmt(self, ctx):
        return super().visitBlock_stmt(ctx)
    
    def visitIf_stmt(self, ctx):
        return super().visitIf_stmt(ctx)
    
    def visitWhl_stmt(self, ctx):
        return super().visitWhl_stmt(ctx)
    
    def visitFor_stmt(self, ctx):
        return super().visitFor_stmt(ctx)
    
    def visitFor_init(self, ctx):
        return super().visitFor_init(ctx)
    
    def visitFor_update(self, ctx):
        return super().visitFor_update(ctx)
    
    def visitFor_assign(self, ctx):
        return super().visitFor_assign(ctx)
    
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
        return super().visitTyp(ctx)
    
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
    


