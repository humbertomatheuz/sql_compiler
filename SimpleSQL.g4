grammar SimpleSQL;

query       : SELECT columns FROM tableName (WHERE condition)? ;

columns     : '*' | column (',' column)* ;
column      : ID ;

tableName   : ID ;

condition   : column op value ;
op          : '=' | '<' | '>' ;
value       : STRING | NUMBER ;

SELECT      : 'SELECT' ;
FROM        : 'FROM' ;
WHERE       : 'WHERE' ;

ID          : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER      : [0-9]+ ;
STRING      : '\'' [a-zA-Z0-9_ ]+ '\'' ;

WS          : [ \t\r\n]+ -> skip ;