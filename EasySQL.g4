grammar EasySQL;

prog: query EOF ;

query
    : 'MOSTRAR' campos ('POR' grupos)? ('ONDE' condicoes)? SEMICOLON        # QuerySelect
    | 'INSERIR EM' IDENTIFICADOR ('(' colunas ')')? 'VALORES' '(' valores ')' SEMICOLON  # QueryInsert
    | 'REMOVER DE' IDENTIFICADOR ('ONDE' condicoes)? SEMICOLON            # QueryDelete
    | 'DELETAR TABELA' IDENTIFICADOR SEMICOLON                             # QueryDeleteTable
    ;

campos: campo (',' campo)* ;

campo: AGREGADOR '(' IDENTIFICADOR ')'    # CampoComAgregador
    | IDENTIFICADOR                     # CampoSimples
    ;

grupos: IDENTIFICADOR (',' IDENTIFICADOR)*;

condicoes: condicao ('E' condicao)* ;

condicao: IDENTIFICADOR operador valor;

colunas: IDENTIFICADOR (',' IDENTIFICADOR)* ;

valores: valor (',' valor)* ;

operador: '=' | '<' | '>' | '<=' | '>=' | '!=' ;

valor: STRING | NUMERO;

AGREGADOR: 'SUM' | 'COUNT' | 'AVG' | 'MAX' | 'MIN' ;

IDENTIFICADOR: [a-zA-Z_][a-zA-Z_0-9]* ;

NUMERO: [0-9]+ ('.' [0-9]+)? ;

STRING: '\'' .*? '\'' ;

SEMICOLON: ';' ;

WS: [ \t\r\n]+ -> skip ;
