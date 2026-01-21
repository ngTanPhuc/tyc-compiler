"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


def test_lexer_placeholder():
    """Placeholder test - replace with actual test cases"""
    source = "// This is a placeholder test"
    tokenizer = Tokenizer(source)
    # TODO: Add actual test assertions
    assert True

# *** COMMENT ***
def test_001():
	source = "/* This is a block comment \nHello world! */"
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_002():
	source = "// This is a line comment"
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_003():
	source = "/* This is to test greedy */ abc /* bla bla bla */"
	expect = "ID,abc,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_004():
	source = "/* bla bla bla // bla bla bla will skip everything*/"
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_005():
	source = "// Line comment bla bla bla */ /*"
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_006():
	source = "/* Spanning block comment\nthat goes to a new line hehehe */" 
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_007():
	source = "abc // line comment with an ID"
	expect = "ID,abc,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_008():
	source = "// A line comment and then goes to a newline\n"
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_009():
	source = "// Another line comment and then have a carrigage return\r"
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_010():
	source = "//"
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_011():
	source = "/**/"
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_012():
	source = "// Below this is an ID\nabc"
	expect = "ID,abc,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_013():
	source = "/* 2 * 3 */"
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_014():
	source = "/********/"
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_015():
	source = "/* /* Nested block comment */ */"
	expect = "MUL,*,DIV,/,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_016():
	source = '"// This is not a comment but a literal string, quote takes over comment"'
	expect = 'STRING_LIT,"// This is not a comment but a literal string, quote takes over comment",EOF'
	assert Tokenizer(source).get_tokens_as_string() == expect

# *** IDENTIFIER ***
def test_017():
	source = "var"
	expect = "ID,var,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_018():
	source = "myVar"
	expect = "ID,myVar,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_019():
	source = "my_var"
	expect = "ID,my_var,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_020():
	source = "_myVar"
	expect = "ID,_myVar,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_021():
	source = "myVar_"
	expect = "ID,myVar_,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_022():
	source = "thisWillBe-threeTokens"
	expect = "ID,thisWillBe,SUB,-,ID,threeTokens,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_023():
	source = "_"
	expect = "ID,_,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_024():
	source = "__init__"
	expect = "ID,__init__,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_025():
	source = "If"
	expect = "ID,If,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_026():
	source = "myvar123"
	expect = "ID,myvar123,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_027():
	source = "my123var"
	expect = "ID,my123var,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_028():
	source = "1twoTokens"
	expect = "INT_LIT,1,ID,twoTokens,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_029():
	source = "Ho+wheels"
	expect = "ID,Ho,ADD,+,ID,wheels,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

# *** KEYWORD ***
def test_030():
	source = "auto break case continue default else float for if int return string struct switch void while"
	expect = "AUTO,auto,BREAK,break,CASE,case,CONTINUE,continue,DEFAULT,default,ELSE,else,FLOAT,float,FOR,for,IF,if,INT,int,RETURN,return,STRING,string,STRUCT,struct,SWITCH,switch,VOID,void,WHILE,while,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_031():
	source = "int a = 3;"
	expect = "INT,int,ID,a,ASSIGN,=,INT_LIT,3,SEMI_COLON,;,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_032():
	source = "elseif"
	expect = "ID,elseif,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_033():
	source = "float2"
	expect = "ID,float2,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_034():
	source = '"return;"'
	expect = 'STRING_LIT,"return;",EOF'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_035():
	source = "if// I get an A in PPL, I will celebrate\n"
	expect = "IF,if,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

# *** OPERATOR ***
def test_036():
	source = "+ - * / % == != < > <= >= || && ! ++ -- = ."
	expect = "ADD,+,SUB,-,MUL,*,DIV,/,MOD,%,EQUAL,==,NOT_EQUAL,!=,LESS,<,GREATER,>,LESS_EQUAL,<=,GREATER_EQUAL,>=,OR,||,AND,&&,NOT,!,INCREMENT,++,DECREMENT,--,ASSIGN,=,MEMBER_ACCESS,.,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_037():
	source = "/ *"
	expect = "DIV,/,MUL,*,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_038():
	source = "* /"
	expect = "MUL,*,DIV,/,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_039():
	source = "<*"
	expect = "LESS,<,MUL,*,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_040():
	source = "!===>="
	expect = "NOT_EQUAL,!=,EQUAL,==,GREATER_EQUAL,>=,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_041():
	source = "1-2"
	expect = "INT_LIT,1,INT_LIT,-2,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_042():
	source = "==="
	expect = "EQUAL,==,ASSIGN,=,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_043():
	source = "1+2-3*4/5"
	expect = "INT_LIT,1,ADD,+,INT_LIT,2,INT_LIT,-3,MUL,*,INT_LIT,4,DIV,/,INT_LIT,5,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_044():
	source = "1 -2"
	expect = "INT_LIT,1,INT_LIT,-2,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_045():
	source = "1 - 2"
	expect = "INT_LIT,1,SUB,-,INT_LIT,2,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_046():
	source = "+++"
	expect = "INCREMENT,++,ADD,+,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_047():
	source = "- 1"
	expect = "SUB,-,INT_LIT,1,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_048():
	source = "-1"
	expect = "INT_LIT,-1,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

# *** SEPARATOR ***
def test_049():
	source = "[ ] { } ( ) ; ,"
	expect = "LSQUARE_BR,[,RSQUARE_BR,],LCURL_BR,{,RCURL_BR,},LPAREN,(,RPAREN,),SEMI_COLON,;,COMMA,,,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_050():
	source = ";;"
	expect = "SEMI_COLON,;,SEMI_COLON,;,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_051():
	source = "a,b,c;"
	expect = "ID,a,COMMA,,,ID,b,COMMA,,,ID,c,SEMI_COLON,;,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_052():
	source = "else{"
	expect = "ELSE,else,LCURL_BR,{,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_053():
	source = "{}"
	expect = "LCURL_BR,{,RCURL_BR,},EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_054():
	source = "[]"
	expect = "LSQUARE_BR,[,RSQUARE_BR,],EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_055():
	source = "()"
	expect = "LPAREN,(,RPAREN,),EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_056():
	source = "((a))"
	expect = "LPAREN,(,LPAREN,(,ID,a,RPAREN,),RPAREN,),EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_057():
	source = '"return;"'
	expect = 'STRING_LIT,"return;",EOF'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_058():
	source = "(int)"
	expect = "LPAREN,(,INT,int,RPAREN,),EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_059():
	source = ")\r"
	expect = "RPAREN,),EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_060():
	source = "\t()"
	expect = "LPAREN,(,RPAREN,),EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

# *** LITERAL ***
def test_061():
	source = "1 2 3 4 5\f"
	expect = "INT_LIT,1,INT_LIT,2,INT_LIT,3,INT_LIT,4,INT_LIT,5,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_062():
	source = "1 -2 5 3 -12345"
	expect = "INT_LIT,1,INT_LIT,-2,INT_LIT,5,INT_LIT,3,INT_LIT,-12345,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_063():
	source = "1"
	expect = "INT_LIT,1,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_064():
	source = "123."
	expect = "FLOAT_LIT,123.,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_065():
	source = "123var"
	expect = "INT_LIT,123,ID,var,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_066():
	source = "99else"
	expect = "INT_LIT,99,ELSE,else,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_067():
	source = "1e1"
	expect = "FLOAT_LIT,1e1,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_068():
	source = "007"
	expect = "INT_LIT,007,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_069():
	source = "1 2"
	expect = "INT_LIT,1,INT_LIT,2,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_070():
	source = "+1"
	expect = "ADD,+,INT_LIT,1,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_071():
	source = "1.23"
	expect = "FLOAT_LIT,1.23,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_072():
	source = ".0123"
	expect = "FLOAT_LIT,.0123,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_073():
	source = "1.010"
	expect = "FLOAT_LIT,1.010,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_074():
	source = "1.12E2"
	expect = "FLOAT_LIT,1.12E2,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_075():
	source = "0.0"
	expect = "FLOAT_LIT,0.0,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_076():
	source = "1.5e-10"
	expect = "FLOAT_LIT,1.5e-10,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_077():
	source = "1e+2"
	expect = "FLOAT_LIT,1e+2,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_078():
	source = "1.2.3"
	expect = "FLOAT_LIT,1.2,FLOAT_LIT,.3,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_079():
	source = "1.2.3."
	expect = "FLOAT_LIT,1.2,FLOAT_LIT,.3,MEMBER_ACCESS,.,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_080():
	source = "1e"
	expect = "INT_LIT,1,ID,e,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_081():
	source = "1.E"
	expect = "FLOAT_LIT,1.,ID,E,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_082():
	source = "1..2"
	expect = "FLOAT_LIT,1.,FLOAT_LIT,.2,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_083():
	source = '"Hello World"'
	expect = 'STRING_LIT,"Hello World",EOF'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_084():
	source = '""'
	expect = 'STRING_LIT,"",EOF'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_085():
	source = r'"String with a newline\n"'
	expect = 'STRING_LIT,"String with a newline\n",EOF'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_086():
	source = '"Er sagt \"Hallo Welt\""'
	expect = 'STRING_LIT,"Er sagt \"Hallo Welt\"",EOF'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_087():
	source = '"This is a string with a tab \t"'
	expect = 'STRING_LIT,"This is a string with a tab \t",EOF'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_088():
	source = '"+"'
	expect = 'STRING_LIT,"+",EOF'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_089():
	source = '"\r\n"'
	expect = 'STRING_LIT,"\r\n",EOF'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_090():
	source = '"A" "B"'
	expect = 'STRING_LIT,"A",STRING_LIT,"B",EOF'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_091():
	source = '// "A string inside a comment"'
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

# *** ERROR ***
def test_092():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_093():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_094():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_095():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_096():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_097():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_098():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_099():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_100():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect