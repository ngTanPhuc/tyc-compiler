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
BLOCK_CMT: '/*' .* '*/' -> skip;  // skip block comments
LINE_CMT: '//' .* '\n' -> skip;  // skip line comments

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


// *** LEXER ***

ERROR_CHAR: .;
ILLEGAL_ESCAPE:.;
UNCLOSE_STRING:.;
