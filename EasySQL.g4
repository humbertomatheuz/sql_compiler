grammar EasySQL;

prog: query EOF ;

query
    : 'MOSTRAR' DISTINTO? campos 'DE' IDENTIFICADOR ('POR' grupos)? ('ONDE' condicoes)? SEMICOLON
    | 'INSERIR EM' IDENTIFICADOR ('(' colunas ')')? 'VALORES' tuplas SEMICOLON 
    | 'REMOVER DE' IDENTIFICADOR ('ONDE' condicoes)? SEMICOLON            
    | 'DELETAR TABELA' IDENTIFICADOR SEMICOLON         
    | 'CRIAR TABELA' IDENTIFICADOR '(' definicoes ')' SEMICOLON 
    | 'ATUALIZAR' IDENTIFICADOR 'DEFINIR' atualizacoes ('ONDE' condicoes)? SEMICOLON                       
    ;

campos: campo (',' campo)* ;

campo: AGREGADOR '(' (DISTINTO IDENTIFICADOR | IDENTIFICADOR) ')'    
     | DISTINTO IDENTIFICADOR 
     | IDENTIFICADOR ;

DISTINTO: 'DIFERENTES' | 'DISTINCT';

tuplas: '(' valores ')' (',' '(' valores ')')* ;

definicoes: definicao (',' definicao)* ;

atualizacoes: IDENTIFICADOR '=' valor ( ',' IDENTIFICADOR '=' valor)* ;

definicao: IDENTIFICADOR tipo_dado ;

grupos: IDENTIFICADOR (',' IDENTIFICADOR)*;

condicoes: condicao ('E' condicao)* ;

condicao: IDENTIFICADOR operador valor  
        | AGREGADOR '(' IDENTIFICADOR ')' operador valor ; 

colunas: IDENTIFICADOR (',' IDENTIFICADOR)* ;

valores: valor (',' valor)* ;

operador: '=' | '<' | '>' | '<=' | '>=' | '!=' ;

valor: STRING 
     | NUMERO 
     | BOOLEANO 
     | 'NULL' ;

STRING: '\'' (~['\r\n])* '\'' ;
NUMERO: '-'? [0-9]+ ('.' [0-9]+)? ;
BOOLEANO: 'True' | 'False' ;

tipo_dado: 'INT' 
  | 'SMALLINT' 
  | 'BIGINT' 
  | 'FLOAT' 
  | 'REAL' 
  | 'DOUBLE' 
  | 'DECIMAL' '(' NUMERO ',' NUMERO ')' 
  | 'NUMERIC' '(' NUMERO ',' NUMERO ')' 
  | 'CHAR' '(' NUMERO ')' 
  | 'VARCHAR' '(' NUMERO ')' 
  | 'TEXT' 
  | 'NCHAR' '(' NUMERO ')' 
  | 'NVARCHAR' '(' NUMERO ')' 
  | 'BOOLEAN' 
  | 'DATE' 
  | 'TIME' 
  | 'DATETIME' 
  | 'TIMESTAMP' 
  | 'YEAR' 
  | 'BLOB' 
  | 'VARBINARY' '(' NUMERO ')' 
  | 'JSON' 
  | 'XML' 
  | 'GEOMETRY' ;

AGREGADOR: 'SOMA' | 'CONTAGEM' | 'MEDIA' | 'MAX' | 'MIN' | 'AVG' | 'SUM' | 'COUNT' ;

IDENTIFICADOR: [a-zA-Z_][a-zA-Z_0-9]* ;

SEMICOLON: ';' ;

WS: [ \t\r\n]+ -> skip ;
