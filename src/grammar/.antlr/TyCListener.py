# Generated from /home/phuc/PPL/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TyCParser import TyCParser
else:
    from TyCParser import TyCParser

# This class defines a complete listener for a parse tree produced by TyCParser.
class TyCListener(ParseTreeListener):

    # Enter a parse tree produced by TyCParser#program.
    def enterProgram(self, ctx:TyCParser.ProgramContext):
        pass

    # Exit a parse tree produced by TyCParser#program.
    def exitProgram(self, ctx:TyCParser.ProgramContext):
        pass


    # Enter a parse tree produced by TyCParser#decl_list.
    def enterDecl_list(self, ctx:TyCParser.Decl_listContext):
        pass

    # Exit a parse tree produced by TyCParser#decl_list.
    def exitDecl_list(self, ctx:TyCParser.Decl_listContext):
        pass


    # Enter a parse tree produced by TyCParser#decl.
    def enterDecl(self, ctx:TyCParser.DeclContext):
        pass

    # Exit a parse tree produced by TyCParser#decl.
    def exitDecl(self, ctx:TyCParser.DeclContext):
        pass


    # Enter a parse tree produced by TyCParser#struct_decl.
    def enterStruct_decl(self, ctx:TyCParser.Struct_declContext):
        pass

    # Exit a parse tree produced by TyCParser#struct_decl.
    def exitStruct_decl(self, ctx:TyCParser.Struct_declContext):
        pass


    # Enter a parse tree produced by TyCParser#member_list.
    def enterMember_list(self, ctx:TyCParser.Member_listContext):
        pass

    # Exit a parse tree produced by TyCParser#member_list.
    def exitMember_list(self, ctx:TyCParser.Member_listContext):
        pass


    # Enter a parse tree produced by TyCParser#member.
    def enterMember(self, ctx:TyCParser.MemberContext):
        pass

    # Exit a parse tree produced by TyCParser#member.
    def exitMember(self, ctx:TyCParser.MemberContext):
        pass


    # Enter a parse tree produced by TyCParser#func_decl.
    def enterFunc_decl(self, ctx:TyCParser.Func_declContext):
        pass

    # Exit a parse tree produced by TyCParser#func_decl.
    def exitFunc_decl(self, ctx:TyCParser.Func_declContext):
        pass


    # Enter a parse tree produced by TyCParser#param_decl.
    def enterParam_decl(self, ctx:TyCParser.Param_declContext):
        pass

    # Exit a parse tree produced by TyCParser#param_decl.
    def exitParam_decl(self, ctx:TyCParser.Param_declContext):
        pass


    # Enter a parse tree produced by TyCParser#param_list.
    def enterParam_list(self, ctx:TyCParser.Param_listContext):
        pass

    # Exit a parse tree produced by TyCParser#param_list.
    def exitParam_list(self, ctx:TyCParser.Param_listContext):
        pass


    # Enter a parse tree produced by TyCParser#param_prime.
    def enterParam_prime(self, ctx:TyCParser.Param_primeContext):
        pass

    # Exit a parse tree produced by TyCParser#param_prime.
    def exitParam_prime(self, ctx:TyCParser.Param_primeContext):
        pass


    # Enter a parse tree produced by TyCParser#param.
    def enterParam(self, ctx:TyCParser.ParamContext):
        pass

    # Exit a parse tree produced by TyCParser#param.
    def exitParam(self, ctx:TyCParser.ParamContext):
        pass


    # Enter a parse tree produced by TyCParser#body.
    def enterBody(self, ctx:TyCParser.BodyContext):
        pass

    # Exit a parse tree produced by TyCParser#body.
    def exitBody(self, ctx:TyCParser.BodyContext):
        pass


    # Enter a parse tree produced by TyCParser#stmt_list.
    def enterStmt_list(self, ctx:TyCParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by TyCParser#stmt_list.
    def exitStmt_list(self, ctx:TyCParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by TyCParser#stmt_prime.
    def enterStmt_prime(self, ctx:TyCParser.Stmt_primeContext):
        pass

    # Exit a parse tree produced by TyCParser#stmt_prime.
    def exitStmt_prime(self, ctx:TyCParser.Stmt_primeContext):
        pass


    # Enter a parse tree produced by TyCParser#stmt.
    def enterStmt(self, ctx:TyCParser.StmtContext):
        pass

    # Exit a parse tree produced by TyCParser#stmt.
    def exitStmt(self, ctx:TyCParser.StmtContext):
        pass


    # Enter a parse tree produced by TyCParser#var_decl.
    def enterVar_decl(self, ctx:TyCParser.Var_declContext):
        pass

    # Exit a parse tree produced by TyCParser#var_decl.
    def exitVar_decl(self, ctx:TyCParser.Var_declContext):
        pass


    # Enter a parse tree produced by TyCParser#block_stmt.
    def enterBlock_stmt(self, ctx:TyCParser.Block_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#block_stmt.
    def exitBlock_stmt(self, ctx:TyCParser.Block_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#if_stmt.
    def enterIf_stmt(self, ctx:TyCParser.If_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#if_stmt.
    def exitIf_stmt(self, ctx:TyCParser.If_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#whl_stmt.
    def enterWhl_stmt(self, ctx:TyCParser.Whl_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#whl_stmt.
    def exitWhl_stmt(self, ctx:TyCParser.Whl_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#for_stmt.
    def enterFor_stmt(self, ctx:TyCParser.For_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#for_stmt.
    def exitFor_stmt(self, ctx:TyCParser.For_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#for_init.
    def enterFor_init(self, ctx:TyCParser.For_initContext):
        pass

    # Exit a parse tree produced by TyCParser#for_init.
    def exitFor_init(self, ctx:TyCParser.For_initContext):
        pass


    # Enter a parse tree produced by TyCParser#for_update.
    def enterFor_update(self, ctx:TyCParser.For_updateContext):
        pass

    # Exit a parse tree produced by TyCParser#for_update.
    def exitFor_update(self, ctx:TyCParser.For_updateContext):
        pass


    # Enter a parse tree produced by TyCParser#for_assign.
    def enterFor_assign(self, ctx:TyCParser.For_assignContext):
        pass

    # Exit a parse tree produced by TyCParser#for_assign.
    def exitFor_assign(self, ctx:TyCParser.For_assignContext):
        pass


    # Enter a parse tree produced by TyCParser#for_increment_decrement.
    def enterFor_increment_decrement(self, ctx:TyCParser.For_increment_decrementContext):
        pass

    # Exit a parse tree produced by TyCParser#for_increment_decrement.
    def exitFor_increment_decrement(self, ctx:TyCParser.For_increment_decrementContext):
        pass


    # Enter a parse tree produced by TyCParser#left_increment_decrement.
    def enterLeft_increment_decrement(self, ctx:TyCParser.Left_increment_decrementContext):
        pass

    # Exit a parse tree produced by TyCParser#left_increment_decrement.
    def exitLeft_increment_decrement(self, ctx:TyCParser.Left_increment_decrementContext):
        pass


    # Enter a parse tree produced by TyCParser#right_increment_decrement.
    def enterRight_increment_decrement(self, ctx:TyCParser.Right_increment_decrementContext):
        pass

    # Exit a parse tree produced by TyCParser#right_increment_decrement.
    def exitRight_increment_decrement(self, ctx:TyCParser.Right_increment_decrementContext):
        pass


    # Enter a parse tree produced by TyCParser#switch_stmt.
    def enterSwitch_stmt(self, ctx:TyCParser.Switch_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#switch_stmt.
    def exitSwitch_stmt(self, ctx:TyCParser.Switch_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#switch_body.
    def enterSwitch_body(self, ctx:TyCParser.Switch_bodyContext):
        pass

    # Exit a parse tree produced by TyCParser#switch_body.
    def exitSwitch_body(self, ctx:TyCParser.Switch_bodyContext):
        pass


    # Enter a parse tree produced by TyCParser#switch_case_list.
    def enterSwitch_case_list(self, ctx:TyCParser.Switch_case_listContext):
        pass

    # Exit a parse tree produced by TyCParser#switch_case_list.
    def exitSwitch_case_list(self, ctx:TyCParser.Switch_case_listContext):
        pass


    # Enter a parse tree produced by TyCParser#switch_case.
    def enterSwitch_case(self, ctx:TyCParser.Switch_caseContext):
        pass

    # Exit a parse tree produced by TyCParser#switch_case.
    def exitSwitch_case(self, ctx:TyCParser.Switch_caseContext):
        pass


    # Enter a parse tree produced by TyCParser#case_expression.
    def enterCase_expression(self, ctx:TyCParser.Case_expressionContext):
        pass

    # Exit a parse tree produced by TyCParser#case_expression.
    def exitCase_expression(self, ctx:TyCParser.Case_expressionContext):
        pass


    # Enter a parse tree produced by TyCParser#switch_default.
    def enterSwitch_default(self, ctx:TyCParser.Switch_defaultContext):
        pass

    # Exit a parse tree produced by TyCParser#switch_default.
    def exitSwitch_default(self, ctx:TyCParser.Switch_defaultContext):
        pass


    # Enter a parse tree produced by TyCParser#break_stmt.
    def enterBreak_stmt(self, ctx:TyCParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#break_stmt.
    def exitBreak_stmt(self, ctx:TyCParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#cont_stmt.
    def enterCont_stmt(self, ctx:TyCParser.Cont_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#cont_stmt.
    def exitCont_stmt(self, ctx:TyCParser.Cont_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#return_stmt.
    def enterReturn_stmt(self, ctx:TyCParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#return_stmt.
    def exitReturn_stmt(self, ctx:TyCParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#expr_stmt.
    def enterExpr_stmt(self, ctx:TyCParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#expr_stmt.
    def exitExpr_stmt(self, ctx:TyCParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#expr.
    def enterExpr(self, ctx:TyCParser.ExprContext):
        pass

    # Exit a parse tree produced by TyCParser#expr.
    def exitExpr(self, ctx:TyCParser.ExprContext):
        pass


    # Enter a parse tree produced by TyCParser#expr1.
    def enterExpr1(self, ctx:TyCParser.Expr1Context):
        pass

    # Exit a parse tree produced by TyCParser#expr1.
    def exitExpr1(self, ctx:TyCParser.Expr1Context):
        pass


    # Enter a parse tree produced by TyCParser#expr2.
    def enterExpr2(self, ctx:TyCParser.Expr2Context):
        pass

    # Exit a parse tree produced by TyCParser#expr2.
    def exitExpr2(self, ctx:TyCParser.Expr2Context):
        pass


    # Enter a parse tree produced by TyCParser#expr3.
    def enterExpr3(self, ctx:TyCParser.Expr3Context):
        pass

    # Exit a parse tree produced by TyCParser#expr3.
    def exitExpr3(self, ctx:TyCParser.Expr3Context):
        pass


    # Enter a parse tree produced by TyCParser#expr4.
    def enterExpr4(self, ctx:TyCParser.Expr4Context):
        pass

    # Exit a parse tree produced by TyCParser#expr4.
    def exitExpr4(self, ctx:TyCParser.Expr4Context):
        pass


    # Enter a parse tree produced by TyCParser#expr5.
    def enterExpr5(self, ctx:TyCParser.Expr5Context):
        pass

    # Exit a parse tree produced by TyCParser#expr5.
    def exitExpr5(self, ctx:TyCParser.Expr5Context):
        pass


    # Enter a parse tree produced by TyCParser#expr6.
    def enterExpr6(self, ctx:TyCParser.Expr6Context):
        pass

    # Exit a parse tree produced by TyCParser#expr6.
    def exitExpr6(self, ctx:TyCParser.Expr6Context):
        pass


    # Enter a parse tree produced by TyCParser#expr7.
    def enterExpr7(self, ctx:TyCParser.Expr7Context):
        pass

    # Exit a parse tree produced by TyCParser#expr7.
    def exitExpr7(self, ctx:TyCParser.Expr7Context):
        pass


    # Enter a parse tree produced by TyCParser#expr8.
    def enterExpr8(self, ctx:TyCParser.Expr8Context):
        pass

    # Exit a parse tree produced by TyCParser#expr8.
    def exitExpr8(self, ctx:TyCParser.Expr8Context):
        pass


    # Enter a parse tree produced by TyCParser#expr9.
    def enterExpr9(self, ctx:TyCParser.Expr9Context):
        pass

    # Exit a parse tree produced by TyCParser#expr9.
    def exitExpr9(self, ctx:TyCParser.Expr9Context):
        pass


    # Enter a parse tree produced by TyCParser#expr10.
    def enterExpr10(self, ctx:TyCParser.Expr10Context):
        pass

    # Exit a parse tree produced by TyCParser#expr10.
    def exitExpr10(self, ctx:TyCParser.Expr10Context):
        pass


    # Enter a parse tree produced by TyCParser#expr_primary.
    def enterExpr_primary(self, ctx:TyCParser.Expr_primaryContext):
        pass

    # Exit a parse tree produced by TyCParser#expr_primary.
    def exitExpr_primary(self, ctx:TyCParser.Expr_primaryContext):
        pass


    # Enter a parse tree produced by TyCParser#typ.
    def enterTyp(self, ctx:TyCParser.TypContext):
        pass

    # Exit a parse tree produced by TyCParser#typ.
    def exitTyp(self, ctx:TyCParser.TypContext):
        pass


    # Enter a parse tree produced by TyCParser#func_call.
    def enterFunc_call(self, ctx:TyCParser.Func_callContext):
        pass

    # Exit a parse tree produced by TyCParser#func_call.
    def exitFunc_call(self, ctx:TyCParser.Func_callContext):
        pass


    # Enter a parse tree produced by TyCParser#arg_list.
    def enterArg_list(self, ctx:TyCParser.Arg_listContext):
        pass

    # Exit a parse tree produced by TyCParser#arg_list.
    def exitArg_list(self, ctx:TyCParser.Arg_listContext):
        pass


    # Enter a parse tree produced by TyCParser#args.
    def enterArgs(self, ctx:TyCParser.ArgsContext):
        pass

    # Exit a parse tree produced by TyCParser#args.
    def exitArgs(self, ctx:TyCParser.ArgsContext):
        pass


    # Enter a parse tree produced by TyCParser#struct_lit.
    def enterStruct_lit(self, ctx:TyCParser.Struct_litContext):
        pass

    # Exit a parse tree produced by TyCParser#struct_lit.
    def exitStruct_lit(self, ctx:TyCParser.Struct_litContext):
        pass


    # Enter a parse tree produced by TyCParser#structmem_list.
    def enterStructmem_list(self, ctx:TyCParser.Structmem_listContext):
        pass

    # Exit a parse tree produced by TyCParser#structmem_list.
    def exitStructmem_list(self, ctx:TyCParser.Structmem_listContext):
        pass



del TyCParser