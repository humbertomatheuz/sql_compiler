grammar EasySQL;

prog: query EOF ;

query
    : 'MOSTRAR' campos ('POR' grupos)? 'DE' IDENTIFICADOR ('ONDE' condicoes)? SEMICOLON
    | 'INSERIR EM' IDENTIFICADOR ('(' colunas ')')? 'VALORES' '(' valores ')' SEMICOLON 
    | 'REMOVER DE' IDENTIFICADOR ('ONDE' condicoes)? SEMICOLON            
    | 'DELETAR TABELA' IDENTIFICADOR SEMICOLON         
    | 'CRIAR TABELA' IDENTIFICADOR '(' definicoes ')' SEMICOLON                        
    ;

campos: campo (',' campo)* ;

campo: AGREGADOR '(' IDENTIFICADOR ')'    
    | IDENTIFICADOR 
    ;

definicoes: definicao (',' definicao)* ;

definicao: IDENTIFICADOR tipo_dado ;

grupos: IDENTIFICADOR (',' IDENTIFICADOR)*;

condicoes: condicao ('E' condicao)* ;

condicao: IDENTIFICADOR operador valor;

colunas: IDENTIFICADOR (',' IDENTIFICADOR)* ;

valores: valor (',' valor)* ;

operador: '=' | '<' | '>' | '<=' | '>=' | '!=' ;

valor: STRING | NUMERO;

tipo_dado: 'INT' | 'FLOAT' | 'CHAR' | 'VARCHAR(50)' | 'TEXT' ;

AGREGADOR: 'SOMA' | 'CONTAR' | 'MEDIA' | 'MAX' | 'MIN' ;

IDENTIFICADOR: [a-zA-Z_][a-zA-Z_0-9]* ;

NUMERO: [0-9]+ ('.' [0-9]+)? ;

STRING: '\'' .*? '\'' ;

SEMICOLON: ';' ;

WS: [ \t\r\n]+ -> skip ;
