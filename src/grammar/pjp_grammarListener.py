# Generated from grammar/pjp_grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .pjp_grammarParser import pjp_grammarParser
else:
    from pjp_grammarParser import pjp_grammarParser

# This class defines a complete listener for a parse tree produced by pjp_grammarParser.
class pjp_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by pjp_grammarParser#program.
    def enterProgram(self, ctx:pjp_grammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#program.
    def exitProgram(self, ctx:pjp_grammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#EmptyStmt.
    def enterEmptyStmt(self, ctx:pjp_grammarParser.EmptyStmtContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#EmptyStmt.
    def exitEmptyStmt(self, ctx:pjp_grammarParser.EmptyStmtContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#VarDecl.
    def enterVarDecl(self, ctx:pjp_grammarParser.VarDeclContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#VarDecl.
    def exitVarDecl(self, ctx:pjp_grammarParser.VarDeclContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#ExprStmt.
    def enterExprStmt(self, ctx:pjp_grammarParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#ExprStmt.
    def exitExprStmt(self, ctx:pjp_grammarParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#ReadStmt.
    def enterReadStmt(self, ctx:pjp_grammarParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#ReadStmt.
    def exitReadStmt(self, ctx:pjp_grammarParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#WriteStmt.
    def enterWriteStmt(self, ctx:pjp_grammarParser.WriteStmtContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#WriteStmt.
    def exitWriteStmt(self, ctx:pjp_grammarParser.WriteStmtContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#BlockStmt.
    def enterBlockStmt(self, ctx:pjp_grammarParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#BlockStmt.
    def exitBlockStmt(self, ctx:pjp_grammarParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#IfStmt.
    def enterIfStmt(self, ctx:pjp_grammarParser.IfStmtContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#IfStmt.
    def exitIfStmt(self, ctx:pjp_grammarParser.IfStmtContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#WhileStmt.
    def enterWhileStmt(self, ctx:pjp_grammarParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#WhileStmt.
    def exitWhileStmt(self, ctx:pjp_grammarParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#DoWhileStmt.
    def enterDoWhileStmt(self, ctx:pjp_grammarParser.DoWhileStmtContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#DoWhileStmt.
    def exitDoWhileStmt(self, ctx:pjp_grammarParser.DoWhileStmtContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#ForStmt.
    def enterForStmt(self, ctx:pjp_grammarParser.ForStmtContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#ForStmt.
    def exitForStmt(self, ctx:pjp_grammarParser.ForStmtContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#BoolCondition.
    def enterBoolCondition(self, ctx:pjp_grammarParser.BoolConditionContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#BoolCondition.
    def exitBoolCondition(self, ctx:pjp_grammarParser.BoolConditionContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#MulExpr.
    def enterMulExpr(self, ctx:pjp_grammarParser.MulExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#MulExpr.
    def exitMulExpr(self, ctx:pjp_grammarParser.MulExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#AndExpr.
    def enterAndExpr(self, ctx:pjp_grammarParser.AndExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#AndExpr.
    def exitAndExpr(self, ctx:pjp_grammarParser.AndExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#MuduloExpr.
    def enterMuduloExpr(self, ctx:pjp_grammarParser.MuduloExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#MuduloExpr.
    def exitMuduloExpr(self, ctx:pjp_grammarParser.MuduloExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#RelExpr.
    def enterRelExpr(self, ctx:pjp_grammarParser.RelExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#RelExpr.
    def exitRelExpr(self, ctx:pjp_grammarParser.RelExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#NegExpr.
    def enterNegExpr(self, ctx:pjp_grammarParser.NegExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#NegExpr.
    def exitNegExpr(self, ctx:pjp_grammarParser.NegExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#AddExpr.
    def enterAddExpr(self, ctx:pjp_grammarParser.AddExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#AddExpr.
    def exitAddExpr(self, ctx:pjp_grammarParser.AddExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#OrExpr.
    def enterOrExpr(self, ctx:pjp_grammarParser.OrExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#OrExpr.
    def exitOrExpr(self, ctx:pjp_grammarParser.OrExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#AssignExpr.
    def enterAssignExpr(self, ctx:pjp_grammarParser.AssignExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#AssignExpr.
    def exitAssignExpr(self, ctx:pjp_grammarParser.AssignExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#ConcatExpr.
    def enterConcatExpr(self, ctx:pjp_grammarParser.ConcatExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#ConcatExpr.
    def exitConcatExpr(self, ctx:pjp_grammarParser.ConcatExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#EqExpr.
    def enterEqExpr(self, ctx:pjp_grammarParser.EqExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#EqExpr.
    def exitEqExpr(self, ctx:pjp_grammarParser.EqExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#ParensExpr.
    def enterParensExpr(self, ctx:pjp_grammarParser.ParensExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#ParensExpr.
    def exitParensExpr(self, ctx:pjp_grammarParser.ParensExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#VarExpr.
    def enterVarExpr(self, ctx:pjp_grammarParser.VarExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#VarExpr.
    def exitVarExpr(self, ctx:pjp_grammarParser.VarExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:pjp_grammarParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:pjp_grammarParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#NotExpr.
    def enterNotExpr(self, ctx:pjp_grammarParser.NotExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#NotExpr.
    def exitNotExpr(self, ctx:pjp_grammarParser.NotExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#TernaryExpr.
    def enterTernaryExpr(self, ctx:pjp_grammarParser.TernaryExprContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#TernaryExpr.
    def exitTernaryExpr(self, ctx:pjp_grammarParser.TernaryExprContext):
        pass


    # Enter a parse tree produced by pjp_grammarParser#literal.
    def enterLiteral(self, ctx:pjp_grammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by pjp_grammarParser#literal.
    def exitLiteral(self, ctx:pjp_grammarParser.LiteralContext):
        pass



del pjp_grammarParser