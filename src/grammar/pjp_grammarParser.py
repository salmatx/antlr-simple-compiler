# Generated from grammar/pjp_grammar.g4 by ANTLR 4.13.2
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
        4,1,37,149,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,
        0,11,0,12,0,13,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,34,8,1,10,1,12,1,37,9,1,1,1,1,
        1,1,1,1,1,1,1,5,1,44,8,1,10,1,12,1,47,9,1,1,1,1,1,1,1,1,1,5,1,53,
        8,1,10,1,12,1,56,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,66,8,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,92,8,1,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,110,8,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,142,8,3,10,3,12,
        3,145,9,3,1,4,1,4,1,4,0,1,6,5,0,2,4,6,8,0,5,1,0,16,17,2,0,14,14,
        19,19,1,0,21,22,1,0,23,24,1,0,30,33,172,0,11,1,0,0,0,2,91,1,0,0,
        0,4,93,1,0,0,0,6,109,1,0,0,0,8,146,1,0,0,0,10,12,3,2,1,0,11,10,1,
        0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,0,15,
        92,5,1,0,0,16,17,5,34,0,0,17,22,5,35,0,0,18,19,5,2,0,0,19,21,5,35,
        0,0,20,18,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,25,
        1,0,0,0,24,22,1,0,0,0,25,92,5,1,0,0,26,27,3,6,3,0,27,28,5,1,0,0,
        28,92,1,0,0,0,29,30,5,3,0,0,30,35,5,35,0,0,31,32,5,2,0,0,32,34,5,
        35,0,0,33,31,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,
        38,1,0,0,0,37,35,1,0,0,0,38,92,5,1,0,0,39,40,5,4,0,0,40,45,3,6,3,
        0,41,42,5,2,0,0,42,44,3,6,3,0,43,41,1,0,0,0,44,47,1,0,0,0,45,43,
        1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,45,1,0,0,0,48,49,5,1,0,0,
        49,92,1,0,0,0,50,54,5,5,0,0,51,53,3,2,1,0,52,51,1,0,0,0,53,56,1,
        0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,57,1,0,0,0,56,54,1,0,0,0,57,
        92,5,6,0,0,58,59,5,7,0,0,59,60,5,8,0,0,60,61,3,4,2,0,61,62,5,9,0,
        0,62,65,3,2,1,0,63,64,5,10,0,0,64,66,3,2,1,0,65,63,1,0,0,0,65,66,
        1,0,0,0,66,92,1,0,0,0,67,68,5,11,0,0,68,69,5,8,0,0,69,70,3,4,2,0,
        70,71,5,9,0,0,71,72,3,2,1,0,72,92,1,0,0,0,73,74,5,12,0,0,74,75,3,
        2,1,0,75,76,5,11,0,0,76,77,5,8,0,0,77,78,3,4,2,0,78,79,5,9,0,0,79,
        80,5,1,0,0,80,92,1,0,0,0,81,82,5,13,0,0,82,83,5,8,0,0,83,84,3,6,
        3,0,84,85,5,1,0,0,85,86,3,4,2,0,86,87,5,1,0,0,87,88,3,6,3,0,88,89,
        5,9,0,0,89,90,3,2,1,0,90,92,1,0,0,0,91,15,1,0,0,0,91,16,1,0,0,0,
        91,26,1,0,0,0,91,29,1,0,0,0,91,39,1,0,0,0,91,50,1,0,0,0,91,58,1,
        0,0,0,91,67,1,0,0,0,91,73,1,0,0,0,91,81,1,0,0,0,92,3,1,0,0,0,93,
        94,3,6,3,0,94,5,1,0,0,0,95,96,6,3,-1,0,96,97,5,8,0,0,97,98,3,6,3,
        0,98,99,5,9,0,0,99,110,1,0,0,0,100,101,5,14,0,0,101,110,3,6,3,14,
        102,103,5,15,0,0,103,110,3,6,3,13,104,110,5,35,0,0,105,110,3,8,4,
        0,106,107,5,35,0,0,107,108,5,29,0,0,108,110,3,6,3,1,109,95,1,0,0,
        0,109,100,1,0,0,0,109,102,1,0,0,0,109,104,1,0,0,0,109,105,1,0,0,
        0,109,106,1,0,0,0,110,143,1,0,0,0,111,112,10,12,0,0,112,113,7,0,
        0,0,113,142,3,6,3,13,114,115,10,11,0,0,115,116,5,18,0,0,116,142,
        3,6,3,12,117,118,10,10,0,0,118,119,7,1,0,0,119,142,3,6,3,11,120,
        121,10,9,0,0,121,122,5,20,0,0,122,142,3,6,3,10,123,124,10,8,0,0,
        124,125,7,2,0,0,125,142,3,6,3,9,126,127,10,7,0,0,127,128,7,3,0,0,
        128,142,3,6,3,8,129,130,10,6,0,0,130,131,5,25,0,0,131,142,3,6,3,
        7,132,133,10,5,0,0,133,134,5,26,0,0,134,142,3,6,3,6,135,136,10,2,
        0,0,136,137,5,27,0,0,137,138,3,6,3,0,138,139,5,28,0,0,139,140,3,
        6,3,3,140,142,1,0,0,0,141,111,1,0,0,0,141,114,1,0,0,0,141,117,1,
        0,0,0,141,120,1,0,0,0,141,123,1,0,0,0,141,126,1,0,0,0,141,129,1,
        0,0,0,141,132,1,0,0,0,141,135,1,0,0,0,142,145,1,0,0,0,143,141,1,
        0,0,0,143,144,1,0,0,0,144,7,1,0,0,0,145,143,1,0,0,0,146,147,7,4,
        0,0,147,9,1,0,0,0,10,13,22,35,45,54,65,91,109,141,143
    ]

class pjp_grammarParser ( Parser ):

    grammarFileName = "pjp_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'read'", "'write'", "'{'", 
                     "'}'", "'if'", "'('", "')'", "'else'", "'while'", "'do'", 
                     "'for'", "'-'", "'!'", "'*'", "'/'", "'%'", "'+'", 
                     "'.'", "'<'", "'>'", "'=='", "'!='", "'&&'", "'||'", 
                     "'?'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "FLOAT", "BOOL", 
                      "STRING", "TYPE", "VAR", "COMMENT", "SPACE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_condition = 2
    RULE_expression = 3
    RULE_literal = 4

    ruleNames =  [ "program", "statement", "condition", "expression", "literal" ]

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
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    INT=30
    FLOAT=31
    BOOL=32
    STRING=33
    TYPE=34
    VAR=35
    COMMENT=36
    SPACE=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pjp_grammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(pjp_grammarParser.StatementContext,i)


        def getRuleIndex(self):
            return pjp_grammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = pjp_grammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.statement()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 67645798842) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pjp_grammarParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition(self):
            return self.getTypedRuleContext(pjp_grammarParser.ConditionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pjp_grammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(pjp_grammarParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class ExprStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)


    class VarDeclContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE(self):
            return self.getToken(pjp_grammarParser.TYPE, 0)
        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(pjp_grammarParser.VAR)
            else:
                return self.getToken(pjp_grammarParser.VAR, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)


    class WhileStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition(self):
            return self.getTypedRuleContext(pjp_grammarParser.ConditionContext,0)

        def statement(self):
            return self.getTypedRuleContext(pjp_grammarParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class BlockStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pjp_grammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(pjp_grammarParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStmt" ):
                listener.enterBlockStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStmt" ):
                listener.exitBlockStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)


    class WriteStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pjp_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStmt" ):
                listener.enterWriteStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStmt" ):
                listener.exitWriteStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStmt" ):
                return visitor.visitWriteStmt(self)
            else:
                return visitor.visitChildren(self)


    class ReadStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(pjp_grammarParser.VAR)
            else:
                return self.getToken(pjp_grammarParser.VAR, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStmt" ):
                listener.enterReadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStmt" ):
                listener.exitReadStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStmt" ):
                return visitor.visitReadStmt(self)
            else:
                return visitor.visitChildren(self)


    class EmptyStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStmt" ):
                listener.enterEmptyStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStmt" ):
                listener.exitEmptyStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStmt" ):
                return visitor.visitEmptyStmt(self)
            else:
                return visitor.visitChildren(self)


    class DoWhileStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(pjp_grammarParser.StatementContext,0)

        def condition(self):
            return self.getTypedRuleContext(pjp_grammarParser.ConditionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStmt" ):
                listener.enterDoWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStmt" ):
                listener.exitDoWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhileStmt" ):
                return visitor.visitDoWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class ForStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pjp_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,i)

        def condition(self):
            return self.getTypedRuleContext(pjp_grammarParser.ConditionContext,0)

        def statement(self):
            return self.getTypedRuleContext(pjp_grammarParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = pjp_grammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = pjp_grammarParser.EmptyStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(pjp_grammarParser.T__0)
                pass
            elif token in [34]:
                localctx = pjp_grammarParser.VarDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(pjp_grammarParser.TYPE)
                self.state = 17
                self.match(pjp_grammarParser.VAR)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 18
                    self.match(pjp_grammarParser.T__1)
                    self.state = 19
                    self.match(pjp_grammarParser.VAR)
                    self.state = 24
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 25
                self.match(pjp_grammarParser.T__0)
                pass
            elif token in [8, 14, 15, 30, 31, 32, 33, 35]:
                localctx = pjp_grammarParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.expression(0)
                self.state = 27
                self.match(pjp_grammarParser.T__0)
                pass
            elif token in [3]:
                localctx = pjp_grammarParser.ReadStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.match(pjp_grammarParser.T__2)
                self.state = 30
                self.match(pjp_grammarParser.VAR)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 31
                    self.match(pjp_grammarParser.T__1)
                    self.state = 32
                    self.match(pjp_grammarParser.VAR)
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 38
                self.match(pjp_grammarParser.T__0)
                pass
            elif token in [4]:
                localctx = pjp_grammarParser.WriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                self.match(pjp_grammarParser.T__3)
                self.state = 40
                self.expression(0)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 41
                    self.match(pjp_grammarParser.T__1)
                    self.state = 42
                    self.expression(0)
                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 48
                self.match(pjp_grammarParser.T__0)
                pass
            elif token in [5]:
                localctx = pjp_grammarParser.BlockStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 50
                self.match(pjp_grammarParser.T__4)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67645798842) != 0):
                    self.state = 51
                    self.statement()
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 57
                self.match(pjp_grammarParser.T__5)
                pass
            elif token in [7]:
                localctx = pjp_grammarParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 58
                self.match(pjp_grammarParser.T__6)
                self.state = 59
                self.match(pjp_grammarParser.T__7)
                self.state = 60
                self.condition()
                self.state = 61
                self.match(pjp_grammarParser.T__8)
                self.state = 62
                self.statement()
                self.state = 65
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 63
                    self.match(pjp_grammarParser.T__9)
                    self.state = 64
                    self.statement()


                pass
            elif token in [11]:
                localctx = pjp_grammarParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 67
                self.match(pjp_grammarParser.T__10)
                self.state = 68
                self.match(pjp_grammarParser.T__7)
                self.state = 69
                self.condition()
                self.state = 70
                self.match(pjp_grammarParser.T__8)
                self.state = 71
                self.statement()
                pass
            elif token in [12]:
                localctx = pjp_grammarParser.DoWhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 73
                self.match(pjp_grammarParser.T__11)
                self.state = 74
                self.statement()
                self.state = 75
                self.match(pjp_grammarParser.T__10)
                self.state = 76
                self.match(pjp_grammarParser.T__7)
                self.state = 77
                self.condition()
                self.state = 78
                self.match(pjp_grammarParser.T__8)
                self.state = 79
                self.match(pjp_grammarParser.T__0)
                pass
            elif token in [13]:
                localctx = pjp_grammarParser.ForStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 81
                self.match(pjp_grammarParser.T__12)
                self.state = 82
                self.match(pjp_grammarParser.T__7)
                self.state = 83
                self.expression(0)
                self.state = 84
                self.match(pjp_grammarParser.T__0)
                self.state = 85
                self.condition()
                self.state = 86
                self.match(pjp_grammarParser.T__0)
                self.state = 87
                self.expression(0)
                self.state = 88
                self.match(pjp_grammarParser.T__8)
                self.state = 89
                self.statement()
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


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pjp_grammarParser.RULE_condition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BoolConditionContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolCondition" ):
                listener.enterBoolCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolCondition" ):
                listener.exitBoolCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolCondition" ):
                return visitor.visitBoolCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition(self):

        localctx = pjp_grammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_condition)
        try:
            localctx = pjp_grammarParser.BoolConditionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pjp_grammarParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pjp_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pjp_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class MuduloExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pjp_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMuduloExpr" ):
                listener.enterMuduloExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMuduloExpr" ):
                listener.exitMuduloExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMuduloExpr" ):
                return visitor.visitMuduloExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pjp_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelExpr" ):
                listener.enterRelExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelExpr" ):
                listener.exitRelExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegExpr" ):
                listener.enterNegExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegExpr" ):
                listener.exitNegExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegExpr" ):
                return visitor.visitNegExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pjp_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pjp_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(pjp_grammarParser.VAR, 0)
        def expression(self):
            return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class ConcatExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pjp_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatExpr" ):
                listener.enterConcatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatExpr" ):
                listener.exitConcatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatExpr" ):
                return visitor.visitConcatExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pjp_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqExpr" ):
                listener.enterEqExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqExpr" ):
                listener.exitEqExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqExpr" ):
                return visitor.visitEqExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class VarExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(pjp_grammarParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarExpr" ):
                listener.enterVarExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarExpr" ):
                listener.exitVarExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExpr" ):
                return visitor.visitVarExpr(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(pjp_grammarParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpr" ):
                listener.enterLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpr" ):
                listener.exitLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpr" ):
                return visitor.visitLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class TernaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pjp_grammarParser.ExpressionContext
            super().__init__(parser)
            self.split = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pjp_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pjp_grammarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernaryExpr" ):
                listener.enterTernaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernaryExpr" ):
                listener.exitTernaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernaryExpr" ):
                return visitor.visitTernaryExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pjp_grammarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = pjp_grammarParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 96
                self.match(pjp_grammarParser.T__7)
                self.state = 97
                self.expression(0)
                self.state = 98
                self.match(pjp_grammarParser.T__8)
                pass

            elif la_ == 2:
                localctx = pjp_grammarParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 100
                localctx.op = self.match(pjp_grammarParser.T__13)
                self.state = 101
                self.expression(14)
                pass

            elif la_ == 3:
                localctx = pjp_grammarParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                localctx.op = self.match(pjp_grammarParser.T__14)
                self.state = 103
                self.expression(13)
                pass

            elif la_ == 4:
                localctx = pjp_grammarParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 104
                self.match(pjp_grammarParser.VAR)
                pass

            elif la_ == 5:
                localctx = pjp_grammarParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 105
                self.literal()
                pass

            elif la_ == 6:
                localctx = pjp_grammarParser.AssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(pjp_grammarParser.VAR)
                self.state = 107
                self.match(pjp_grammarParser.T__28)
                self.state = 108
                self.expression(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 141
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = pjp_grammarParser.MulExprContext(self, pjp_grammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 111
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 112
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 113
                        self.expression(13)
                        pass

                    elif la_ == 2:
                        localctx = pjp_grammarParser.MuduloExprContext(self, pjp_grammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 114
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 115
                        localctx.op = self.match(pjp_grammarParser.T__17)
                        self.state = 116
                        self.expression(12)
                        pass

                    elif la_ == 3:
                        localctx = pjp_grammarParser.AddExprContext(self, pjp_grammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 117
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 118
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==19):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 119
                        self.expression(11)
                        pass

                    elif la_ == 4:
                        localctx = pjp_grammarParser.ConcatExprContext(self, pjp_grammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 120
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 121
                        localctx.op = self.match(pjp_grammarParser.T__19)
                        self.state = 122
                        self.expression(10)
                        pass

                    elif la_ == 5:
                        localctx = pjp_grammarParser.RelExprContext(self, pjp_grammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 123
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 124
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 125
                        self.expression(9)
                        pass

                    elif la_ == 6:
                        localctx = pjp_grammarParser.EqExprContext(self, pjp_grammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 126
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 127
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 128
                        self.expression(8)
                        pass

                    elif la_ == 7:
                        localctx = pjp_grammarParser.AndExprContext(self, pjp_grammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 129
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 130
                        localctx.op = self.match(pjp_grammarParser.T__24)
                        self.state = 131
                        self.expression(7)
                        pass

                    elif la_ == 8:
                        localctx = pjp_grammarParser.OrExprContext(self, pjp_grammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 132
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 133
                        localctx.op = self.match(pjp_grammarParser.T__25)
                        self.state = 134
                        self.expression(6)
                        pass

                    elif la_ == 9:
                        localctx = pjp_grammarParser.TernaryExprContext(self, pjp_grammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 135
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 136
                        self.match(pjp_grammarParser.T__26)
                        self.state = 137
                        self.expression(0)
                        self.state = 138
                        localctx.split = self.match(pjp_grammarParser.T__27)
                        self.state = 139
                        self.expression(3)
                        pass

             
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(pjp_grammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(pjp_grammarParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(pjp_grammarParser.BOOL, 0)

        def STRING(self):
            return self.getToken(pjp_grammarParser.STRING, 0)

        def getRuleIndex(self):
            return pjp_grammarParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = pjp_grammarParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




