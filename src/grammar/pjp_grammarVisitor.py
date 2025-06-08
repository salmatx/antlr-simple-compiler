# Generated from grammar/pjp_grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .pjp_grammarParser import pjp_grammarParser
else:
    from pjp_grammarParser import pjp_grammarParser

# This class defines a complete generic visitor for a parse tree produced by pjp_grammarParser.

class pjp_grammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pjp_grammarParser#program.
    def visitProgram(self, ctx:pjp_grammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#EmptyStmt.
    def visitEmptyStmt(self, ctx:pjp_grammarParser.EmptyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#VarDecl.
    def visitVarDecl(self, ctx:pjp_grammarParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#ExprStmt.
    def visitExprStmt(self, ctx:pjp_grammarParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#ReadStmt.
    def visitReadStmt(self, ctx:pjp_grammarParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#WriteStmt.
    def visitWriteStmt(self, ctx:pjp_grammarParser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#BlockStmt.
    def visitBlockStmt(self, ctx:pjp_grammarParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#IfStmt.
    def visitIfStmt(self, ctx:pjp_grammarParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#WhileStmt.
    def visitWhileStmt(self, ctx:pjp_grammarParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#DoWhileStmt.
    def visitDoWhileStmt(self, ctx:pjp_grammarParser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#ForStmt.
    def visitForStmt(self, ctx:pjp_grammarParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#BoolCondition.
    def visitBoolCondition(self, ctx:pjp_grammarParser.BoolConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#MulExpr.
    def visitMulExpr(self, ctx:pjp_grammarParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#AndExpr.
    def visitAndExpr(self, ctx:pjp_grammarParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#MuduloExpr.
    def visitMuduloExpr(self, ctx:pjp_grammarParser.MuduloExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#RelExpr.
    def visitRelExpr(self, ctx:pjp_grammarParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#NegExpr.
    def visitNegExpr(self, ctx:pjp_grammarParser.NegExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#AddExpr.
    def visitAddExpr(self, ctx:pjp_grammarParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#OrExpr.
    def visitOrExpr(self, ctx:pjp_grammarParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#AssignExpr.
    def visitAssignExpr(self, ctx:pjp_grammarParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#ConcatExpr.
    def visitConcatExpr(self, ctx:pjp_grammarParser.ConcatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#EqExpr.
    def visitEqExpr(self, ctx:pjp_grammarParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#ParensExpr.
    def visitParensExpr(self, ctx:pjp_grammarParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#VarExpr.
    def visitVarExpr(self, ctx:pjp_grammarParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#LiteralExpr.
    def visitLiteralExpr(self, ctx:pjp_grammarParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#NotExpr.
    def visitNotExpr(self, ctx:pjp_grammarParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#TernaryExpr.
    def visitTernaryExpr(self, ctx:pjp_grammarParser.TernaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pjp_grammarParser#literal.
    def visitLiteral(self, ctx:pjp_grammarParser.LiteralContext):
        return self.visitChildren(ctx)



del pjp_grammarParser