# Generated from grammar/pjp_grammar.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,37,266,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,
        1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,
        1,23,1,23,1,23,1,24,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,27,1,27,
        1,28,1,28,1,29,4,29,167,8,29,11,29,12,29,168,1,30,4,30,172,8,30,
        11,30,12,30,173,1,30,1,30,5,30,178,8,30,10,30,12,30,181,9,30,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,192,8,31,1,32,1,32,
        1,32,5,32,197,8,32,10,32,12,32,200,9,32,1,32,1,32,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,
        1,33,1,33,3,33,222,8,33,1,34,1,34,1,34,5,34,227,8,34,10,34,12,34,
        230,9,34,1,35,1,35,1,35,1,35,5,35,236,8,35,10,35,12,35,239,9,35,
        1,35,1,35,1,36,4,36,244,8,36,11,36,12,36,245,1,36,1,36,1,37,1,37,
        1,37,3,37,253,8,37,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,40,
        1,40,1,41,1,41,0,0,42,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,
        10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,
        21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,
        32,65,33,67,34,69,35,71,36,73,37,75,0,77,0,79,0,81,0,83,0,1,0,7,
        2,0,34,34,92,92,2,0,10,10,13,13,3,0,9,10,13,13,32,32,8,0,34,34,47,
        47,92,92,98,98,102,102,110,110,114,114,116,116,3,0,48,57,65,70,97,
        102,2,0,65,90,97,122,1,0,48,57,274,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,
        0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,
        0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,
        0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,
        0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,
        0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,1,85,1,0,
        0,0,3,87,1,0,0,0,5,89,1,0,0,0,7,94,1,0,0,0,9,100,1,0,0,0,11,102,
        1,0,0,0,13,104,1,0,0,0,15,107,1,0,0,0,17,109,1,0,0,0,19,111,1,0,
        0,0,21,116,1,0,0,0,23,122,1,0,0,0,25,125,1,0,0,0,27,129,1,0,0,0,
        29,131,1,0,0,0,31,133,1,0,0,0,33,135,1,0,0,0,35,137,1,0,0,0,37,139,
        1,0,0,0,39,141,1,0,0,0,41,143,1,0,0,0,43,145,1,0,0,0,45,147,1,0,
        0,0,47,150,1,0,0,0,49,153,1,0,0,0,51,156,1,0,0,0,53,159,1,0,0,0,
        55,161,1,0,0,0,57,163,1,0,0,0,59,166,1,0,0,0,61,171,1,0,0,0,63,191,
        1,0,0,0,65,193,1,0,0,0,67,221,1,0,0,0,69,223,1,0,0,0,71,231,1,0,
        0,0,73,243,1,0,0,0,75,249,1,0,0,0,77,254,1,0,0,0,79,260,1,0,0,0,
        81,262,1,0,0,0,83,264,1,0,0,0,85,86,5,59,0,0,86,2,1,0,0,0,87,88,
        5,44,0,0,88,4,1,0,0,0,89,90,5,114,0,0,90,91,5,101,0,0,91,92,5,97,
        0,0,92,93,5,100,0,0,93,6,1,0,0,0,94,95,5,119,0,0,95,96,5,114,0,0,
        96,97,5,105,0,0,97,98,5,116,0,0,98,99,5,101,0,0,99,8,1,0,0,0,100,
        101,5,123,0,0,101,10,1,0,0,0,102,103,5,125,0,0,103,12,1,0,0,0,104,
        105,5,105,0,0,105,106,5,102,0,0,106,14,1,0,0,0,107,108,5,40,0,0,
        108,16,1,0,0,0,109,110,5,41,0,0,110,18,1,0,0,0,111,112,5,101,0,0,
        112,113,5,108,0,0,113,114,5,115,0,0,114,115,5,101,0,0,115,20,1,0,
        0,0,116,117,5,119,0,0,117,118,5,104,0,0,118,119,5,105,0,0,119,120,
        5,108,0,0,120,121,5,101,0,0,121,22,1,0,0,0,122,123,5,100,0,0,123,
        124,5,111,0,0,124,24,1,0,0,0,125,126,5,102,0,0,126,127,5,111,0,0,
        127,128,5,114,0,0,128,26,1,0,0,0,129,130,5,45,0,0,130,28,1,0,0,0,
        131,132,5,33,0,0,132,30,1,0,0,0,133,134,5,42,0,0,134,32,1,0,0,0,
        135,136,5,47,0,0,136,34,1,0,0,0,137,138,5,37,0,0,138,36,1,0,0,0,
        139,140,5,43,0,0,140,38,1,0,0,0,141,142,5,46,0,0,142,40,1,0,0,0,
        143,144,5,60,0,0,144,42,1,0,0,0,145,146,5,62,0,0,146,44,1,0,0,0,
        147,148,5,61,0,0,148,149,5,61,0,0,149,46,1,0,0,0,150,151,5,33,0,
        0,151,152,5,61,0,0,152,48,1,0,0,0,153,154,5,38,0,0,154,155,5,38,
        0,0,155,50,1,0,0,0,156,157,5,124,0,0,157,158,5,124,0,0,158,52,1,
        0,0,0,159,160,5,63,0,0,160,54,1,0,0,0,161,162,5,58,0,0,162,56,1,
        0,0,0,163,164,5,61,0,0,164,58,1,0,0,0,165,167,3,83,41,0,166,165,
        1,0,0,0,167,168,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,60,1,
        0,0,0,170,172,3,83,41,0,171,170,1,0,0,0,172,173,1,0,0,0,173,171,
        1,0,0,0,173,174,1,0,0,0,174,175,1,0,0,0,175,179,5,46,0,0,176,178,
        3,83,41,0,177,176,1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,
        1,0,0,0,180,62,1,0,0,0,181,179,1,0,0,0,182,183,5,116,0,0,183,184,
        5,114,0,0,184,185,5,117,0,0,185,192,5,101,0,0,186,187,5,102,0,0,
        187,188,5,97,0,0,188,189,5,108,0,0,189,190,5,115,0,0,190,192,5,101,
        0,0,191,182,1,0,0,0,191,186,1,0,0,0,192,64,1,0,0,0,193,198,5,34,
        0,0,194,197,3,75,37,0,195,197,8,0,0,0,196,194,1,0,0,0,196,195,1,
        0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,201,1,
        0,0,0,200,198,1,0,0,0,201,202,5,34,0,0,202,66,1,0,0,0,203,204,5,
        105,0,0,204,205,5,110,0,0,205,222,5,116,0,0,206,207,5,102,0,0,207,
        208,5,108,0,0,208,209,5,111,0,0,209,210,5,97,0,0,210,222,5,116,0,
        0,211,212,5,98,0,0,212,213,5,111,0,0,213,214,5,111,0,0,214,222,5,
        108,0,0,215,216,5,115,0,0,216,217,5,116,0,0,217,218,5,114,0,0,218,
        219,5,105,0,0,219,220,5,110,0,0,220,222,5,103,0,0,221,203,1,0,0,
        0,221,206,1,0,0,0,221,211,1,0,0,0,221,215,1,0,0,0,222,68,1,0,0,0,
        223,228,3,81,40,0,224,227,3,81,40,0,225,227,3,83,41,0,226,224,1,
        0,0,0,226,225,1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,228,229,1,
        0,0,0,229,70,1,0,0,0,230,228,1,0,0,0,231,232,5,47,0,0,232,233,5,
        47,0,0,233,237,1,0,0,0,234,236,8,1,0,0,235,234,1,0,0,0,236,239,1,
        0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,240,1,0,0,0,239,237,1,
        0,0,0,240,241,6,35,0,0,241,72,1,0,0,0,242,244,7,2,0,0,243,242,1,
        0,0,0,244,245,1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,247,1,
        0,0,0,247,248,6,36,0,0,248,74,1,0,0,0,249,252,5,92,0,0,250,253,7,
        3,0,0,251,253,3,77,38,0,252,250,1,0,0,0,252,251,1,0,0,0,253,76,1,
        0,0,0,254,255,5,117,0,0,255,256,3,79,39,0,256,257,3,79,39,0,257,
        258,3,79,39,0,258,259,3,79,39,0,259,78,1,0,0,0,260,261,7,4,0,0,261,
        80,1,0,0,0,262,263,7,5,0,0,263,82,1,0,0,0,264,265,7,6,0,0,265,84,
        1,0,0,0,13,0,168,173,179,191,196,198,221,226,228,237,245,252,1,6,
        0,0
    ]

class pjp_grammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    INT = 30
    FLOAT = 31
    BOOL = 32
    STRING = 33
    TYPE = 34
    VAR = 35
    COMMENT = 36
    SPACE = 37

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "'read'", "'write'", "'{'", "'}'", "'if'", "'('", 
            "')'", "'else'", "'while'", "'do'", "'for'", "'-'", "'!'", "'*'", 
            "'/'", "'%'", "'+'", "'.'", "'<'", "'>'", "'=='", "'!='", "'&&'", 
            "'||'", "'?'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "BOOL", "STRING", "TYPE", "VAR", "COMMENT", 
            "SPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "INT", "FLOAT", "BOOL", "STRING", 
                  "TYPE", "VAR", "COMMENT", "SPACE", "ESC", "UNICODE_ESC", 
                  "HEX", "LETTER", "DIGIT" ]

    grammarFileName = "pjp_grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


