"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


def test_001():
    source = """
    void main() {
        printString("Hello World");
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_002():
    source = """
    int main() {
        return 0;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_003():
    source = """
    void doNothing() {}
    void main() { doNothing(); }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_004():
    source = """
    // This is a comment
    /* This is a block comment */
    void main() {
        // Comment inside
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_005():
    source = """
    float getPi() { return 3.14; }
    void main() { getPi(); }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_006():
    source = """
    void main() {
        ; // Empty statement
        ;
    }
    """
    expected = "Error on line 3 col 8: ;"
    assert Parser(source).parse() == expected

def test_007():
    source = """
    struct Empty {}; 
    void main() {
        Empty e;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_008():
    source = """
    struct Data { int x; };
    Data globalVar;
    void main() {}
    """
    expected = "Error on line 3 col 18: ;"
    assert Parser(source).parse() == expected

def test_009():
    source = """
    void main() {
        string s = "String with escaped quote \" inside";
    }
    """
    expected = "Unclosed String: ;\n"
    assert Parser(source).parse() == expected

def test_010():
    source = """
    void main() {
        int x = -1;
        float y = -2.5;
    }
    """
    expected = "Error on line 4 col 20: .5"
    assert Parser(source).parse() == expected


# --- GROUP 2: VARIABLE DECLARATIONS (011-020) ---

def test_011():
    source = """
    void main() {
        int ;
        int b = 10;
    }
    """
    expected = "Error on line 3 col 12: ;"
    assert Parser(source).parse() == expected

def test_012():
    source = """
    void main() {
        float f;
        float g = 0.01;
        float h = .5;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_013():
    source = """
    void main() {
        string s;
        string name = "Katsushika Hokusai";
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_014():
    source = """
    void main() {
        auto i = 10;
        auto f = 20.5;
        auto s = "auto string";
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_015():
    source = """
    struct Point { int x; };
    void main() {
        Point p;
        auto p2 = p;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_016():
    source = """
    /*
    ░░░░░░░▄▄████▄▄▄░░░░░░▄▄██████▄▄
    ░░░░░██▓▓▓▓▓▓▒▓▓██░░▓█▓▓▓▓▒░▒▒▓▓██
    ░░░██▓▓▓▓▓▓▓▓▓▒░▓▓███▓▓▓▓▓▒▒▒░░▒▓▓█
    ░░██▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓█▓▓▓▓▓▓▓▓▓▓▒░░▓▓█
    ░▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓██▓▓▓▓▓▓▓▓▓▒░░▓▓█
    ░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▒▓█
    ░█▓▓▓▓▓▓▓▓▓▓▓▓████░████▓▓▓▓▓▓▓▓▓▒░░▓██
    █▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░██▓▓▓▓▓▓▓▓▓░░▓▓█
    █▓▓▓▓▓▓▓▓▓▓▓▓▓░░█░░░█░░▓▓▓▓▓▓▓▓▓▓▒░▓▓█▒
    █▓▓▓▓▓▓▓▓▓▓▓▓▓░█▒█░█▒█░▓▓▓▓▓▓▓▓▓▓▒▒▓▓█▒
    █▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒▓██▒
    █▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▒██░░░▓▓▓▓▓▓▓▓▓▓▓▒▓▓█▓▒
    ░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓█▓▒
    ░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒
    ░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒
    ░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓█▓▒
    ░░░█▓▓▓▓▓▓▓▓▓██▓▓▓▓█████▓▓▓▓▓▓▓▓▓▓█▓▒
    ░░░░█▓▓▓▓▓▓▓▓██████████▓▓▓▓▓▓▓▓▓▓██▓▒
    ░░░░▓█▓▓▓▓▓▓▓▓██▒▒▓▒▒█▓▓▓▓▓▓▓▓▓▓██▓▒
    ░░░░░░█▓▓▓▓▓▓▓▓██▒▒▒█▓▓▓▓▓▓▓▓▓▓██▓▒
    ░░░░░░░██▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓██▓▒
    ░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▒
    ░░░░░░░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒
    ░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓██▓▒
    ░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓█▓▒
    ░░░░░░░░░░░░░░░██▓▓▓▓▓██▓▒
    ░░░░░░░░░░░░░░░░░█▓▓██▓▒
    ░░░░░░░░░░░░░░░░░░░█▓▒
    */
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_017():
    source = """
    void main() {
        auto x; // Valid in grammar rules for auto without init?
        // Grammar: type_var ID (ASSIGN expression)?; 
        // type_var -> AUTO. So 'auto x;' is syntactically valid by this parser.
        x = 5;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_018():
    source = """
    void main() {
        float scientific = 1.2e10;
        float scientific2 = 1e-5;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_019():
    source = """
    void main() {
        int hex_looking_id = 0; 
        // Grammar only supports decimal INT_LIT
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_020():
    source = """
    struct Rect { int w; int h; };
    void main() {
        Rect r = {10, 20};
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected


# --- GROUP 3: EXPRESSIONS & OPERATORS (021-030) ---

def test_021():
    source = """
    void main() {
        int x = 1 + 2 * 3;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_022():
    source = """
    void main() {
        int x = (1 + 2) * 3;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_023():
    source = """
    void main() {
        bool b = true && false || !true; 
        // Note: 'true'/'false' are IDs in this grammar, not keywords, but syntactically ID is expression
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_024():
    source = """
    void main() {
        int a = 10;
        int b = 5;
        int c = a % b;
        int d = a / b;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_025():
    source = """
    void main() {
        int x = 0;
        x++;
        ++x;
        x--;
        --x;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_026():
    source = """
    void main() {
        int x = 5;
        int y = 10;
        auto z = x > y;
        z = x <= y;
        z = x == y;
        z = x != y;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_027():
    source = """
    void main() {
        int a; int b; int c;
        a = b  c = 10; // Chained assignment
    }
    """
    expected = "Error on line 4 col 15: c"
    assert Parser(source).parse() == expected

def test_028():
    source = """
    struct Vec { int x; };
    void main() {
        Vec v;
        v.x = 10;
        v.x++;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_029():
    source = """
    void main() {
        int x = - - 5; // Double negation/subtraction
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_030():
    source = """
    void main() {
        int val = func(1, 2+2, func2());
    }
    """
    expected = "Error on line 3 col 18: func"
    assert Parser(source).parse() == expected


# --- GROUP 4: IF / ELSE (031-040) ---

def test_031():
    source = """
    void main() {
        if (1) print(1);
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_032():
    source = """
    void main() {
        if (x > 0) {
            print(x);
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_033():
    source = """
    void main() {
        if (x) a = 1; else a = 2;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_034():
    source = """
    void main() {
        if (x) {
            a = 1
        } else {
            a = 2
        }
    }
    """
    expected = "Error on line 5 col 10: else"
    assert Parser(source).parse() == expected

def test_035():
    source = """
    void main() {
        if (a)
            if (b)
                c = 1;
            else
                c = 2;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_036():
    source = """
    void main() {
        if (a) {
            if (b) {
                // nested
            }
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_037():
    source = """
    void main() {
        if (a == 1) {} else if a == 2) {} else {}
    }
    """
    expected = "Error on line 3 col 31: a"
    assert Parser(source).parse() == expected

def test_038():
    source = """
    void main() {
        if (callFunc()) return;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_039():
    source = """
    void main() {
        if (a || b && c) {
            // Complex condition
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_040():
    source = """
    void main() {
        if (x = 5)) { 
            // Assignment in condition
        }
    }
    """
    expected = "Error on line 3 col 18: )"
    assert Parser(source).parse() == expected


# --- GROUP 5: LOOPS (041-050) ---

def test_041():
    source = """
    void main() {
        while (true) break;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_042():
    source = """
    void main() {
        while (x < 10) {
            x++;
            continue;
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_043():
    source = """
    void main() {
        for (int i=0; i<10; i++) {}
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_044():
    source = """
    void main() {
        for (i=0; i<10; ++i) print(i);
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_045():
    source = """
    void main() {
        for(;;) { break; } // Infinite loop
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_046():
    source = """
    void main() {
        for (auto x = 0; x < 5; x = x + 1) {
            // update with assignment
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_047():
    source = """
    void main() {
        while(1) {
            while(2) {
                break;
            }
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_048():
    source = """
    void main() {
        int i;
        for (i=0; i<n; i++) {
            if (i % 2 == 0) continue;
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_049():
    source = """
    void main() {
        // expression statement in for init
        for (initFunc(); check(); update()) {}
    }
    """
    expected = "Error on line 4 col 21: ("
    assert Parser(source).parse() == expected

def test_050():
    source = """
    void main() {
        for (int i=0; ; i++) break; // Empty condition
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected


# --- GROUP 6: SWITCH CASE (051-060) ---

def test_051():
    source = """
    void main() {
        switch(x) {
            case 1: break;
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_052():
    source = """
    void main() {
        switch(x) {
            case 1: break;
            default: break;
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_053():
    source = """
    void main() {
        switch(x) {
            case 1 
                x++;
                break;
            case 2:
                x--;
                break;
        }
    }
    """
    expected = "Error on line 5 col 16: x"
    assert Parser(source).parse() == expected

def test_054():
    source = """
    void main() {
        switch(x + y) {
            case 10: break;
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_055():
    source = """
    void main() {
        switch(c) {
            case "hello": break;
            case 1.5: break;
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_056():
    source = """
    void main() {
        switch(x) {
            // Empty cases
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_057():
    source = """
    void main() {
        switch(x) {
            case 1: case 2: case 3:
                doWork();
                break;
        }
    }
    """
    expected = "Error on line 4 col 20: case"
    assert Parser(source).parse() == expected

def test_058():
    source = """
    void main() {
        switch(x) {
            default:
                break;
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_059():
    source = """
    void main() {
        switch(x) {
            case 1: {
                int y = 2;
                break;
            }
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_060():
    source = """
    void main() {
        switch (flag) {
            case 1: return;
            default: return;
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected


# --- GROUP 7: STRUCTS (061-070) ---

def test_061():
    source = """
    struct A {
        int x;
    };
    void main() {}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_062():
    source = """
    struct Person {
        string name;
        int age;
        float height;
    };
    void main() {}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_063():
    source = """
    struct Node {
        int value;
        Node next; 
    };
    void main() {}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_064():
    source = """
    struct Point { int x; int y; };
    struct Rect { Point p1; Point p2; };
    void main() {}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_065():
    source = """
    struct Point { int x; int y; };
    void main() {
        Point p = {1, 2};
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_066():
    source = """
    struct Data { int id; };
    void main() {
        Data d;
        d.id = 5;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_067():
    source = """
    struct Outer { Inner in; };
    struct Inner { int val; };
    void main() {
        Outer o;
        o.in.val = 10;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_068():
    source = """
    struct A { int x; };
    A getA() { A temp; return temp; }
    void main() {
        int v = getA().x;
    }
    """
    expected = "Error on line 5 col 22: ."
    assert Parser(source).parse() == expected

def test_069():
    source = """
    struct A { int x; };
    void main() {
        A a1;
        A a2;
        a1 = a2;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_070():
    source = """
    struct Empty {};
    void main() {
        Empty e = {};
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected


# --- GROUP 8: FUNCTIONS (071-080) ---

def test_071():
    source = """
    void foo() {}
    void main() {}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_072():
    source = """
    int add(int a, int b) { return a+b; }
    void main() {}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_073():
    source = """
    void printInfo(string name, int age) {}
    void main() {}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_074():
    source = """
    float compute(float x) {
        if (x > 0) return x;
        return -x;
    }
    void main() {}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_075():
    source = """
    struct Box { int s; };
    Box createBox() {
        Box b;
        return b;
    }
    void main() {}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_076():
    source = """
    void recursive(int n) {
        if (n == 0) return;
        recursive(n - 1);
    }
    void main() {}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_077():
    source = """
    // Function with no return type specified (implicitly void? or error?)
    // Grammar: (type_explicit | VOID)? ID ...
    myFunc() {} 
    void main() {}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_078():
    source = """
    int calculate(int a, int b, int c) {
        return a * b + c;
    }
    void main() {}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_079():
    source = """
    void main() {
        // Function call as statement
        calculate(1, 2, 3);
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_080():
    source = """
    void main() {
        // Nested calls
        print(max(min(a, b), c));
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected


# --- GROUP 9: COMPLEX LOGIC & INTEGRATION (081-090) ---

def test_081():
    source = """
    int fib(int n) {
        if (n <= 1) return n;
        return fib(n-1) + fib(n-2);
    }
    void main() {
        fib(10);
    }
    """
    expected = "Error on line 4 col 20: -1"
    assert Parser(source).parse() == expected

def test_082():
    source = """
    int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    void main() {}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_083():
    source = """
    void main() {
        int sum = 0;
        for (int i = 0; i < 100; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                sum = sum + i;
            }
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_084():
    source = """
    struct Complex { float real; float imag; };
    Complex add(Complex a, Complex b) {
        Complex res;
        res.real = a.real + b.real;
        res.imag = a.imag + b.imag;
        return res;
    }
    void main() {}
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_085():
    source = """
    void main() {
        int day = 3;
        string name;
        switch(day) {
            case 1: name = "Mon"; break;
            case 2: name = "Tue"; break;
            default: name = "Unknown";
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_086():
    source = """
    void main() {
        // Testing operator precedence
        if (a + b * c > d && e || f) {
            return;
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_087():
    source = """
    void main() {
        // Brackets
        int x = (((1 + 2) * 3) / 4);
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_088():
    source = """
    void main() {
        // Empty blocks everywhere
        if(1){}else{}
        while() {}
        for(;;){}
        {}
    }
    """
    expected = "Error on line 5 col 14: )"
    assert Parser(source).parse() == expected

def test_089():
    source = """
    void main() {
        // Initializer expression
        int x = 1;
        int y = {1, 2, 3}; // Valid via expression11 -> LCB list_expression RCB
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_090():
    source = """
    struct S { int x; };
    void main() {
        S s;
        // Dot access deep
        s.x. = 10;
    }
    """
    expected = "Error on line 6 col 13: ="
    assert Parser(source).parse() == expected


# --- GROUP 10: EDGE CASES & FORMATTING (091-100) ---

def test_091():
    source = """
    void main() {
        int 
        x 
        = 
        5
        ;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_092():
    source = """
    void main() {int x=5 int y=6;if(x>y)return;}
    """
    expected = "Error on line 2 col 25: int"
    assert Parser(source).parse() == expected

def test_093():
    source = """
    void main() {
        string s = "";
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_094():
    source = """
    void main() {
        float f = 1.; // Dot at end
        float g = .1; // Dot at start
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_095():
    source = """
    void main() {
        // String with escape chars
        string s = "\\n \\t \\\\ \\\"";
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_096():
    source = """
    void main() {
        int _validIdentifier_123 = 1;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_097():
    source = """
    void main() {
        // Just return
        return;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_098():
    source = """
    void main() {
        // Return with expression
        return 1 + 2;
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected

def test_099():
    source = """
    void main() {
        // Dangling operations
        i++;
        call();
        a = b;
    }
    """
    expected = "Error on line 5 col 8: call"
    assert Parser(source).parse() == expected

def test_100():
    source = """
    // The Mega Test
    struct Point { float x; float y; };
    
    Point move(Point p, float dx, float dy) {
        p.x = p.x + dx;
        p.y = p.y + dy;
        return p;
    }

    void main() {
        auto p = {0.0, 0.0};
        int i = 0;
        
        while (i < 10) {
            switch(i % 2) {
                case 0: p = move(p, 1.0, 1.0); break;
                default: p = move(p, -0.5, -0.5); break;
            }
            i++;
        }
        
        if (p.x > 5.0) {
            print("Far");
        } else {
            print("Near");
        }
    }
    """
    expected = "Error on line 18 col 39: .5"
    assert Parser(source).parse() == expected