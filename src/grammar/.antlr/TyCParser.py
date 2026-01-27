# Generated from /home/phuc/PPL/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,52,10,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,2,0,2,0,0,
        7,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,
        8,1,0,0,0,8,3,1,0,0,0,0
    ]

class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'break'", "'case'", "'continue'", "'default'", 
                     "'else'", "'float'", "'for'", "'if'", "'int'", "'return'", 
                     "'string'", "'struct'", "'switch'", "'void'", "'while'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", 
                     "'++'", "'--'", "'='", "'.'", "'['", "']'", "'{'", 
                     "'}'", "'('", "')'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "WS", "BLOCK_CMT", "LINE_CMT", "AUTO", 
                      "BREAK", "CASE", "CONTINUE", "DEFAULT", "ELSE", "FLOAT", 
                      "FOR", "IF", "INT", "RETURN", "STRING", "STRUCT", 
                      "SWITCH", "VOID", "WHILE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQUAL", "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", 
                      "GREATER_EQUAL", "OR", "AND", "NOT", "INCREMENT", 
                      "DECREMENT", "ASSIGN", "MEMBER_ACCESS", "LSQUARE_BR", 
                      "RSQUARE_BR", "LCURL_BR", "RCURL_BR", "LPAREN", "RPAREN", 
                      "SEMI_COLON", "COMMA", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl_list = 1

    ruleNames =  [ "program", "decl_list" ]

    EOF = Token.EOF
    WS=1
    BLOCK_CMT=2
    LINE_CMT=3
    AUTO=4
    BREAK=5
    CASE=6
    CONTINUE=7
    DEFAULT=8
    ELSE=9
    FLOAT=10
    FOR=11
    IF=12
    INT=13
    RETURN=14
    STRING=15
    STRUCT=16
    SWITCH=17
    VOID=18
    WHILE=19
    ADD=20
    SUB=21
    MUL=22
    DIV=23
    MOD=24
    EQUAL=25
    NOT_EQUAL=26
    LESS=27
    GREATER=28
    LESS_EQUAL=29
    GREATER_EQUAL=30
    OR=31
    AND=32
    NOT=33
    INCREMENT=34
    DECREMENT=35
    ASSIGN=36
    MEMBER_ACCESS=37
    LSQUARE_BR=38
    RSQUARE_BR=39
    LCURL_BR=40
    RCURL_BR=41
    LPAREN=42
    RPAREN=43
    SEMI_COLON=44
    COMMA=45
    INT_LIT=46
    FLOAT_LIT=47
    STRING_LIT=48
    ID=49
    ILLEGAL_ESCAPE=50
    UNCLOSE_STRING=51
    ERROR_CHAR=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(TyCParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.decl_list()
            self.state = 5
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TyCParser.RULE_decl_list




    def decl_list(self):

        localctx = TyCParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





