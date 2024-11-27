grammar EasySQL;

prog: query EOF ;

query
    : 'MOSTRAR' campos 'DE' IDENTIFICADOR ('POR' grupos)? ('ONDE' condicoes)? SEMICOLON
    | 'INSERIR EM' IDENTIFICADOR ('(' colunas ')')? 'VALORES' '(' valores ')' SEMICOLON 
    | 'REMOVER DE' IDENTIFICADOR ('ONDE' condicoes)? SEMICOLON            
    | 'DELETAR TABELA' IDENTIFICADOR SEMICOLON         
    | 'CRIAR TABELA' IDENTIFICADOR '(' definicoes ')' SEMICOLON 
    | 'ATUALIZAR' IDENTIFICADOR 'DEFINIR' atualizacoes ('ONDE' condicoes)? SEMICOLON                       
    ;

campos: campo (',' campo)* ;

campo: AGREGADOR '(' IDENTIFICADOR ')'    
    | IDENTIFICADOR 
    ;

definicoes: definicao (',' definicao)* ;

atualizacoes: IDENTIFICADOR '=' valor ( ',' IDENTIFICADOR '=' valor)* ;

definicao: IDENTIFICADOR tipo_dado ;

grupos: IDENTIFICADOR (',' IDENTIFICADOR)*;

condicoes: condicao ('E' condicao)* ;

condicao: IDENTIFICADOR operador valor  // Condições básicas
        | AGREGADOR '(' IDENTIFICADOR ')' operador valor ; // Condições com agregações

colunas: IDENTIFICADOR (',' IDENTIFICADOR)* ;

valores: valor (',' valor)* ;

operador: '=' | '<' | '>' | '<=' | '>=' | '!=' ;

valor: STRING 
     | NUMERO 
     | AGREGADOR '(' IDENTIFICADOR ')' ;  // Suporte a funções agregadas

tipo_dado: 'INT' | 'FLOAT' | 'CHAR' | 'VARCHAR' '(' NUMERO ')' | 'TEXT' ;

AGREGADOR: 'SOMA' | 'CONTAR' | 'MEDIA' | 'MAX' | 'MIN' | 'AVG' | 'SUM' | 'COUNT' ;

IDENTIFICADOR: [a-zA-Z_][a-zA-Z_0-9]* ;

NUMERO: [0-9]+ ('.' [0-9]+)? ;

STRING: '\'' .*? '\'' ;

SEMICOLON: ';' ;

WS: [ \t\r\n]+ -> skip ;
