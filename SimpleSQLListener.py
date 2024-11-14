# Generated from SimpleSQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleSQLParser import SimpleSQLParser
else:
    from SimpleSQLParser import SimpleSQLParser

# This class defines a complete listener for a parse tree produced by SimpleSQLParser.
class SimpleSQLListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleSQLParser#query.
    def enterQuery(self, ctx:SimpleSQLParser.QueryContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#query.
    def exitQuery(self, ctx:SimpleSQLParser.QueryContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#columns.
    def enterColumns(self, ctx:SimpleSQLParser.ColumnsContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#columns.
    def exitColumns(self, ctx:SimpleSQLParser.ColumnsContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#column.
    def enterColumn(self, ctx:SimpleSQLParser.ColumnContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#column.
    def exitColumn(self, ctx:SimpleSQLParser.ColumnContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#tableName.
    def enterTableName(self, ctx:SimpleSQLParser.TableNameContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#tableName.
    def exitTableName(self, ctx:SimpleSQLParser.TableNameContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#condition.
    def enterCondition(self, ctx:SimpleSQLParser.ConditionContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#condition.
    def exitCondition(self, ctx:SimpleSQLParser.ConditionContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#op.
    def enterOp(self, ctx:SimpleSQLParser.OpContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#op.
    def exitOp(self, ctx:SimpleSQLParser.OpContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#value.
    def enterValue(self, ctx:SimpleSQLParser.ValueContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#value.
    def exitValue(self, ctx:SimpleSQLParser.ValueContext):
        pass



del SimpleSQLParser