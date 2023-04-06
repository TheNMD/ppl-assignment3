grammar MT22;

@lexer::header {
from lexererr import *;
studentID = "2052932";
studentName = "Nguyen Manh Dan";
}

options{
	language=Python3;
}

//==========================================================
// Lexer Rules
//==========================================================

// Whitespace
WS : [ \t\n\r\f\b]+ -> skip ;

// COMMENT
CCOMMENT :  '/*' .*? '*/' -> skip;

CPPCOMMENT : '//' ~ [\r\n]* -> skip;

// KEYWORD
KWVOID : 'void' ;

KWAUTO : 'auto' ;

KWINT :  'integer' ;

KWFLOAT : 'float' ;

KWBOO : 'boolean' ;

KWSTR : 'string' ;

KWARR : 'array' ;

KWINHERIT : 'inherit' ;

KWFUNC : 'function' ;

KWTRUE : 'true' ;

KWFALSE : 'false' ;

KWFOR : 'for' ;

KWWHILE : 'while' ;

KWDO : 'do' ;

KWBRK : 'break' ;

KWCONT : 'continue' ;

KWRTN : 'return' ;

KWIF : 'if' ;

KWELSE : 'else' ;

KWOF : 'of' ;

KWOUT : 'out' ;

// Identifiers
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

// Operators
ADDOP : '+' ;

SUBOP : '-' ;

MULOP : '*' ;

DIVOP : '/' ;

MODOP : '%' ;

EXCOP : '!' ;

ANDOP : '&&' ;

OROP : '||' ;

EQLOP : '==' ;

DIFOP : '!=' ;

LARGEOP : '>' ;

LEQLOP : '>=' ;

SMALLOP : '<' ;

SEQLOP : '<=' ;

CONCATOP : '::' ;

// Separators
DOT : '.' ;

CM : ',' ;

SM : ';' ;

CL : ':' ;

LB : '(' ;

RB : ')' ;

LSB : '[' ;

RSB : ']' ;

LCB : '{' ;

RCB : '}' ;

EQL : '=' ;

// Literals
LITINT : [0-9] | [1-9][0-9_]*[0-9] {self.text = self.text.replace('_','')} ;

LITFLOAT : LITINT {self.text = self.text.replace('_','')} 
		 | LITINT Decimal {self.text = self.text.replace('_','')}
		 | LITINT Exponent {self.text = self.text.replace('_','')} 
		 | LITINT Decimal Exponent {self.text = self.text.replace('_','')}
		 | Decimal {self.text = self.text.replace('_','')}
		 | Decimal Exponent {self.text = self.text.replace('_','')} ;

fragment Decimal : DOT [0-9]* ;

fragment Exponent : [eE] [+-]? [0-9]+ ;

litboo : KWTRUE | KWFALSE ;

LITSTR : '"' Char* '"' {self.text = self.text[1:-1]}  ;

fragment Char : ('\\' [bfrnt'\\"] | ~[\n'\\"]) ; 

//==========================================================
// Parser Rules
//==========================================================

program : declist EOF ;

declist : decl declist | decl ;

decl : vardecl | funcdecl ;

vardecl : idlist CL (KWARR LSB dimenlist RSB KWOF)? vartyp SM
		| ID middle expr SM ;

idlist : ID ids | ID ;

ids : CM ID ids | ;

vartyp : KWINT | KWFLOAT | KWBOO | KWSTR | KWAUTO ;

dimenlist : LITINT dimens | LITINT ;

dimens : CM LITINT dimens | ;

middle : CM ID middle expr CM | CL (KWARR LSB dimenlist RSB KWOF)? vartyp EQL ;

funcdecl : funcproto funcbody ;

funcproto : ID CL KWFUNC (KWARR LSB dimenlist RSB KWOF)? functyp paradecl (KWINHERIT ID)? ;

functyp :  KWINT | KWFLOAT | KWBOO | KWSTR | KWAUTO | KWVOID ;

paradecl : LB paralist RB ;

paralist : para paras | ;

paras : CM para paras | ;

para :  KWINHERIT? KWOUT? ID CL (KWARR LSB dimenlist RSB KWOF)? vartyp ;

funcbody : blockstmt ;

blockstmt : LCB bodylist RCB ;

bodylist : body bodylist | ;

body : vardecl | stmt | ifstmt | forstmt | whilestmt | blockstmt ;

stmt : (assignstmt | dowhilestmt | breakstmt | continuestmt | rtnstmt | callstmt) SM ;

ifstmt : matchstmt | unmatchstmt ;

matchstmt : KWIF LB expr RB matchstmt KWELSE matchstmt | (stmt | forstmt | whilestmt | blockstmt) ;

unmatchstmt : KWIF LB expr RB ifstmt | KWIF LB expr RB matchstmt KWELSE unmatchstmt ;

forstmt : KWFOR LB assignstmt CM expr CM expr RB (stmt | ifstmt | forstmt | whilestmt | blockstmt) ;

whilestmt : KWWHILE LB expr RB (stmt | ifstmt | forstmt | whilestmt | blockstmt) ;

assignstmt : ID idxop? EQL expr ;

dowhilestmt : KWDO blockstmt KWWHILE LB expr RB ;

breakstmt : KWBRK ;

continuestmt : KWCONT ;

rtnstmt : KWRTN (expr)? ;

callstmt : (ID LB RB | ID LB exprlist RB | specialfunc) ;

exprlist : expr exprs | expr ;

exprs : CM expr exprs | ;

expr : expr1 CONCATOP expr1 | expr1 ;

expr1 : expr2 (EQLOP | DIFOP | LARGEOP | LEQLOP | SMALLOP | SEQLOP)  expr2 | expr2 ;

expr2 : expr2 (ANDOP | OROP) expr3 | expr3 ;

expr3 : expr3 (ADDOP | SUBOP) expr4 | expr4 ;

expr4 : expr4 (MULOP | DIVOP | MODOP) expr5 | expr5 ;

expr5 :  EXCOP expr5 | expr6 ;

expr6 : SUBOP expr6 | operand ;

//expr7 : expr7 idxop | operand ;

operand: LITINT | LITFLOAT | litboo | LITSTR | ID idxop? | funccall | subexpr | litarr | specialfunc ;

idxop : LSB celllist RSB ;

celllist : expr cells | expr ;

cells : CM expr cells | ;

funccall : ID LB exprlist? RB ;

subexpr : LB expr RB ;

litarr : LCB exprlist? RCB ;

specialfunc : ('readInteger' | 'readFloat' | 'readBoolean' | 'readString' | 'preventDefault') LB RB 
			| ('printInteger' | 'writeFloat' | 'printBoolean' | 'printString' | 'super') LB exprlist RB ;

// ERROR TOKENS
ILLEGAL_ESCAPE: '"' Char* ('\\' ~[bfrnt'\\"]) {self.text = self.text[1:]; raise IllegalEscape(self.text)};

UNCLOSED_STRING:  '"' Char* (EOF)? {self.text = self.text[1:]; raise UncloseString(self.text)};

ERROR_CHAR: . {raise ErrorToken(self.text)};
