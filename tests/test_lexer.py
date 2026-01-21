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
	expect = "ID,a,EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_004():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_005():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_006():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_007():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_008():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_009():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_010():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_011():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_012():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_013():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_014():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_015():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_016():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_017():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_018():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_019():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_020():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_021():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_022():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_023():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_024():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_025():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_026():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_027():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_028():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_029():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_030():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_031():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_032():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_033():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_034():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_035():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_036():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_037():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_038():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_039():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_040():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_041():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_042():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_043():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_044():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_045():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_046():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_047():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_048():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_049():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_050():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_051():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_052():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_053():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_054():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_055():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_056():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_057():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_058():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_059():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_060():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_061():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_062():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_063():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_064():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_065():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_066():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_067():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_068():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_069():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_070():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_071():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_072():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_073():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_074():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_075():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_076():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_077():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_078():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_079():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_080():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_081():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_082():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_083():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_084():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_085():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_086():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_087():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_088():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_089():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_090():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

def test_091():
	source = ""
	expect = "EOF"
	assert Tokenizer(source).get_tokens_as_string() == expect

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