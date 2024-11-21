import sys
from antlr4 import *
from EasySQLLexer import EasySQLLexer
from EasySQLParser import EasySQLParser
from EasySQLListener import EasySQLListener

def analize_campos(campos):
    campos_text = ""
    numero_campos = 0
    for campo in campos.campo():
        if numero_campos > 0: campos_text += ', '
        campos_text += f'{campo.getText()}'
        numero_campos += 1

    return campos_text

def analize_grupos(grupos):
    grupos_text = ""
    numero_grupos = 0
    for grupo in grupos.IDENTIFICADOR():
        if numero_grupos > 0: grupos_text += ', '
        grupos_text += grupo.getText()
        numero_grupos += 1
    
    return grupos_text

def analize_condicoes(condicoes):
    condicoes_text = ""
    numero_condicoes = 0
    for condicao in condicoes.condicao():
        if numero_condicoes > 0: condicoes_text += ' E '
        numero_condicoes += 1

        if condicao.valor().STRING(): valor = condicao.valor().STRING().getText()
        else: valor = condicao.valor().NUMERO().getText()
        
        condicoes_text += f'{condicao.IDENTIFICADOR().getText()} {condicao.operador().getText()} {valor}'
    
    return condicoes_text

def analize_colunas(colunas):
    colunas_text = ""
    numero_colunas = 0
    for coluna in colunas.IDENTIFICADOR():
        if numero_colunas > 0: colunas_text += ', '
        colunas_text += coluna.getText()
        numero_colunas += 1
    
    return colunas_text

def analize_valores(valores):
    valores_text = ""
    numero_valores = 0
    for valor in valores.valor():
        if numero_valores > 0: valores_text += ', '
        valores_text += valor.getText()
        numero_valores += 1
    
    return valores_text

input_text = input("Digite a consulta: ")

input_stream = InputStream(input_text)
lexer = EasySQLLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = EasySQLParser(stream)
query = parser.prog().query()
sql_command = ""

if "MOSTRAR" in query.getText():
    campos_text = analize_campos(query.campos())
    grupos_text = analize_grupos(query.grupos())
    condicoes_text = analize_condicoes(query.condicoes())

    sql_command += f'SELECT {campos_text} GROUP BY {grupos_text}'
    if condicoes_text != "":
        sql_command += f' WHERE {condicoes_text};'
elif "INSERIR" in query.getText():
    identificador_text = query.IDENTIFICADOR().getText()
    sql_command += f'INSERT INTO {identificador_text} '

    if query.colunas():
        colunas_text = analize_colunas(query.colunas())
        sql_command += f' ({colunas_text}) '

    valores_text = analize_valores(query.valores())
    sql_command += f'VALUES ({valores_text});'
elif "REMOVER" in query.getText():
    sql_command = f'DELETE FROM {query.IDENTIFICADOR().getText()}'

    if query.condicoes():
        condicoes_text = analize_condicoes(query.condicoes())
        sql_command += f' WHERE {condicoes_text}'

    sql_command += ';'
elif "DELETAR" in query.getText(): sql_command = f'DROP TABLE {query.IDENTIFICADOR().getText()};'
else:
    raise ValueError("Comando Inválido")

print(sql_command)

'''
Exemplos de Comandos:

MOSTRAR SUM(vendas), categoria POR categoria ONDE ano >= 2020;

INSERIR EM produtos VALORES ('Notebook', 3500.00, 'Eletrônicos');

REMOVER DE vendas ONDE categoria = 'Tecnologia' E ano < 2020;

DELETAR TABELA clientes;

'''