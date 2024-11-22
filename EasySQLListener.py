# Generated from EasySQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EasySQLParser import EasySQLParser
else:
    from EasySQLParser import EasySQLParser

# This class defines a complete listener for a parse tree produced by EasySQLParser.
class EasySQLListener(ParseTreeListener):

    # Enter a parse tree produced by EasySQLParser#prog.
    def enterProg(self, ctx:EasySQLParser.ProgContext):
        pass

    # Exit a parse tree produced by EasySQLParser#prog.
    def exitProg(self, ctx:EasySQLParser.ProgContext):
        pass


    # Enter a parse tree produced by EasySQLParser#query.
    def enterQuery(self, ctx:EasySQLParser.QueryContext):
        pass

    # Exit a parse tree produced by EasySQLParser#query.
    def exitQuery(self, ctx:EasySQLParser.QueryContext):
        pass


    # Enter a parse tree produced by EasySQLParser#campos.
    def enterCampos(self, ctx:EasySQLParser.CamposContext):
        pass

    # Exit a parse tree produced by EasySQLParser#campos.
    def exitCampos(self, ctx:EasySQLParser.CamposContext):
        pass


    # Enter a parse tree produced by EasySQLParser#campo.
    def enterCampo(self, ctx:EasySQLParser.CampoContext):
        pass

    # Exit a parse tree produced by EasySQLParser#campo.
    def exitCampo(self, ctx:EasySQLParser.CampoContext):
        pass


    # Enter a parse tree produced by EasySQLParser#definicoes.
    def enterDefinicoes(self, ctx:EasySQLParser.DefinicoesContext):
        pass

    # Exit a parse tree produced by EasySQLParser#definicoes.
    def exitDefinicoes(self, ctx:EasySQLParser.DefinicoesContext):
        pass


    # Enter a parse tree produced by EasySQLParser#definicao.
    def enterDefinicao(self, ctx:EasySQLParser.DefinicaoContext):
        pass

    # Exit a parse tree produced by EasySQLParser#definicao.
    def exitDefinicao(self, ctx:EasySQLParser.DefinicaoContext):
        pass


    # Enter a parse tree produced by EasySQLParser#grupos.
    def enterGrupos(self, ctx:EasySQLParser.GruposContext):
        pass

    # Exit a parse tree produced by EasySQLParser#grupos.
    def exitGrupos(self, ctx:EasySQLParser.GruposContext):
        pass


    # Enter a parse tree produced by EasySQLParser#condicoes.
    def enterCondicoes(self, ctx:EasySQLParser.CondicoesContext):
        pass

    # Exit a parse tree produced by EasySQLParser#condicoes.
    def exitCondicoes(self, ctx:EasySQLParser.CondicoesContext):
        pass


    # Enter a parse tree produced by EasySQLParser#condicao.
    def enterCondicao(self, ctx:EasySQLParser.CondicaoContext):
        pass

    # Exit a parse tree produced by EasySQLParser#condicao.
    def exitCondicao(self, ctx:EasySQLParser.CondicaoContext):
        pass


    # Enter a parse tree produced by EasySQLParser#colunas.
    def enterColunas(self, ctx:EasySQLParser.ColunasContext):
        pass

    # Exit a parse tree produced by EasySQLParser#colunas.
    def exitColunas(self, ctx:EasySQLParser.ColunasContext):
        pass


    # Enter a parse tree produced by EasySQLParser#valores.
    def enterValores(self, ctx:EasySQLParser.ValoresContext):
        pass

    # Exit a parse tree produced by EasySQLParser#valores.
    def exitValores(self, ctx:EasySQLParser.ValoresContext):
        pass


    # Enter a parse tree produced by EasySQLParser#operador.
    def enterOperador(self, ctx:EasySQLParser.OperadorContext):
        pass

    # Exit a parse tree produced by EasySQLParser#operador.
    def exitOperador(self, ctx:EasySQLParser.OperadorContext):
        pass


    # Enter a parse tree produced by EasySQLParser#valor.
    def enterValor(self, ctx:EasySQLParser.ValorContext):
        pass

    # Exit a parse tree produced by EasySQLParser#valor.
    def exitValor(self, ctx:EasySQLParser.ValorContext):
        pass


    # Enter a parse tree produced by EasySQLParser#tipo_dado.
    def enterTipo_dado(self, ctx:EasySQLParser.Tipo_dadoContext):
        pass

    # Exit a parse tree produced by EasySQLParser#tipo_dado.
    def exitTipo_dado(self, ctx:EasySQLParser.Tipo_dadoContext):
        pass



del EasySQLParser