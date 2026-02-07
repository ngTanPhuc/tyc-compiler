grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// TODO: Define grammar rules here
// *** PARSER ***

program: decl_list EOF;

decl_list: decl decl_list | ;
decl: struct_decl | func_decl;

// struct
struct_decl: STRUCT ID LCURL_BR member_list RCURL_BR SEMI_COLON;

member_list: member member_list | ;
member: typ ID SEMI_COLON;

// function
func_decl: (typ | VOID | ) ID param_decl body;

param_decl: LPAREN param_list RPAREN;
param_list: param_prime | ;
param_prime: param COMMA param_prime | param;
param: typ ID;

body: LCURL_BR stmt_list RCURL_BR;  // !NOTE: function body is a block statement, can a block statement be empty? Answer: yes, it can be empty!
stmt_list: stmt_prime | ;
stmt_prime: stmt stmt_prime | stmt;
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

var_decl: (typ | AUTO) ID (ASSIGN expr | ) SEMI_COLON;

block_stmt: LCURL_BR stmt_list RCURL_BR;

if_stmt: IF LPAREN expr RPAREN stmt (ELSE stmt | );

whl_stmt: WHILE LPAREN expr RPAREN stmt;

// !NOTE: <update> should check for assign, increment, decrement in parser or should it be in the AST generation step? Answer: in parser just for sure (it can be in the AST gen step too)
for_stmt: FOR LPAREN for_init (expr | ) SEMI_COLON (for_update | ) RPAREN stmt;
for_init: var_decl | expr_stmt | SEMI_COLON;  // !NOTE: <init> var_decl should check for declare and assign at the same time
for_update: for_lhs ASSIGN expr
		| for_lhs (INCREMENT | DECREMENT)
		| (INCREMENT | DECREMENT) for_lhs
		;
for_lhs: ID | expr MEMBER_ACCESS ID;

switch_stmt: SWITCH LPAREN expr RPAREN LCURL_BR switch_body RCURL_BR;
switch_body: switch_case_list (switch_default switch_case_list | );
switch_case_list: switch_case switch_case_list | ;
switch_case: CASE case_expression COLON (stmt_list | );
case_expression: (INT_LIT | (ADD | SUB) INT_LIT | LPAREN expr RPAREN | expr);
switch_default: DEFAULT COLON (stmt_list | );

break_stmt: BREAK SEMI_COLON;

cont_stmt: CONTINUE SEMI_COLON;

return_stmt: RETURN (expr | ) SEMI_COLON;

expr_stmt: expr SEMI_COLON;

// expression
expr: expr1 ASSIGN expr | expr1;
expr1: expr1 OR expr2 | expr2;
expr2: expr2 AND expr3 | expr3;
expr3: expr3 (EQUAL | NOT_EQUAL) expr4 | expr4;
expr4: expr4 (LESS | LESS_EQUAL | GREATER | GREATER_EQUAL) expr5 | expr5;
expr5: expr5 (ADD | SUB) expr6 | expr6;
expr6: expr6 (MUL | DIV | MOD) expr7 | expr7;
expr7: (NOT | ADD | SUB) expr7 | expr8;
expr8: (INCREMENT | DECREMENT) expr8 | expr9;
expr9: expr9 (INCREMENT | DECREMENT) | expr10;
expr10: expr10 MEMBER_ACCESS ID | expr_primary;
expr_primary: INT_LIT 
            | FLOAT_LIT 
            | STRING_LIT 
            | ID 
            | LPAREN expr RPAREN 
            | func_call 
            | struct_lit
            ;

// others
typ: INT | FLOAT | STRING | ID;  // no auto keyword
func_call: ID LPAREN arg_list RPAREN;
arg_list: args | ;
args: expr COMMA args | expr;
struct_lit: LCURL_BR (structmem_list | ) RCURL_BR;
structmem_list: expr COMMA structmem_list | expr;

// *** PARSER ***

// *** LEXER ***
// Errors
ILLEGAL_ESCAPE: '"' (~["\\\r\n] | ESC_SEQ)* '\\' ~["\\bfrnt] '"' {self.text = self.text[1:]};  // a backslash followed by an undefined character

// White spaces and comments
WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs
BLOCK_CMT: '/*' .*? '*/' -> skip;  // skip block comments
LINE_CMT: '//' ~[\n]* -> skip;  // skip line comments. Means skip everything until \n

// Keywords
AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
RETURN: 'return';
STRING: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

// Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
GREATER: '>';
LESS_EQUAL: '<=';
GREATER_EQUAL: '>=';
OR: '||';
AND: '&&';
NOT: '!';
INCREMENT: '++';
DECREMENT: '--';
ASSIGN: '=';
MEMBER_ACCESS: '.';

// Separators
LSQUARE_BR: '[';
RSQUARE_BR: ']';
LCURL_BR: '{';
RCURL_BR: '}';
LPAREN: '(';
RPAREN: ')';
SEMI_COLON: ';';
COMMA: ',';
COLON: ':';

// Literals
// !!! NOTE !!!
// for now, INT_LIT will only be positive value, negative value -1 will be handled by the parser.
// So, 1-2 is 3 tokens.
INT_LIT: [0-9]+;
// FLOAT_LIT: '-'? (
//       [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)?  // 1.2, 123.123, 0.12e-421
//       | '.' [0-9]+ ([eE] [+-]? [0-9]+)?       // .2, .2332, .12E-333
//       | [0-9]* [eE]? [0-9]+                   // 2e-1, 2E+123, e-123  *** ATTENTION!!! ***
// );

FLOAT_LIT: INTEGER FRAC | INTEGER EXP | INTEGER FRAC EXP | FRAC;
fragment INTEGER: [0-9]*;
fragment FRAC: '.' [0-9]*;
fragment EXP: [eE] [+-]? [1-9] [0-9]*;

// !!! NOTE !!!
// There's a difference between a newline character (\n) and a literal newline (Enter)
// "Hello from\nThe other side" -- allowed
// "Hello from
// The other side" -- not allowed
// The lexer sees the "\" and look for the next allowed escape sequence [bfrnt["][\]]. So if you write \b, \n, \t 
// The lexer will take this as literal
STRING_LIT: '"' (~["\\\r\n] | ESC_SEQ)* '"' {self.text = self.text[1:-1]};
fragment ESC_SEQ: '\\' [bfrnt"\\];

// Identifiers
ID: [a-zA-Z_] [0-9a-zA-Z_]*;

UNCLOSE_STRING: '"' (~["\\\r\n] | ESC_SEQ)* '\\'? {self.text = self.text[1:]};
ERROR_CHAR: .;  // at the end to catch all the undefined characters

// *** LEXER ***