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
program: EOF;

// *** LEXER ***

// White spaces and comments
WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs
BLOCK_CMT: '/*' .*? '*/' -> skip;  // skip block comments
LINE_CMT: '//' .*? '\n' -> skip;  // skip line comments

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

// Literals
INT_LIT: '-'? [0-9]+;
// FLOAT_LIT: '-'? (
//       [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)?  // 1.2, 123.123, 0.12e-421
//       | '.' [0-9]+ ([eE] [+-]? [0-9]+)?       // .2, .2332, .12E-333
//       | [0-9]* [eE]? [0-9]+                   // 2e-1, 2E+123, e-123  *** ATTENTION!!! ***
// );

FLOAT_LIT: INTEGER '.' (FRAC | EXP)?;
fragment INTEGER: [0-9]*;
fragment FRAC: [0-9]* [1-9];
fragment EXP: [0-9]* [eE] [-]? [1-9]+ [0-9] [1-9];

STRING_LIT: '"' (~["\\\r\n] | ESC_SEQ)* '"';

fragment ESC_SEQ: '\\' ["\\bfrnt];  // means: \" \\ \b \f \r \n \t 

BACKSPC: '\b';
FORMFEED: '\f';
CARRIAGE: '\r';
NEWLN: '\n';
TAB: '\t';
DOUBLE_QUOTE: '\\"';
BACKSLASH: '\\';

// Identifiers
ID: [a-zA-Z_] [0-9a-zA-Z_]*;



ILLEGAL_ESCAPE: '"' (~["\\\r\n] | ESC_SEQ)* '\\' ~["\\bfrnt] '"';  // a backslash followed by an undefined character
UNCLOSE_STRING: '"' (~["\\\r\n] | ESC_SEQ)* '\\'?;

ERROR_CHAR: .;  // at the end to catch all the undefined characters

// *** LEXER ***