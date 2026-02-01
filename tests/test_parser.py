"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


def test_parser_placeholder():
  """Placeholder test - replace with actual test cases"""
  source = "// This is a placeholder test"
  parser = Parser(source)
  # TODO: Add actual test assertions
  assert True
	
def test_empty_program():
    """1. Empty program"""
    assert Parser("").parse() == "success"


def test_program_with_only_main():
    """2. Program with only main function"""
    assert Parser("void main() {}").parse() == "success"


def test_struct_simple():
    """3. Struct declaration"""
    source = "struct Point { int x; int y; };"
    assert Parser(source).parse() == "success"


def test_function_no_params():
    """4. Function with no parameters"""
    source = "void greet() { printString(\"Hello\"); }"
    assert Parser(source).parse() == "success"


def test_var_decl_auto_with_init():
    """5. Variable declaration"""
    source = "void main() { auto x = 5; }"
    assert Parser(source).parse() == "success"


def test_if_simple():
    """6. If statement"""
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_while_simple():
    """7. While statement"""
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_for_simple():
    """8. For statement"""
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_switch_simple():
    """9. Switch statement"""
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert Parser(source).parse() == "success"


def test_assignment_simple():
    """10. Assignment statement"""
    source = "void main() { int x; x = 5; }"
    assert Parser(source).parse() == "success"

# *** OVERALL ***
def test_001():
  source = "void main() {int a = 8;}"
  expect = "success"
  assert Parser(source).parse() == expect

def test_002():
	source = ""
	expect = "success"
	assert Parser(source).parse() == expect

def test_003():
	source = "int main() {}"
	expect = "success"
	assert Parser(source).parse() == expect

def test_004():
	source = "float foo() {int a = 28;}"
	expect = "success"
	assert Parser(source).parse() == expect

def test_005():
	source = "foo() {;}"
	expect = "Error on line 1 col 7: ;"
	assert Parser(source).parse() == expect

# *** STRUCT ***
def test_006():
	source = "struct A {int a; float b;};"
	expect = "success"
	assert Parser(source).parse() == expect

def test_007():
	source = "struct A {};"
	expect = "success"
	assert Parser(source).parse() == expect

def test_008():
	source = "struct A {}"
	expect = "Error on line 1 col 11: <EOF>"
	assert Parser(source).parse() == expect

def test_009():
	source = "struct A {B b; C c; D d;};"
	expect = "success"
	assert Parser(source).parse() == expect

def test_010():
	source = "struct A {auto A;};"
	expect = "Error on line 1 col 10: auto"
	assert Parser(source).parse() == expect

def test_011():
	source = "struct A {struct B {};};"
	expect = "Error on line 1 col 10: struct"
	assert Parser(source).parse() == expect

def test_012():
	source = """
	void main() {
  A a;
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_013():
	source = """
	void main() {
  A a = {1, 2, 3, "abc", b};
  }
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_014():
	source = """
  void main() {
	A a = {};
	}
  """
	expect = "success"
	assert Parser(source).parse() == expect

def test_015():
	source = """
  void main() {
	A a = {b , 1, "abc", 2.8, foo()};
	}
  """
	expect = "success"
	assert Parser(source).parse() == expect

def test_016():
	source = """
  void main() {
	A a = {b , 1, "abc", 2.8, foo(a, b, c, "def")};
	}
  """
	expect = "success"
	assert Parser(source).parse() == expect

def test_017():
	source = """
  void main() {
	A a = {{1, 2}, 3};
	}
  """
	expect = "success"
	assert Parser(source).parse() == expect

def test_018():
	source = """
  void main() {
	A a = {{{}, 2}, 3};
	}
  """
	expect = "success"
	assert Parser(source).parse() == expect

def test_019():
	source = 'struct A {A a = "a"};'
	expect = "Error on line 1 col 14: ="
	assert Parser(source).parse() == expect

def test_020():
	source = "struct A {float;}"
	expect = "Error on line 1 col 15: ;"
	assert Parser(source).parse() == expect

def test_021():
	source = "struct {int a;};"
	expect = "Error on line 1 col 7: {"
	assert Parser(source).parse() == expect

def test_022():
	source = "struct A {int a, y;};"
	expect = "Error on line 1 col 15: ,"
	assert Parser(source).parse() == expect

def test_023():
	source = "struct A {int a; void foo() {};};"
	expect = "Error on line 1 col 17: void"
	assert Parser(source).parse() == expect

def test_024():
	source = "struct A {int a[10];};"
	expect = "Error on line 1 col 15: ["
	assert Parser(source).parse() == expect

def test_025():
	source = "struct A {float while;};"
	expect = "Error on line 1 col 16: while"
	assert Parser(source).parse() == expect

def test_026():
	source = "struct int {int a;}"
	expect = "Error on line 1 col 7: int"
	assert Parser(source).parse() == expect

def test_027():
	source = """
  struct A
	int a;
	float b;
	};
  """
	expect = "Error on line 3 col 1: int"
	assert Parser(source).parse() == expect

def test_028():
	source = """
  struct A {
	// This is a line comment
	/* This is a block comment */
	};
  """
	expect = "success"
	assert Parser(source).parse() == expect

def test_029():
	source = """
  struct A {
	int x;
	float y;
	};
	
	struct B {
	A a;
	string C;
	};
	
	void main() {
	B b = {{1, 2.8}, "hello world"};
	}
  """
	expect = "success"
	assert Parser(source).parse() == expect

def test_030():
	source = "struct A {int a; ;};"
	expect = "Error on line 1 col 17: ;"
	assert Parser(source).parse() == expect

# *** FUNCTION ***
def test_031():
	source = """
  void foo() {}
	void main() {}
  """
	expect = "success"
	assert Parser(source).parse() == expect

def test_032():
	source = """
  void foo(int x, float y) {} 
  """
	expect = "success"
	assert Parser(source).parse() == expect

def test_033():
	source = """
  foo(int a, float b) {
    return a + b;
	}
  """
	expect = "success"
	assert Parser(source).parse() == expect

def test_034():
	source = """
  struct A {int x; int y;};
	A foo() {
    A a = {1, 2};
		return a;
	}
  """
	expect = "success"
	assert Parser(source).parse() == expect

def test_035():
	source = """
  struct A {int x; int y;};
  float foo(A a) {}
  """
	expect = "success"
	assert Parser(source).parse() == expect

def test_036():
	source = """
	void main() { 
	  // This is a line comment
		/* This is a block comment */
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_037():
	source = "void main() { // This is a line comment but on the same line as the bracket}"
	expect = "Error on line 1 col 76: <EOF>"
	assert Parser(source).parse() == expect

def test_038():
	source = "void foo(auto a) {}"
	expect = "Error on line 1 col 9: auto"
	assert Parser(source).parse() == expect

def test_039():
	source = """
  (int x, int y) {
    return x + y;
	}
  """
	expect = "Error on line 2 col 2: ("
	assert Parser(source).parse() == expect

def test_040():
	source = ""
	expect = "success"
	assert Parser(source).parse() == expect

def test_041():
	source = "void main {}"
	expect = "Error on line 1 col 10: {"
	assert Parser(source).parse() == expect

def test_042():
	source = """
  void outer() {
    int inner() {
		}
	}
  """
	expect = "Error on line 3 col 13: ("
	assert Parser(source).parse() == expect

def test_043():
	source = "void main(int x = 8) {}"
	expect = "Error on line 1 col 16: ="
	assert Parser(source).parse() == expect

def test_044():
	source = "void foo(int x, float y, string z) {}"
	expect = "success"
	assert Parser(source).parse() == expect

def test_045():
	source = "void foo(int x)"
	expect = "Error on line 1 col 15: <EOF>"
	assert Parser(source).parse() == expect

def test_046():
	source = "void foo(int a[10]) {}"
	expect = "Error on line 1 col 14: ["
	assert Parser(source).parse() == expect

def test_047():
	source = "int float() {}"
	expect = "Error on line 1 col 4: float"
	assert Parser(source).parse() == expect

def test_048():
	source = "int foo(int, float y) {}"
	expect = "Error on line 1 col 11: ,"
	assert Parser(source).parse() == expect

def test_049():
	source = "int foo(float x; float y) {}"
	expect = "Error on line 1 col 15: ;"
	assert Parser(source).parse() == expect

def test_050():
	source = "int foo() {};"
	expect = "Error on line 1 col 12: ;"
	assert Parser(source).parse() == expect

def test_051():
	source = "int foo(int x, int y,) {}"
	expect = "Error on line 1 col 21: )"
	assert Parser(source).parse() == expect

def test_052():
	source = "auto foo() {}"
	expect = "Error on line 1 col 0: auto"
	assert Parser(source).parse() == expect

# *** STATEMENT ***
def test_053():
	source = """
	void main() {
		int x;
		float y;
		string z;
		auto a;
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_054():
	source = """
	void main() {
		A a;
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_055():
	source = """
	void main() {
		int x = 5;
		float y = -2.8;
		string z = "Hello World";
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_056():
	source = """
	void main() {
		int x = -1;
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_057():
	source = """
	void main() {
		auto a = x + 1 - y;
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_058():
	source = """
	void main() {
		auto x;
		x = 1 + 1;
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_059():
	source = """
	void main() {
		A a = {{1, 2}, "Hello World", {2.8, -2}};
		int x = foo(a);
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_060():
	source = """
	void main() {
		int x = 2;
		int y = -8;
		{
      float x = 2.0;
			float y = .8;
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_061():
	source = """
	void main() {
		int x = 1;
		{
      int x = 2;
			{
        int x = 3;
			}
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_062():
	source = """
	void main() {
		foo();
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_063():
	source = """
	void main() {
		if (x < 1) foo("ehe");
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_064():
	source = """
	void main() {
		if (x > 2) foo("ehe"); else foo("teehee");
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_065():
	source = """
	void main() {
		if (x >= y || x <= z) {
      foo();
		} else {
      goo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_066():
	source = """
	void main() {
		if (x == y && y == z) {
      foo();
			
			if (x != y) {
        goo();
			}
		} else {
      hoo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_067():
	source = """
	void main() {
		if (isCool) {
      print("Hell Yeah!");
		} else {
      print("Nahhh");
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_068():
	source = """
	void main() {
		int x = -2;
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_069():
	source = """
	void main() {
		if (a) foo(); if (b) goo(); else hoo();
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_070():
	source = """
	void main() {
		while (TrueAF) doAFlip();
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_071():
	source = """
	void main() {
		while (notCool) {
      shout("Get out!!!");
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_072():
	source = """
	void main() {
		auto i = 0;
		while (i < 10) {
      count(i);
			i++;
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_073():
	source = """
	void main() {
		while (beingCool) {
      while (doingBackFlip) {
        // empty while
			}
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_074():
	source = """
	void main() {
    while () {}
	}
	"""
	expect = "Error on line 3 col 11: )"
	assert Parser(source).parse() == expect

def test_075():
	source = """
	void main() {
		for (; ;) {
      doNothing();
			a++;
			i = i + 1;
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_076():
	source = """
	void main() {
		int i = 0;
		for (i; i < 10; i++) {
      foo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_077():
	source = """
	void main() {
		for (int i = 0; i < 10; i++) {
      foo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_078():
	source = """
	void main() {
		int i = 1;
		for (i = 0; i < 10; i++) {
      foo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_079():
	source = """
	void main() {
		for (int i = 0; i < 10; ) {
      foo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_080():
	source = """
	void main() {
		for (int i = 0; i < 10; i = 12) {
      foo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_081():
	source = """
	void main() {
		for (int i = 0; i < 10; i++) {
      foo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_082():
	source = """
	void main() {
		for (int i = 0; i < 10; --i) {
      foo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_083():
	source = """
	void main() {
		for (int i = 0; i < 10; i = goo(i)) {
      foo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_084():
	source = """
	void main() {
		for (int i = 0; i < 10; i = x && y) {
      foo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_085():
	source = """
	void main() {
		switch (x) {
      case 1:
        foo();
			case 2:
        goo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_086():
	source = """
	void main() {
		switch (x) {
      case 1:
        foo();
			case 2:
        goo();
			default:
        hoo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_087():
	source = """
	void main() {
		switch (x) {
      case 28:
        foo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_088():
	source = """
	void main() {
		switch (x) {
      case +28:
        foo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_089():
	source = """
	void main() {
		switch (x) {
      case -28:
        foo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_090():
	source = """
	void main() {
		switch (x) {
      case (28 + 1):
        foo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_091():
	source = """
	void main() {
		switch (x) {
      case (x * 2 + 1):
        foo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_092():
	source = """
	void main() {
		switch (x) {
      case 28:
        foo();
			default:
        goo();
			case 82:
        hoo();
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_093():
	source = """
	void main() {
		switch (x) {
      case 28:
        foo();
			default:
        goo();
			default:
        hoo();
		}
	}
	"""
	expect = "Error on line 8 col 3: default"
	assert Parser(source).parse() == expect

def test_094():
	source = """
	void main() {
		switch (x) {}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_095():
	source = """
	void main() {
		switch (x) {
      case 28:
			default:
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_096():
	source = """
	void main() {
		switch (x) {
      case 28:
        foo();
				break;
			case 82:
        goo();
				break;
			default:
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_097():
	source = """
	void main() {
		switch (x) {
      case 28 + 1:
			default:
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_098():
	source = """
	void main() {
		for (int i = 0; i < 10; i++) {
      if (i == 2) continue;
		}
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_099():
	source = """
	float foo() {
		return a + 1;
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect

def test_100():
	source = """
	void main() {
		return;
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect
	
def test_101():
	source = """
	void main() {
		int x = 1;
		42;
		"Hello World";
		foo();
		a = b = c = -1.2;
		x == 8;
		!!a || b && !c;
		point.z;
		++point.z;
	}
	"""
	expect = "success"
	assert Parser(source).parse() == expect
	
def test_102():
	source = """
	void main() {
		;
	}
	"""
	expect = "Error on line 3 col 2: ;"
	assert Parser(source).parse() == expect
	
def test_103():
	source = """
	void main() {
		x +;
	}
	"""
	expect = "Error on line 3 col 5: ;"
	assert Parser(source).parse() == expect