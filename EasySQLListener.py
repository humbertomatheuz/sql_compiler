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


    # Enter a parse tree produced by EasySQLParser#QuerySelect.
    def enterQuerySelect(self, ctx:EasySQLParser.QuerySelectContext):
        pass

    # Exit a parse tree produced by EasySQLParser#QuerySelect.
    def exitQuerySelect(self, ctx:EasySQLParser.QuerySelectContext):
        pass


    # Enter a parse tree produced by EasySQLParser#QueryInsert.
    def enterQueryInsert(self, ctx:EasySQLParser.QueryInsertContext):
        pass

    # Exit a parse tree produced by EasySQLParser#QueryInsert.
    def exitQueryInsert(self, ctx:EasySQLParser.QueryInsertContext):
        pass


    # Enter a parse tree produced by EasySQLParser#QueryDelete.
    def enterQueryDelete(self, ctx:EasySQLParser.QueryDeleteContext):
        pass

    # Exit a parse tree produced by EasySQLParser#QueryDelete.
    def exitQueryDelete(self, ctx:EasySQLParser.QueryDeleteContext):
        pass


    # Enter a parse tree produced by EasySQLParser#QueryDeleteTable.
    def enterQueryDeleteTable(self, ctx:EasySQLParser.QueryDeleteTableContext):
        pass

    # Exit a parse tree produced by EasySQLParser#QueryDeleteTable.
    def exitQueryDeleteTable(self, ctx:EasySQLParser.QueryDeleteTableContext):
        pass


    # Enter a parse tree produced by EasySQLParser#campos.
    def enterCampos(self, ctx:EasySQLParser.CamposContext):
        pass

    # Exit a parse tree produced by EasySQLParser#campos.
    def exitCampos(self, ctx:EasySQLParser.CamposContext):
        pass


    # Enter a parse tree produced by EasySQLParser#CampoComAgregador.
    def enterCampoComAgregador(self, ctx:EasySQLParser.CampoComAgregadorContext):
        pass

    # Exit a parse tree produced by EasySQLParser#CampoComAgregador.
    def exitCampoComAgregador(self, ctx:EasySQLParser.CampoComAgregadorContext):
        pass


    # Enter a parse tree produced by EasySQLParser#CampoSimples.
    def enterCampoSimples(self, ctx:EasySQLParser.CampoSimplesContext):
        pass

    # Exit a parse tree produced by EasySQLParser#CampoSimples.
    def exitCampoSimples(self, ctx:EasySQLParser.CampoSimplesContext):
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



del EasySQLParser