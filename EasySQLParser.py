# Generated from EasySQL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,119,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        3,1,30,8,1,1,1,1,1,3,1,34,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,44,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,56,8,1,1,1,
        1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,5,2,67,8,2,10,2,12,2,70,9,2,1,
        3,1,3,1,3,1,3,1,3,3,3,77,8,3,1,4,1,4,1,4,5,4,82,8,4,10,4,12,4,85,
        9,4,1,5,1,5,1,5,5,5,90,8,5,10,5,12,5,93,9,5,1,6,1,6,1,6,1,6,1,7,
        1,7,1,7,5,7,102,8,7,10,7,12,7,105,9,7,1,8,1,8,1,8,5,8,110,8,8,10,
        8,12,8,113,9,8,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,
        16,18,20,0,2,1,0,12,17,1,0,20,21,120,0,22,1,0,0,0,2,61,1,0,0,0,4,
        63,1,0,0,0,6,76,1,0,0,0,8,78,1,0,0,0,10,86,1,0,0,0,12,94,1,0,0,0,
        14,98,1,0,0,0,16,106,1,0,0,0,18,114,1,0,0,0,20,116,1,0,0,0,22,23,
        3,2,1,0,23,24,5,0,0,1,24,1,1,0,0,0,25,26,5,1,0,0,26,29,3,4,2,0,27,
        28,5,2,0,0,28,30,3,8,4,0,29,27,1,0,0,0,29,30,1,0,0,0,30,33,1,0,0,
        0,31,32,5,3,0,0,32,34,3,10,5,0,33,31,1,0,0,0,33,34,1,0,0,0,34,35,
        1,0,0,0,35,36,5,22,0,0,36,62,1,0,0,0,37,38,5,4,0,0,38,43,5,19,0,
        0,39,40,5,5,0,0,40,41,3,14,7,0,41,42,5,6,0,0,42,44,1,0,0,0,43,39,
        1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,5,7,0,0,46,47,5,5,0,0,
        47,48,3,16,8,0,48,49,5,6,0,0,49,50,5,22,0,0,50,62,1,0,0,0,51,52,
        5,8,0,0,52,55,5,19,0,0,53,54,5,3,0,0,54,56,3,10,5,0,55,53,1,0,0,
        0,55,56,1,0,0,0,56,57,1,0,0,0,57,62,5,22,0,0,58,59,5,9,0,0,59,60,
        5,19,0,0,60,62,5,22,0,0,61,25,1,0,0,0,61,37,1,0,0,0,61,51,1,0,0,
        0,61,58,1,0,0,0,62,3,1,0,0,0,63,68,3,6,3,0,64,65,5,10,0,0,65,67,
        3,6,3,0,66,64,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,
        69,5,1,0,0,0,70,68,1,0,0,0,71,72,5,18,0,0,72,73,5,5,0,0,73,74,5,
        19,0,0,74,77,5,6,0,0,75,77,5,19,0,0,76,71,1,0,0,0,76,75,1,0,0,0,
        77,7,1,0,0,0,78,83,5,19,0,0,79,80,5,10,0,0,80,82,5,19,0,0,81,79,
        1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,9,1,0,0,0,85,
        83,1,0,0,0,86,91,3,12,6,0,87,88,5,11,0,0,88,90,3,12,6,0,89,87,1,
        0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,11,1,0,0,0,93,
        91,1,0,0,0,94,95,5,19,0,0,95,96,3,18,9,0,96,97,3,20,10,0,97,13,1,
        0,0,0,98,103,5,19,0,0,99,100,5,10,0,0,100,102,5,19,0,0,101,99,1,
        0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,15,1,0,
        0,0,105,103,1,0,0,0,106,111,3,20,10,0,107,108,5,10,0,0,108,110,3,
        20,10,0,109,107,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,
        1,0,0,0,112,17,1,0,0,0,113,111,1,0,0,0,114,115,7,0,0,0,115,19,1,
        0,0,0,116,117,7,1,0,0,117,21,1,0,0,0,11,29,33,43,55,61,68,76,83,
        91,103,111
    ]

class EasySQLParser ( Parser ):

    grammarFileName = "EasySQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'MOSTRAR'", "'POR'", "'ONDE'", "'INSERIR EM'", 
                     "'('", "')'", "'VALORES'", "'REMOVER DE'", "'DELETAR TABELA'", 
                     "','", "'E'", "'='", "'<'", "'>'", "'<='", "'>='", 
                     "'!='", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "AGREGADOR", "IDENTIFICADOR", 
                      "NUMERO", "STRING", "SEMICOLON", "WS" ]

    RULE_prog = 0
    RULE_query = 1
    RULE_campos = 2
    RULE_campo = 3
    RULE_grupos = 4
    RULE_condicoes = 5
    RULE_condicao = 6
    RULE_colunas = 7
    RULE_valores = 8
    RULE_operador = 9
    RULE_valor = 10

    ruleNames =  [ "prog", "query", "campos", "campo", "grupos", "condicoes", 
                   "condicao", "colunas", "valores", "operador", "valor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    AGREGADOR=18
    IDENTIFICADOR=19
    NUMERO=20
    STRING=21
    SEMICOLON=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def query(self):
            return self.getTypedRuleContext(EasySQLParser.QueryContext,0)


        def EOF(self):
            return self.getToken(EasySQLParser.EOF, 0)

        def getRuleIndex(self):
            return EasySQLParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = EasySQLParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.query()
            self.state = 23
            self.match(EasySQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EasySQLParser.RULE_query

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class QueryDeleteContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EasySQLParser.QueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFICADOR(self):
            return self.getToken(EasySQLParser.IDENTIFICADOR, 0)
        def SEMICOLON(self):
            return self.getToken(EasySQLParser.SEMICOLON, 0)
        def condicoes(self):
            return self.getTypedRuleContext(EasySQLParser.CondicoesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryDelete" ):
                listener.enterQueryDelete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryDelete" ):
                listener.exitQueryDelete(self)


    class QueryInsertContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EasySQLParser.QueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFICADOR(self):
            return self.getToken(EasySQLParser.IDENTIFICADOR, 0)
        def valores(self):
            return self.getTypedRuleContext(EasySQLParser.ValoresContext,0)

        def SEMICOLON(self):
            return self.getToken(EasySQLParser.SEMICOLON, 0)
        def colunas(self):
            return self.getTypedRuleContext(EasySQLParser.ColunasContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryInsert" ):
                listener.enterQueryInsert(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryInsert" ):
                listener.exitQueryInsert(self)


    class QueryDeleteTableContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EasySQLParser.QueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFICADOR(self):
            return self.getToken(EasySQLParser.IDENTIFICADOR, 0)
        def SEMICOLON(self):
            return self.getToken(EasySQLParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryDeleteTable" ):
                listener.enterQueryDeleteTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryDeleteTable" ):
                listener.exitQueryDeleteTable(self)


    class QuerySelectContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EasySQLParser.QueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def campos(self):
            return self.getTypedRuleContext(EasySQLParser.CamposContext,0)

        def SEMICOLON(self):
            return self.getToken(EasySQLParser.SEMICOLON, 0)
        def grupos(self):
            return self.getTypedRuleContext(EasySQLParser.GruposContext,0)

        def condicoes(self):
            return self.getTypedRuleContext(EasySQLParser.CondicoesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuerySelect" ):
                listener.enterQuerySelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuerySelect" ):
                listener.exitQuerySelect(self)



    def query(self):

        localctx = EasySQLParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = EasySQLParser.QuerySelectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(EasySQLParser.T__0)
                self.state = 26
                self.campos()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 27
                    self.match(EasySQLParser.T__1)
                    self.state = 28
                    self.grupos()


                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 31
                    self.match(EasySQLParser.T__2)
                    self.state = 32
                    self.condicoes()


                self.state = 35
                self.match(EasySQLParser.SEMICOLON)
                pass
            elif token in [4]:
                localctx = EasySQLParser.QueryInsertContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(EasySQLParser.T__3)
                self.state = 38
                self.match(EasySQLParser.IDENTIFICADOR)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 39
                    self.match(EasySQLParser.T__4)
                    self.state = 40
                    self.colunas()
                    self.state = 41
                    self.match(EasySQLParser.T__5)


                self.state = 45
                self.match(EasySQLParser.T__6)
                self.state = 46
                self.match(EasySQLParser.T__4)
                self.state = 47
                self.valores()
                self.state = 48
                self.match(EasySQLParser.T__5)
                self.state = 49
                self.match(EasySQLParser.SEMICOLON)
                pass
            elif token in [8]:
                localctx = EasySQLParser.QueryDeleteContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.match(EasySQLParser.T__7)
                self.state = 52
                self.match(EasySQLParser.IDENTIFICADOR)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 53
                    self.match(EasySQLParser.T__2)
                    self.state = 54
                    self.condicoes()


                self.state = 57
                self.match(EasySQLParser.SEMICOLON)
                pass
            elif token in [9]:
                localctx = EasySQLParser.QueryDeleteTableContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.match(EasySQLParser.T__8)
                self.state = 59
                self.match(EasySQLParser.IDENTIFICADOR)
                self.state = 60
                self.match(EasySQLParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CamposContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def campo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasySQLParser.CampoContext)
            else:
                return self.getTypedRuleContext(EasySQLParser.CampoContext,i)


        def getRuleIndex(self):
            return EasySQLParser.RULE_campos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCampos" ):
                listener.enterCampos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCampos" ):
                listener.exitCampos(self)




    def campos(self):

        localctx = EasySQLParser.CamposContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_campos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.campo()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 64
                self.match(EasySQLParser.T__9)
                self.state = 65
                self.campo()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EasySQLParser.RULE_campo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CampoSimplesContext(CampoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EasySQLParser.CampoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFICADOR(self):
            return self.getToken(EasySQLParser.IDENTIFICADOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCampoSimples" ):
                listener.enterCampoSimples(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCampoSimples" ):
                listener.exitCampoSimples(self)


    class CampoComAgregadorContext(CampoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a EasySQLParser.CampoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AGREGADOR(self):
            return self.getToken(EasySQLParser.AGREGADOR, 0)
        def IDENTIFICADOR(self):
            return self.getToken(EasySQLParser.IDENTIFICADOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCampoComAgregador" ):
                listener.enterCampoComAgregador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCampoComAgregador" ):
                listener.exitCampoComAgregador(self)



    def campo(self):

        localctx = EasySQLParser.CampoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_campo)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = EasySQLParser.CampoComAgregadorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(EasySQLParser.AGREGADOR)
                self.state = 72
                self.match(EasySQLParser.T__4)
                self.state = 73
                self.match(EasySQLParser.IDENTIFICADOR)
                self.state = 74
                self.match(EasySQLParser.T__5)
                pass
            elif token in [19]:
                localctx = EasySQLParser.CampoSimplesContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(EasySQLParser.IDENTIFICADOR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GruposContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self, i:int=None):
            if i is None:
                return self.getTokens(EasySQLParser.IDENTIFICADOR)
            else:
                return self.getToken(EasySQLParser.IDENTIFICADOR, i)

        def getRuleIndex(self):
            return EasySQLParser.RULE_grupos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrupos" ):
                listener.enterGrupos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrupos" ):
                listener.exitGrupos(self)




    def grupos(self):

        localctx = EasySQLParser.GruposContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_grupos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(EasySQLParser.IDENTIFICADOR)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 79
                self.match(EasySQLParser.T__9)
                self.state = 80
                self.match(EasySQLParser.IDENTIFICADOR)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasySQLParser.CondicaoContext)
            else:
                return self.getTypedRuleContext(EasySQLParser.CondicaoContext,i)


        def getRuleIndex(self):
            return EasySQLParser.RULE_condicoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicoes" ):
                listener.enterCondicoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicoes" ):
                listener.exitCondicoes(self)




    def condicoes(self):

        localctx = EasySQLParser.CondicoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_condicoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.condicao()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 87
                self.match(EasySQLParser.T__10)
                self.state = 88
                self.condicao()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(EasySQLParser.IDENTIFICADOR, 0)

        def operador(self):
            return self.getTypedRuleContext(EasySQLParser.OperadorContext,0)


        def valor(self):
            return self.getTypedRuleContext(EasySQLParser.ValorContext,0)


        def getRuleIndex(self):
            return EasySQLParser.RULE_condicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicao" ):
                listener.enterCondicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicao" ):
                listener.exitCondicao(self)




    def condicao(self):

        localctx = EasySQLParser.CondicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(EasySQLParser.IDENTIFICADOR)
            self.state = 95
            self.operador()
            self.state = 96
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColunasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self, i:int=None):
            if i is None:
                return self.getTokens(EasySQLParser.IDENTIFICADOR)
            else:
                return self.getToken(EasySQLParser.IDENTIFICADOR, i)

        def getRuleIndex(self):
            return EasySQLParser.RULE_colunas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColunas" ):
                listener.enterColunas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColunas" ):
                listener.exitColunas(self)




    def colunas(self):

        localctx = EasySQLParser.ColunasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_colunas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(EasySQLParser.IDENTIFICADOR)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 99
                self.match(EasySQLParser.T__9)
                self.state = 100
                self.match(EasySQLParser.IDENTIFICADOR)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasySQLParser.ValorContext)
            else:
                return self.getTypedRuleContext(EasySQLParser.ValorContext,i)


        def getRuleIndex(self):
            return EasySQLParser.RULE_valores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValores" ):
                listener.enterValores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValores" ):
                listener.exitValores(self)




    def valores(self):

        localctx = EasySQLParser.ValoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_valores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.valor()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 107
                self.match(EasySQLParser.T__9)
                self.state = 108
                self.valor()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EasySQLParser.RULE_operador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperador" ):
                listener.enterOperador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperador" ):
                listener.exitOperador(self)




    def operador(self):

        localctx = EasySQLParser.OperadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(EasySQLParser.STRING, 0)

        def NUMERO(self):
            return self.getToken(EasySQLParser.NUMERO, 0)

        def getRuleIndex(self):
            return EasySQLParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)




    def valor(self):

        localctx = EasySQLParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





