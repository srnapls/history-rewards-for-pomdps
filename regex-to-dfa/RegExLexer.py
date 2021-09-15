# Generated from RegEx.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    content = [3, 24715, 42794, 33075, 47597, 16764, 15335, 30598, 22884, 2, 10, 37, 8, 1, 4, 2, 9, 2, 4, 3, 9, 3, 4, 4, 9, 4, 4, 5, 9, 5, 4, 6, 9, 6, 4, 7, 9, 7, 4, 8, 9, 8, 4, 9, 9, 9, 3, 2, 3, 2, 3, 3, 3, 3, 3, 4, 3, 4, 3, 5, 3, 5, 3, 6, 3, 6, 3, 7, 3, 7, 3, 8, 3, 8, 3, 9, 3, 9, 3, 9, 3, 9, 2, 2, 10, 3, 3, 5, 4, 7, 5, 9, 6, 11, 7, 13, 8, 15, 9, 17, 10, 3, 2, 4, 5, 2, 50, 59, 67, 92, 99, 124, 5, 2, 11, 11, 15, 15, 34, 34, 2, 36, 2, 3, 3, 2, 2, 2, 2, 5, 3, 2, 2, 2, 2, 7, 3, 2, 2, 2, 2, 9, 3, 2, 2, 2, 2, 11, 3, 2, 2, 2, 2, 13, 3, 2, 2, 2, 2, 15, 3, 2, 2, 2, 2, 17, 3, 2, 2, 2, 3, 19, 3, 2, 2, 2, 5, 21, 3, 2, 2, 2, 7, 23, 3, 2, 2, 2, 9, 25, 3, 2, 2, 2, 11, 27, 3, 2, 2, 2, 13, 29, 3, 2, 2, 2, 15, 31, 3, 2, 2, 2, 17, 33, 3, 2, 2, 2, 19, 20, 7, 44, 2, 2, 20, 4, 3, 2, 2, 2, 21, 22, 7, 126, 2, 2, 22, 6, 3, 2, 2, 2, 23, 24, 7, 957, 2, 2, 24, 8, 3, 2, 2, 2, 25, 26, 7, 42, 2, 2, 26, 10, 3, 2, 2, 2, 27, 28, 7, 43, 2, 2, 28, 12, 3, 2, 2, 2, 29, 30, 7, 12, 2, 2, 30, 14, 3, 2, 2, 2, 31, 32, 9, 2, 2, 2, 32, 16, 3, 2, 2, 2, 33, 34, 9, 3, 2, 2, 34, 35, 3, 2, 2, 2, 35, 36, 8, 9, 2, 2, 36, 18, 3, 2, 2, 2, 3, 2, 3, 8, 2, 2]
    return [chr(x) for x in content]


class RegExLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())
    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    ID = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'|'", "'λ'", "'('", "')'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "ID", 
                  "WS" ]

    grammarFileName = "RegEx.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        #self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


