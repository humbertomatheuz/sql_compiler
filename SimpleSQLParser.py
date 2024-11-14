# Generated from SimpleSQL.g4 by ANTLR 4.13.2
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
        4,1,12,46,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,1,0,3,0,21,8,0,1,1,1,1,1,1,1,1,5,1,27,8,1,
        10,1,12,1,30,9,1,3,1,32,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,5,
        1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,2,1,0,3,5,1,0,10,11,41,0,
        14,1,0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,35,1,0,0,0,8,37,1,0,0,0,10,
        41,1,0,0,0,12,43,1,0,0,0,14,15,5,6,0,0,15,16,3,2,1,0,16,17,5,7,0,
        0,17,20,3,6,3,0,18,19,5,8,0,0,19,21,3,8,4,0,20,18,1,0,0,0,20,21,
        1,0,0,0,21,1,1,0,0,0,22,32,5,1,0,0,23,28,3,4,2,0,24,25,5,2,0,0,25,
        27,3,4,2,0,26,24,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,
        0,29,32,1,0,0,0,30,28,1,0,0,0,31,22,1,0,0,0,31,23,1,0,0,0,32,3,1,
        0,0,0,33,34,5,9,0,0,34,5,1,0,0,0,35,36,5,9,0,0,36,7,1,0,0,0,37,38,
        3,4,2,0,38,39,3,10,5,0,39,40,3,12,6,0,40,9,1,0,0,0,41,42,7,0,0,0,
        42,11,1,0,0,0,43,44,7,1,0,0,44,13,1,0,0,0,3,20,28,31
    ]

class SimpleSQLParser ( Parser ):

    grammarFileName = "SimpleSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "','", "'='", "'<'", "'>'", "'SELECT'", 
                     "'FROM'", "'WHERE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SELECT", "FROM", "WHERE", 
                      "ID", "NUMBER", "STRING", "WS" ]

    RULE_query = 0
    RULE_columns = 1
    RULE_column = 2
    RULE_tableName = 3
    RULE_condition = 4
    RULE_op = 5
    RULE_value = 6

    ruleNames =  [ "query", "columns", "column", "tableName", "condition", 
                   "op", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    SELECT=6
    FROM=7
    WHERE=8
    ID=9
    NUMBER=10
    STRING=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(SimpleSQLParser.SELECT, 0)

        def columns(self):
            return self.getTypedRuleContext(SimpleSQLParser.ColumnsContext,0)


        def FROM(self):
            return self.getToken(SimpleSQLParser.FROM, 0)

        def tableName(self):
            return self.getTypedRuleContext(SimpleSQLParser.TableNameContext,0)


        def WHERE(self):
            return self.getToken(SimpleSQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(SimpleSQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return SimpleSQLParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = SimpleSQLParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(SimpleSQLParser.SELECT)
            self.state = 15
            self.columns()
            self.state = 16
            self.match(SimpleSQLParser.FROM)
            self.state = 17
            self.tableName()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 18
                self.match(SimpleSQLParser.WHERE)
                self.state = 19
                self.condition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleSQLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(SimpleSQLParser.ColumnContext,i)


        def getRuleIndex(self):
            return SimpleSQLParser.RULE_columns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumns" ):
                listener.enterColumns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumns" ):
                listener.exitColumns(self)




    def columns(self):

        localctx = SimpleSQLParser.ColumnsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_columns)
        self._la = 0 # Token type
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(SimpleSQLParser.T__0)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.column()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 24
                    self.match(SimpleSQLParser.T__1)
                    self.state = 25
                    self.column()
                    self.state = 30
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleSQLParser.ID, 0)

        def getRuleIndex(self):
            return SimpleSQLParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)




    def column(self):

        localctx = SimpleSQLParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(SimpleSQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleSQLParser.ID, 0)

        def getRuleIndex(self):
            return SimpleSQLParser.RULE_tableName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableName" ):
                listener.enterTableName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableName" ):
                listener.exitTableName(self)




    def tableName(self):

        localctx = SimpleSQLParser.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(SimpleSQLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(SimpleSQLParser.ColumnContext,0)


        def op(self):
            return self.getTypedRuleContext(SimpleSQLParser.OpContext,0)


        def value(self):
            return self.getTypedRuleContext(SimpleSQLParser.ValueContext,0)


        def getRuleIndex(self):
            return SimpleSQLParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = SimpleSQLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.column()
            self.state = 38
            self.op()
            self.state = 39
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleSQLParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)




    def op(self):

        localctx = SimpleSQLParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SimpleSQLParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(SimpleSQLParser.NUMBER, 0)

        def getRuleIndex(self):
            return SimpleSQLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = SimpleSQLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
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





