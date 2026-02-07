"""
AST Generation test cases for TyC compiler.
TODO: Implement 100 test cases for AST generation
"""

import pytest
from tests.utils import ASTGenerator


def test_ast_gen_placeholder():
    """Placeholder test - replace with actual test cases"""
    source = """void main() {
}"""
    # TODO: Add actual test assertions
    # Example:
    # expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    # assert str(ASTGenerator(source).generate()) == expected
    assert True

# *** STRUCT ***
def test_001():
    source = "struct A {int a; float b;};"
    expect = "Program([StructDecl(A, [MemberDecl(IntType(), a), MemberDecl(FloatType(), b)])])"
    assert str(ASTGenerator(source).generate()) == expect

def test_002():
    source = "struct A {};"
    expect = "Program([StructDecl(A, [])])"
    assert str(ASTGenerator(source).generate()) == expect

def test_003():
    source = "struct A {B b; C c; D d;};"
    expect = "Program([StructDecl(A, [MemberDecl(StructType(B), b), MemberDecl(StructType(C), c), MemberDecl(StructType(D), d)])])"
    assert str(ASTGenerator(source).generate()) == expect

def test_004():
    source = "struct User {string name;};"
    expect = "Program([StructDecl(User, [MemberDecl(StringType(), name)])])"
    assert str(ASTGenerator(source).generate()) == expect

def test_005():
    source = """
    struct A { int x; };
    struct B { float y; };
    """
    expect = "Program([StructDecl(A, [MemberDecl(IntType(), x)]), StructDecl(B, [MemberDecl(FloatType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expect

def test_006():
    source = "struct Data {int id; float value; string label;};"
    expect = "Program([StructDecl(Data, [MemberDecl(IntType(), id), MemberDecl(FloatType(), value), MemberDecl(StringType(), label)])])"
    assert str(ASTGenerator(source).generate()) == expect

def test_007():
    source = "struct Vector3 {float x; float y; float z;};"
    expect = "Program([StructDecl(Vector3, [MemberDecl(FloatType(), x), MemberDecl(FloatType(), y), MemberDecl(FloatType(), z)])])"
    assert str(ASTGenerator(source).generate()) == expect

def test_008():
    source = """
    struct Point { float x; float y; };
    struct Rect { Point topLeft; Point bottomRight; };
    """
    expect = "Program([StructDecl(Point, [MemberDecl(FloatType(), x), MemberDecl(FloatType(), y)]), StructDecl(Rect, [MemberDecl(StructType(Point), topLeft), MemberDecl(StructType(Point), bottomRight)])])"
    assert str(ASTGenerator(source).generate()) == expect

def test_009():
    source = "struct Item_1 { int _id; float price_tag2; };"
    expect = "Program([StructDecl(Item_1, [MemberDecl(IntType(), _id), MemberDecl(FloatType(), price_tag2)])])"
    assert str(ASTGenerator(source).generate()) == expect

def test_010():
    source = "struct S{int i;float f;};"
    expect = "Program([StructDecl(S, [MemberDecl(IntType(), i), MemberDecl(FloatType(), f)])])"
    assert str(ASTGenerator(source).generate()) == expect

def test_011():
    source = "struct Node { int Node; };"
    expect = "Program([StructDecl(Node, [MemberDecl(IntType(), Node)])])"
    assert str(ASTGenerator(source).generate()) == expect

def test_012():
    source = """
    struct /* comment */ Commented {
        int /* inline */ x; 
        // end of line
        float y;
    };
    """
    expect = "Program([StructDecl(Commented, [MemberDecl(IntType(), x), MemberDecl(FloatType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expect

def test_013():
    source = """
    void main() {
        A a;
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(A), a)]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_014():
    source = """
    void main() {
        A a = {};
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(A), a = StructLiteral({}))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_015():
    source = """
    void main() {
        A a = {1, 2.5, "Hallo Welt"};
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(A), a = StructLiteral({IntLiteral(1), FloatLiteral(2.5), StringLiteral('Hallo Welt')}))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_016():
    source = """
    void main() {
        Point p = {x, y, z};
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p = StructLiteral({Identifier(x), Identifier(y), Identifier(z)}))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_017():
    source = """
    void main() {
        Data d = {10, getInfo()};
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Data), d = StructLiteral({IntLiteral(10), FuncCall(getInfo, [])}))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_018():
    source = """
    void main() {
        Rect r = {{0, 0}, {10, 20}};
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Rect), r = StructLiteral({StructLiteral({IntLiteral(0), IntLiteral(0)}), StructLiteral({IntLiteral(10), IntLiteral(20)})}))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_019():
    source = """
    void main() {
        Wrapper w = {{{1}, 2}, 3};
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Wrapper), w = StructLiteral({StructLiteral({StructLiteral({IntLiteral(1)}), IntLiteral(2)}), IntLiteral(3)}))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_020():
    source = """
    void main() {
        Complex c = {a, 1, foo(x, "test")};
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Complex), c = StructLiteral({Identifier(a), IntLiteral(1), FuncCall(foo, [Identifier(x), StringLiteral('test')])}))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_021():
    source = """
    struct B {
        A a;
        string C;
    };
    
    void main() {
        B b = {{1, 2.8}, "hello world"};
    }
    """
    expect = "Program([StructDecl(B, [MemberDecl(StructType(A), a), MemberDecl(StringType(), C)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(B), b = StructLiteral({StructLiteral({IntLiteral(1), FloatLiteral(2.8)}), StringLiteral('hello world')}))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_022():
    source = """
    struct Point {int x; int y;};
    Point createPoint() {
        Point p = {1, 2};
        return p;
    }
    """
    expect = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), FuncDecl(StructType(Point), createPoint, [], BlockStmt([VarDecl(StructType(Point), p = StructLiteral({IntLiteral(1), IntLiteral(2)})), ReturnStmt(return Identifier(p))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_023():
    source = """
    void foo() {}
    void main() {}
    """
    expect = "Program([FuncDecl(VoidType(), foo, [], BlockStmt([])), FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_024():
    source = """
    void foo(int x, float y) {} 
    """
    expect = "Program([FuncDecl(VoidType(), foo, [Param(IntType(), x), Param(FloatType(), y)], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_025():
    source = """
    foo(int a, float b) {
        return a + b;
    }
    """
    # ! Note: nodes.py FuncDecl prints "auto" when return_type is None
    expect = "Program([FuncDecl(auto, foo, [Param(IntType(), a), Param(FloatType(), b)], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), +, Identifier(b)))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_026():
    source = """
    struct A {int x; int y;};
    A foo() {
        A a = {1, 2};
        return a;
    }
    """
    expect = "Program([StructDecl(A, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), FuncDecl(StructType(A), foo, [], BlockStmt([VarDecl(StructType(A), a = StructLiteral({IntLiteral(1), IntLiteral(2)})), ReturnStmt(return Identifier(a))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_027():
    source = """
    struct A {int x; int y;};
    float foo(A a) {}
    """
    expect = "Program([StructDecl(A, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), FuncDecl(FloatType(), foo, [Param(StructType(A), a)], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_028():
    source = """
    void main() { 
        // This is a line comment
        /* This is a block comment */
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_029():
    source = ""
    expect = "Program([])"
    assert str(ASTGenerator(source).generate()) == expect

def test_030():
    source = "void foo(int x, float y, string z) {}"
    expect = "Program([FuncDecl(VoidType(), foo, [Param(IntType(), x), Param(FloatType(), y), Param(StringType(), z)], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_031():
    source = """
    void main() {
        
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_032():
    source = "int add(int a, int b) { return a + b; }"
    expect = "Program([FuncDecl(IntType(), add, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), +, Identifier(b)))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_033():
    source = "string getName() { return \"TyC\"; }"
    expect = "Program([FuncDecl(StringType(), getName, [], BlockStmt([ReturnStmt(return StringLiteral('TyC'))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_034():
    source = "void stop() { return; }"
    expect = "Program([FuncDecl(VoidType(), stop, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_035():
    source = "int identity(int x) { return x; }"
    expect = "Program([FuncDecl(IntType(), identity, [Param(IntType(), x)], BlockStmt([ReturnStmt(return Identifier(x))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_036():
    source = """
    int fn1() {}
    float fn2() {}
    """
    expect = "Program([FuncDecl(IntType(), fn1, [], BlockStmt([])), FuncDecl(FloatType(), fn2, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_037():
    source = """
    void process() {
        int x = 10;
        x = x + 1;
    }
    """
    expect = "Program([FuncDecl(VoidType(), process, [], BlockStmt([VarDecl(IntType(), x = IntLiteral(10)), ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1))))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_038():
    source = "void weirdo(int creep) {}"
    expect = "Program([FuncDecl(VoidType(), weirdo, [Param(IntType(), creep)], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_039():
    source = """
    int fact(int n) {
        return n * fact(n - 1);
    }
    """
    expect = "Program([FuncDecl(IntType(), fact, [Param(IntType(), n)], BlockStmt([ReturnStmt(return BinaryOp(Identifier(n), *, FuncCall(fact, [BinaryOp(Identifier(n), -, IntLiteral(1))])))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_040():
    source = """
    struct Box { int id; };
    Box unbox(Box b) { return b; }
    """
    expect = "Program([StructDecl(Box, [MemberDecl(IntType(), id)]), FuncDecl(StructType(Box), unbox, [Param(StructType(Box), b)], BlockStmt([ReturnStmt(return Identifier(b))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_041():
    source = "void main(int argc, string argv) {}"
    expect = "Program([FuncDecl(VoidType(), main, [Param(IntType(), argc), Param(StringType(), argv)], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_042():
    source = "void many(int a, int b, int c, int d) {}"
    expect = "Program([FuncDecl(VoidType(), many, [Param(IntType(), a), Param(IntType(), b), Param(IntType(), c), Param(IntType(), d)], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_043():
    source = "int f(int x){return x;}"
    expect = "Program([FuncDecl(IntType(), f, [Param(IntType(), x)], BlockStmt([ReturnStmt(return Identifier(x))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_044():
    source = """
    void main() {
        int x;
        float y;
        string z;
        auto a;
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x), VarDecl(FloatType(), y), VarDecl(StringType(), z), VarDecl(auto, a)]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_045():
    source = """
    void main() {
        int x = -1;
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x = PrefixOp(-IntLiteral(1)))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_046():
    source = """
    void main() {
        int x = 5;
        float y = 2.8;
        string z = "Hello World";
    }
    """
    # Note: 2.8 is FloatLiteral(2.8)
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x = IntLiteral(5)), VarDecl(FloatType(), y = FloatLiteral(2.8)), VarDecl(StringType(), z = StringLiteral('Hello World'))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_047():
    source = """
    void main() {
        auto a = x + 1 - y;
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, a = BinaryOp(BinaryOp(Identifier(x), +, IntLiteral(1)), -, Identifier(y)))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_048():
    source = """
    void main() {
        A a = {{1, 2}, "Hello World", {2.8, 2}};
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(A), a = StructLiteral({StructLiteral({IntLiteral(1), IntLiteral(2)}), StringLiteral('Hello World'), StructLiteral({FloatLiteral(2.8), IntLiteral(2)})}))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_049():
    source = """
    void main() {
        int x = 2;
        {
            float x = 2.0;
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x = IntLiteral(2)), BlockStmt([VarDecl(FloatType(), x = FloatLiteral(2.0))])]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_050():
    source = """
    void main() {
        if (x < 1) foo("ehe");
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if BinaryOp(Identifier(x), <, IntLiteral(1)) then ExprStmt(FuncCall(foo, [StringLiteral('ehe')])))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_051():
    source = """
    void main() {
        if (x > 2) foo("ehe"); else foo("teehee");
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(2)) then ExprStmt(FuncCall(foo, [StringLiteral('ehe')])), else ExprStmt(FuncCall(foo, [StringLiteral('teehee')])))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_052():
    source = """
    void main() {
        if (x >= y || x <= z) {
            foo();
        } else {
            goo();
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(x), >=, Identifier(y)), ||, BinaryOp(Identifier(x), <=, Identifier(z))) then BlockStmt([ExprStmt(FuncCall(foo, []))]), else BlockStmt([ExprStmt(FuncCall(goo, []))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_053():
    source = """
    void main() {
        if (x == y) {
            if (x != y) {
                goo();
            }
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if BinaryOp(Identifier(x), ==, Identifier(y)) then BlockStmt([IfStmt(if BinaryOp(Identifier(x), !=, Identifier(y)) then BlockStmt([ExprStmt(FuncCall(goo, []))]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_054():
    source = """
    void main() {
        while (TrueAF) doAFlip();
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while Identifier(TrueAF) do ExprStmt(FuncCall(doAFlip, [])))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_055():
    source = """
    void main() {
        while (i < 10) {
            i++;
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(10)) do BlockStmt([ExprStmt(PostfixOp(Identifier(i)++))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_056():
    source = """
    void main() {
        while (a) {
            while (b) {
            }
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while Identifier(a) do BlockStmt([WhileStmt(while Identifier(b) do BlockStmt([]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_057():
    source = """
    void main() {
        for (; ;) {
            a++;
        }
    }
    """
    # Init is None, Condition is None, Update is None
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for None; None; None do BlockStmt([ExprStmt(PostfixOp(Identifier(a)++))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_058():
    source = """
    void main() {
        for (i; i < 10; i++) {
            foo();
        }
    }
    """
    # Init: ExprStmt(Identifier(i))
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for ExprStmt(Identifier(i)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(FuncCall(foo, []))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_059():
    source = """
    void main() {
        
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_060():
    source = """
    void main() {
        for (int i = 0; i < 10; i++) {
            foo();
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(FuncCall(foo, []))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_061():
    source = """
    void main() {
        
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_062():
    source = """
    void main() {
        for (i = 0; i < 10; i++) {
            foo();
        }
    }
    """
    # Init is ExprStmt containing AssignExpr
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(FuncCall(foo, []))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_063():
    source = """
    void main() {
        for (int i = 0; ; i++) {
            foo();
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); None; PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(FuncCall(foo, []))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_064():
    source = """
    void main() {
        auto x;
        x = 1 + 1;
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, x), ExprStmt(AssignExpr(Identifier(x) = BinaryOp(IntLiteral(1), +, IntLiteral(1))))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_065():
    source = """
    void main() {
        int x = 1;
        {
            int x = 2;
        }
        x = 3;
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x = IntLiteral(1)), BlockStmt([VarDecl(IntType(), x = IntLiteral(2))]), ExprStmt(AssignExpr(Identifier(x) = IntLiteral(3)))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_066():
    source = """
    void main() {
        for (int i = 0; i < 10; i = 12) {
            foo();
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = IntLiteral(12)) do BlockStmt([ExprStmt(FuncCall(foo, []))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_067():
    source = """
    void main() {
        for (int i = 0; i < 10; i++) {
            foo();
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(FuncCall(foo, []))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_068():
    source = """
    void main() {
        for (int i = 0; i < 10; --i) {
            foo();
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PrefixOp(--Identifier(i)) do BlockStmt([ExprStmt(FuncCall(foo, []))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_069():
    source = """
    void main() {
        for (int i = 0; i < 10; i = goo(i)) {
            foo();
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = FuncCall(goo, [Identifier(i)])) do BlockStmt([ExprStmt(FuncCall(foo, []))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_070():
    source = """
    void main() {
        for (int i = 0; i < 10; i = x && y) {
            foo();
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(x), &&, Identifier(y))) do BlockStmt([ExprStmt(FuncCall(foo, []))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_071():
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
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(foo, []))]), CaseStmt(case IntLiteral(2): [ExprStmt(FuncCall(goo, []))])])]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_072():
    source = """
    void main() {
        switch (x) {
            case 1: foo();
            case 2: goo();
            default: hoo();
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(foo, []))]), CaseStmt(case IntLiteral(2): [ExprStmt(FuncCall(goo, []))])], default DefaultStmt(default: [ExprStmt(FuncCall(hoo, []))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_073():
    source = """
    void main() {
        switch (x) {
            case 28: foo();
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(28): [ExprStmt(FuncCall(foo, []))])])]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_074():
    source = """
    void main() {
        switch (x) {
            case +28: foo();
        }
    }
    """
    # !Note: +28 is typically parsed as IntLiteral(28) unless unary plus is explicit
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(28): [ExprStmt(FuncCall(foo, []))])])]))])"
    assert str(ASTGenerator(source).generate()) == expect
    assert str(ASTGenerator(source).generate()) == expect

def test_075():
    source = """
    void main() {
        switch (x) {
            case -28: foo();
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(-28): [ExprStmt(FuncCall(foo, []))])])]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_076():
    source = """
    void main() {
        switch (x) {
            case (28 + 1): foo();
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case BinaryOp(IntLiteral(28), +, IntLiteral(1)): [ExprStmt(FuncCall(foo, []))])])]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_077():
    source = """
    void main() {
        
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_078():
    source = """
    void main() {
        switch (x) {
            case (x * 2 + 1): foo();
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case BinaryOp(BinaryOp(Identifier(x), *, IntLiteral(2)), +, IntLiteral(1)): [ExprStmt(FuncCall(foo, []))])])]))])"
    assert str(ASTGenerator(source).generate()) == expect
    assert str(ASTGenerator(source).generate()) == expect

def test_079():
    source = """
    void main() {
        switch (x) {
            case 28: foo();
            default: goo();
            case 82: hoo();
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(28): [ExprStmt(FuncCall(foo, []))]), CaseStmt(case IntLiteral(82): [ExprStmt(FuncCall(hoo, []))])], default DefaultStmt(default: [ExprStmt(FuncCall(goo, []))]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_080():
    source = """
    void main() {
        switch (x) {}
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [])]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_081():
    source = """
    void main() {
        switch (x) {
            case 28:
            default:
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(28): [])], default DefaultStmt(default: []))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_082():
    source = """
    void main() {
        switch (x) {
            case 28: foo(); break;
            default:
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(28): [ExprStmt(FuncCall(foo, [])), BreakStmt()])], default DefaultStmt(default: []))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_083():
    source = """
    void main() {
        switch (x) {
            case 28 + 1: default:
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case BinaryOp(IntLiteral(28), +, IntLiteral(1)): [])], default DefaultStmt(default: []))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_084():
    source = """
    void main() {
        for (int i = 0; i < 10; i++) {
            if (i == 2) continue;
        }
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([IfStmt(if BinaryOp(Identifier(i), ==, IntLiteral(2)) then ContinueStmt())]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_085():
    source = """
    float foo() {
        return a + 1;
    }
    """
    expect = "Program([FuncDecl(FloatType(), foo, [], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), +, IntLiteral(1)))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_086():
    source = """
    float foo() {
        return a + 1;
    }
    """
    expect = "Program([FuncDecl(FloatType(), foo, [], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), +, IntLiteral(1)))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_087():
    source = """
    void main() {
        return;
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_088():
    source = """
    void main() {
        
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_089():
    source = """
    void main() {
        42;
        "Hello World";
        x == 8;
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(IntLiteral(42)), ExprStmt(StringLiteral('Hello World')), ExprStmt(BinaryOp(Identifier(x), ==, IntLiteral(8)))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_090():
    source = """
    void main() {
        A.a = 1;
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(A).a) = IntLiteral(1)))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_091():
    source = """
    void main() {
        foo(2.8).a = 1;
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(FuncCall(foo, [FloatLiteral(2.8)]).a) = IntLiteral(1)))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_092():
    source = """
    void main() {
        auto ayo = A.a;
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, ayo = MemberAccess(Identifier(A).a))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_093():
    source = """
    void main() {
        foo(A.a);
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, [MemberAccess(Identifier(A).a)]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_094():
    source = """
    void main() {
        A.a++;
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(PostfixOp(MemberAccess(Identifier(A).a)++))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_095():
    source = """
    void main() {
        (A.a).b = "Hello World!";
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(A).a).b) = StringLiteral('Hello World!')))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_096():
    source = """
    void main() {
        rect.topLeft.x = 0;
    }
    """
    # MemberAccess(MemberAccess(rect, "topLeft"), "x")
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(rect).topLeft).x) = IntLiteral(0)))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_097():
    source = """
    void main() {
        foo({2.5, "abc"});
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, [StructLiteral({FloatLiteral(2.5), StringLiteral('abc')})]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_098():
    source = """
    void main() {
        for(A = {1, 2}; A.x < 1; A.x++) {}
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for ExprStmt(AssignExpr(Identifier(A) = StructLiteral({IntLiteral(1), IntLiteral(2)}))); BinaryOp(MemberAccess(Identifier(A).x), <, IntLiteral(1)); PostfixOp(MemberAccess(Identifier(A).x)++) do BlockStmt([]))]))])"
    assert str(ASTGenerator(source).generate()) == expect

def test_099():
    source = """
    void main() {
        a = b = c;
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = Identifier(c))))]))])"
    assert str(ASTGenerator(source).generate()) == expect
    assert str(ASTGenerator(source).generate()) == expect

def test_100():
    source = """
    void main() {
        x = a.b.c;
    }
    """
    expect = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = MemberAccess(MemberAccess(Identifier(a).b).c)))]))])"
    assert str(ASTGenerator(source).generate()) == expect