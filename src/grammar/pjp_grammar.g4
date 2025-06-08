grammar pjp_grammar;
program: (statement)+;

statement                                                                               
    : ';'                                                             # EmptyStmt  
    | TYPE VAR (',' VAR)* ';'                                         # VarDecl
    | expression ';'                                                  # ExprStmt   
    | 'read' VAR (',' VAR)* ';'                                       # ReadStmt   
    | 'write' expression (',' expression)* ';'                        # WriteStmt  
    | '{' statement* '}'                                              # BlockStmt  
    | 'if' '(' condition ')' statement ('else' statement)?            # IfStmt     
    | 'while' '(' condition ')' statement                             # WhileStmt  
    | 'do' statement 'while' '(' condition ')' ';'                    # DoWhileStmt
    | 'for' '(' expression ';' condition ';' expression ')' statement # ForStmt    
    ;

condition                       
	: expression # BoolCondition
	;

expression                                                                      
    : '(' expression ')'                                  # ParensExpr     
    | op='-' expression                                   # NegExpr       
    | op='!' expression                                   # NotExpr       
    | expression op=('*' | '/') expression                # MulExpr     
    | expression op='%' expression                        # MuduloExpr    
    | expression op=('+' | '-') expression                # AddExpr     
    | expression op='.' expression                        # ConcatExpr    
    | expression op=('<' | '>') expression                # RelExpr  
    | expression op=('==' | '!=') expression              # EqExpr
    | expression op='&&' expression                       # AndExpr     
    | expression op='||' expression                       # OrExpr     
    | VAR                                                 # VarExpr       
    | literal                                             # LiteralExpr   
    | expression '?' expression split=':' expression      # TernaryExpr   
    | VAR '=' expression                                  # AssignExpr    
    ;

literal
    : INT
    | FLOAT
    | BOOL
    | STRING
    ;

INT: DIGIT+;
FLOAT: DIGIT+ '.' DIGIT*;
BOOL: 'true' | 'false';
STRING: '"' (ESC | ~["\\])* '"';

TYPE: 'int' | 'float' | 'bool' | 'string';
VAR: LETTER (LETTER | DIGIT)*;

COMMENT: '//' ~[\r\n]* -> skip;
SPACE: [ \t\r\n]+ -> skip;

fragment ESC: '\\' (["\\/bfnrt] | UNICODE_ESC);
fragment UNICODE_ESC: 'u' HEX HEX HEX HEX;
fragment HEX: [0-9a-fA-F];

fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
