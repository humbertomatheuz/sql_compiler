import sqlite3
import sys
import os
from antlr4 import *
from EasySQLLexer import EasySQLLexer
from EasySQLParser import EasySQLParser
from EasySQLListener import EasySQLListener

DB_FILE = "database.db"

def executar_sql(comando_sql):
    if not os.path.exists(DB_FILE):
        with sqlite3.connect(DB_FILE) as conn:
            print(f"Banco de dados '{DB_FILE}' criado com sucesso.")
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute(comando_sql)
            if comando_sql.strip().upper().startswith("SELECT"):
                return cursor.fetchall()
            else:
                conn.commit()
                return "Comando executado com sucesso."
    except sqlite3.Error as e:
        return f"Erro ao executar SQL: {e}"

def analize_campos(campos):
    campos_text = ""
    numero_campos = 0
    for campo in campos.campo():
        if numero_campos > 0: campos_text += ', '
        if campo.AGREGADOR():
            agregador = campo.AGREGADOR().getText().strip()
            if agregador == 'SOMA' or agregador == 'SUM': 
                campos_text += f'SUM({campo.IDENTIFICADOR().getText()})'
            elif agregador == 'CONTAR' or agregador == 'COUNT': 
                campos_text += f'COUNT({campo.IDENTIFICADOR().getText()})'
            elif agregador == 'MEDIA' or agregador == 'AVG': 
                campos_text += f'AVG({campo.IDENTIFICADOR().getText()})'
            elif agregador == 'MAX': 
                campos_text += f'MAX({campo.IDENTIFICADOR().getText()})'
            elif agregador == 'MIN': 
                campos_text += f'MIN({campo.IDENTIFICADOR().getText()})'
        else:
            if campo.getText() == 'TUDO':
                campos_text += '*'
            else : 
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
    if not condicoes:
        return ""

    condicoes_text = []
    for condicao in condicoes.condicao():
        if condicao.valor().STRING():
            valor = condicao.valor().STRING().getText()
        elif condicao.valor().NUMERO():
            valor = condicao.valor().NUMERO().getText()
        else:
            raise ValueError("Valor inválido na condição.") 

        if condicao.AGREGADOR():
            agregador = condicao.AGREGADOR().getText()
            if agregador == 'SOMA' or agregador == 'SUM': 
                agregador = f'SUM'
            elif agregador == 'CONTAR' or agregador == 'COUNT': 
                agregador = f'COUNT'
            elif agregador == 'MEDIA' or agregador == 'AVG': 
                agregador = f'AVG'
            elif agregador == 'MAX': 
                agregador = f'MAX'
            elif agregador == 'MIN': 
                agregador = f'MIN'
            coluna = condicao.IDENTIFICADOR().getText()
            operador = condicao.operador().getText()
            condicoes_text.append(f"{agregador}({coluna}) {operador} {valor}")
        else:
            coluna = condicao.IDENTIFICADOR().getText()
            operador = condicao.operador().getText()
            condicoes_text.append(f"{coluna} {operador} {valor}")

    return " AND ".join(condicoes_text)


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

def analize_definicoes(definicoes):
    definicoes_text = ""
    numero_definicoes = 0
    for definicao in definicoes.definicao():
        if numero_definicoes > 0: definicoes_text += ', '
        definicoes_text += f'{definicao.IDENTIFICADOR().getText()} {definicao.tipo_dado().getText()}'
        numero_definicoes += 1
    
    return definicoes_text

def analize_atualizacoes(atualizacoes):
    atualizacoes_text = ""
    numero_atualizacoes = 0
     
    for atualizacao in atualizacoes.IDENTIFICADOR():
       
        valor = atualizacoes.valor()[numero_atualizacoes].getText()  # Valor relacionado ao campo
        
        if numero_atualizacoes > 0: 
            atualizacoes_text += ', '
        atualizacoes_text += f'{atualizacao.getText()} = {valor}'
        numero_atualizacoes += 1
    
    return atualizacoes_text

    atualizacoes_text = ""
    numero_atualizacoes = 0
    for atualizacao in atualizacoes:
        if numero_atualizacoes > 0: atualizacoes_text += ', '
        atualizacoes_text += f'{atualizacao.IDENTIFICADOR().getText()} = {atualizacao.valor().getText()}'
        numero_atualizacoes += 1
    
    return atualizacoes_text

def translate_command(query):
    sql_command = ""

    if "MOSTRAR" in query.getText():
        campos_text = analize_campos(query.campos())

        sql_command = f'SELECT {campos_text} FROM {query.IDENTIFICADOR().getText()}'

        sql_grupos = ''
        if query.grupos():
            grupos_text = analize_grupos(query.grupos())
            sql_grupos += f' GROUP BY {grupos_text}'

        sql_condicoes = ''
        if query.condicoes():
            condicoes_text = analize_condicoes(query.condicoes())

            if query.grupos() and any(func in condicoes_text for func in ["SUM(", "COUNT(", "AVG(", "MAX(", "MIN("]):
                sql_condicoes += f' HAVING {condicoes_text}'
            else:
                sql_condicoes += f' WHERE {condicoes_text}'
        
        if 'WHERE' in sql_condicoes: sql_command += sql_condicoes + sql_grupos
        else: sql_command += sql_grupos + sql_condicoes
        
        sql_command += ';'
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
    elif "CRIAR" in query.getText(): 
        sql_command = f'CREATE TABLE {query.IDENTIFICADOR().getText()} '

        definicoes_text = analize_definicoes(query.definicoes())
        sql_command += f'({definicoes_text});'
    elif "ATUALIZAR" in query.getText(): 
        sql_command = f'UPDATE {query.IDENTIFICADOR().getText()} SET '

        atualizacoes_text = analize_atualizacoes(query.atualizacoes())
        sql_command += atualizacoes_text

        if query.condicoes():
            condicoes_text = analize_condicoes(query.condicoes())
            sql_command += f' WHERE {condicoes_text}'

        sql_command += ';'
    else:
        raise ValueError("Comando Inválido")

    return sql_command

while True:
    input_text = input("Digite a consulta:")
    if input_text.strip() == "":
        break

    input_stream = InputStream(input_text)
    lexer = EasySQLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = EasySQLParser(stream)
    query = parser.prog().query()
    sql_command = translate_command(query)

    print(executar_sql(sql_command))