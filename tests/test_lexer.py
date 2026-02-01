"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer
from src.grammar.lexererr import ErrorToken


def test_lexer_placeholder():
    """Placeholder test - replace with actual test cases"""
    source = "// This is a placeholder test"
    tokenizer = Tokenizer(source)
    # TODO: Add actual test assertions
    assert True

def test_keyword_auto():
    """1. Keyword"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"


def test_operator_assign():
    """2. Operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_separator_semi():
    """3. Separator"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"


def test_integer_single_digit():
    """4. Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"


def test_float_decimal():
    """5. Float literal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"


def test_string_simple():
    """6. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"


def test_identifier_simple():
    """7. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_line_comment():
    """8. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_integer_in_expression():
    """9. Mixed: integers and operator"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"


def test_complex_expression():
    """10. Complex: variable declaration"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"

# *** COMMENT ***
def test_001():
	source = "/* This is a block comment \nHello world! */"
	expect = "<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_002():
	source = "// This is a line comment"
	expect = "<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_003():
	source = "/* This is to test greedy */ abc /* bla bla bla */"
	expect = "abc,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_004():
	source = "/* bla bla bla // bla bla bla will skip everything*/"
	expect = "<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_005():
	source = "// Line comment bla bla bla */ /*"
	expect = "<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_006():
	source = "/* Spanning block comment\nthat goes to a new line hehehe */" 
	expect = "<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_007():
	source = "abc // line comment with an ID"
	expect = "abc,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_008():
	source = "// A line comment and then goes to a newline\n"
	expect = "<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_009():
	source = "// Another line comment and then have a carrigage return\r"
	expect = "<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_010():
	source = "//"
	expect = "<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_011():
	source = "/**/"
	expect = "<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_012():
	source = "// Below this is an ID\nabc"
	expect = "abc,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_013():
	source = "/* 2 * 3 */"
	expect = "<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_014():
	source = "/********/"
	expect = "<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_015():
	source = "/* /* Nested block comment */ */"
	expect = "*,/,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_016():
	source = '"// This is not a comment but a literal string, quote takes over comment"'
	expect = "// This is not a comment but a literal string, quote takes over comment,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

# *** IDENTIFIER ***
def test_017():
	source = "var"
	expect = "var,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_018():
	source = "myVar"
	expect = "myVar,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_019():
	source = "my_var"
	expect = "my_var,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_020():
	source = "_myVar"
	expect = "_myVar,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_021():
	source = "myVar_"
	expect = "myVar_,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_022():
	source = "thisWillBe-threeTokens"
	expect = "thisWillBe,-,threeTokens,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_023():
	source = "_"
	expect = "_,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_024():
	source = "__init__"
	expect = "__init__,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_025():
	source = "If"
	expect = "If,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_026():
	source = "myvar123"
	expect = "myvar123,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_027():
	source = "my123var"
	expect = "my123var,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_028():
	source = "1twoTokens"
	expect = "1,twoTokens,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_029():
	source = "Ho+wheels"
	expect = "Ho,+,wheels,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

# *** KEYWORD ***
def test_030():
	source = "auto break case continue default else float for if int return string struct switch void while"
	expect = "auto,break,case,continue,default,else,float,for,if,int,return,string,struct,switch,void,while,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_031():
	source = "int a = 3;"
	expect = "int,a,=,3,;,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_032():
	source = "elseif"
	expect = "elseif,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_033():
	source = "float2"
	expect = "float2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_034():
	source = '"return;"'
	expect = "return;,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_035():
	source = "if// I get an A in PPL, I will celebrate\n"
	expect = "if,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

# *** OPERATOR ***
def test_036():
	source = "+ - * / % == != < > <= >= || && ! ++ -- = ."
	expect = "+,-,*,/,%,==,!=,<,>,<=,>=,||,&&,!,++,--,=,.,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_037():
	source = "/ *"
	expect = "/,*,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_038():
	source = "* /"
	expect = "*,/,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_039():
	source = "<*"
	expect = "<,*,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_040():
	source = "!===>="
	expect = "!=,==,>=,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_041():
	source = "1-2"
	expect = "1,-,2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_042():
	source = "==="
	expect = "==,=,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_043():
	source = "1+2-3*4/5"
	expect = "1,+,2,-,3,*,4,/,5,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_044():
	source = "1 -2"
	expect = "1,-,2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_045():
	source = "1 - 2"
	expect = "1,-,2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_046():
	source = "+++"
	expect = "++,+,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_047():
	source = "- 1"
	expect = "-,1,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_048():
	source = "-1"
	expect = "-,1,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

# *** SEPARATOR ***
def test_049():
	source = "[ ] { } ( ) ; ,"
	expect = "[,],{,},(,),;,,,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_050():
	source = ";;"
	expect = ";,;,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_051():
	source = "a,b,c;"
	expect = "a,,,b,,,c,;,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_052():
	source = "else{"
	expect = "else,{,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_053():
	source = "{}"
	expect = "{,},<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_054():
	source = "[]"
	expect = "[,],<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_055():
	source = "()"
	expect = "(,),<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_056():
	source = "((a))"
	expect = "(,(,a,),),<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_057():
	source = '"return;"'
	expect = "return;,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_058():
	source = "(int)"
	expect = "(,int,),<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_059():
	source = ")\r"
	expect = "),<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_060():
	source = "\t()"
	expect = "(,),<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

# *** LITERAL ***
def test_061():
	source = "1 2 3 4 5\f"
	expect = "1,2,3,4,5,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_062():
	source = "1 -2 5 3 -12345"
	expect = "1,-,2,5,3,-,12345,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_063():
	source = "1--2"
	expect = "1,--,2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_064():
	source = "123."
	expect = "123.,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_065():
	source = "123var"
	expect = "123,var,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_066():
	source = "99else"
	expect = "99,else,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_067():
	source = "1e1"
	expect = "1e1,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_068():
	source = "007"
	expect = "007,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_069():
	source = "1 2"
	expect = "1,2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_070():
	source = "+1"
	expect = "+,1,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_071():
	source = "1.23"
	expect = "1.23,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_072():
	source = ".0123"
	expect = ".0123,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_073():
	source = "1.010"
	expect = "1.010,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_074():
	source = "1.12E2"
	expect = "1.12E2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_075():
	source = "0.0"
	expect = "0.0,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_076():
	source = "1.5e-10"
	expect = "1.5e-10,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_077():
	source = "1e+2"
	expect = "1e+2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_078():
	source = "1.2.3"
	expect = "1.2,.3,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_079():
	source = "1.2.3."
	expect = "1.2,.3,.,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_080():
	source = "1e"
	expect = "1,e,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_081():
	source = "1.E"
	expect = "1.,E,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_082():
	source = "1..2"
	expect = "1.,.2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_083():
	source = '"Hello World"'
	expect = "Hello World,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_084():
	source = '""'
	expect = ",<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_085():
	source = r'"String with a newline\nA new line"'
	expect = r'String with a newline\nA new line,<EOF>'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_086():
	source = r'"Er sagt \"Hallo Welt\""'
	expect = r'Er sagt \"Hallo Welt\",<EOF>'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_087():
	source = r'"This is a string with a tab \t"'
	expect = r'This is a string with a tab \t,<EOF>'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_088():
	source = '"+"'
	expect = '+,<EOF>'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_089():
	source = r'"\r\n"'
	expect = r'\r\n,<EOF>'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_090():
	source = '"A" "B"'
	expect = 'A,B,<EOF>'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_091():
	source = '// "A string inside a comment"'
	expect = "<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect

# *** ERROR ***
def test_092():
	source = "#"
	expect = "Error Token #"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_093():
	source = "$"
	expect = "Error Token $"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_094():
	source = "int @"
	expect = "int,Error Token @"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_095():
	source = '"This is unclosed string'
	expect = 'Unclosed String: This is unclosed string'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_096():
	source = '"Another unclosed string but with a newline\n'
	expect = 'Unclosed String: Another unclosed string but with a newline'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_097():
	source = '"'
	expect = r'Unclosed String: '
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_098():
	source = r'"Content with \"'
	expect = r'Unclosed String: Content with \"'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_099():
	source = r'"Hello \a"'
	expect = r'Illegal Escape In String: Hello \a"'
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_100():
	source = r'"Space \ "'
	expect = r'Illegal Escape In String: Space \ "'
	assert Tokenizer(source).get_tokens_as_string() == expect

# *** EXTEND TESTCASES ***
def test_101():
	source = "1-2"  # 3 Tokens
	expect = "1,-,2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect
	
def test_102():
  source = "1 -2"  # 2 Tokens
  expect = "1,-,2,<EOF>"
  assert Tokenizer(source).get_tokens_as_string() == expect

def test_103():
	source = "1 - 2"
	expect = "1,-,2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect
	
def test_104():
	source = "1--2"
	expect = "1,--,2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect
	
def test_105():
	source = "1-- 2"
	expect = "1,--,2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect
	
def test_106():
	source = "1 - -2"
	expect = "1,-,-,2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect
	
def test_107():
	source = "---2"
	expect = "--,-,2,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect
	
def test_108():
	source = "+++"
	expect = "++,+,<EOF>"
	assert Tokenizer(source).get_tokens_as_string() == expect
	
