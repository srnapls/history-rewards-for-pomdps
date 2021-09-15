# Generated from RegEx.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    content = [3, 24715, 42794, 33075, 47597, 16764, 15335, 30598, 22884, 3, 10, 40, 4, 2, 9, 2, 4, 3, 9, 3, 4, 4, 9, 4, 3, 2, 3, 2, 3, 2, 7, 2, 12, 10, 2, 12, 2, 14, 2, 15, 11, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3, 24, 10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 3, 33, 10, 3, 12, 3, 14, 3, 36, 11, 3, 3, 4, 3, 4, 3, 4, 2, 3, 4, 5, 2, 4, 6, 2, 2, 2, 42, 2, 13, 3, 2, 2, 2, 4, 23, 3, 2, 2, 2, 6, 37, 3, 2, 2, 2, 8, 9, 5, 4, 3, 2, 9, 10, 5, 6, 4, 2, 10, 12, 3, 2, 2, 2, 11, 8, 3, 2, 2, 2, 12, 15, 3, 2, 2, 2, 13, 11, 3, 2, 2, 2, 13, 14, 3, 2, 2, 2, 14, 3, 3, 2, 2, 2, 15, 13, 3, 2, 2, 2, 16, 17, 8, 3, 1, 2, 17, 24, 7, 9, 2, 2, 18, 24, 7, 5, 2, 2, 19, 20, 7, 6, 2, 2, 20, 21, 5, 4, 3, 2, 21, 22, 7, 7, 2, 2, 22, 24, 3, 2, 2, 2, 23, 16, 3, 2, 2, 2, 23, 18, 3, 2, 2, 2, 23, 19, 3, 2, 2, 2, 24, 34, 3, 2, 2, 2, 25, 26, 12, 7, 2, 2, 26, 33, 5, 4, 3, 8, 27, 28, 12, 6, 2, 2, 28, 29, 7, 4, 2, 2, 29, 33, 5, 4, 3, 7, 30, 31, 12, 8, 2, 2, 31, 33, 7, 3, 2, 2, 32, 25, 3, 2, 2, 2, 32, 27, 3, 2, 2, 2, 32, 30, 3, 2, 2, 2, 33, 36, 3, 2, 2, 2, 34, 32, 3, 2, 2, 2, 34, 35, 3, 2, 2, 2, 35, 5, 3, 2, 2, 2, 36, 34, 3, 2, 2, 2, 37, 38, 7, 8, 2, 2, 38, 7, 3, 2, 2, 2, 6, 13, 23, 32, 34]
    return [chr(x) for x in content]


class RegExParser ( Parser ):

    grammarFileName = "RegEx.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'|'", "'λ'", "'('", "')'", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "WS" ]

    RULE_prog = 0
    RULE_regex = 1
    RULE_newline = 2

    ruleNames =  [ "prog", "regex", "newline" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ID=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        #self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def regex(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegExParser.RegexContext)
            else:
                return self.getTypedRuleContext(RegExParser.RegexContext,i)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegExParser.NewlineContext)
            else:
                return self.getTypedRuleContext(RegExParser.NewlineContext,i)


        def getRuleIndex(self):
            return RegExParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)

    def prog(self):

        localctx = RegExParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RegExParser.T__2) | (1 << RegExParser.T__3) | (1 << RegExParser.ID))) != 0):
                self.state = 6
                self.regex(0)
                self.state = 7
                self.newline()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegExParser.RULE_regex

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class EpsilonContext(RegexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExParser.RegexContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEpsilon" ):
                return visitor.visitEpsilon(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierContext(RegexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExParser.RegexContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(RegExParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class ConcatenationContext(RegexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExParser.RegexContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def regex(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegExParser.RegexContext)
            else:
                return self.getTypedRuleContext(RegExParser.RegexContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatenation" ):
                return visitor.visitConcatenation(self)
            else:
                return visitor.visitChildren(self)


    class AlternationContext(RegexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExParser.RegexContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def regex(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegExParser.RegexContext)
            else:
                return self.getTypedRuleContext(RegExParser.RegexContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternation" ):
                return visitor.visitAlternation(self)
            else:
                return visitor.visitChildren(self)


    class KlneeContext(RegexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExParser.RegexContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def regex(self):
            return self.getTypedRuleContext(RegExParser.RegexContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKlnee" ):
                return visitor.visitKlnee(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(RegexContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExParser.RegexContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def regex(self):
            return self.getTypedRuleContext(RegExParser.RegexContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)



    def regex(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegExParser.RegexContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_regex, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegExParser.ID]:
                localctx = RegExParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 15
                self.match(RegExParser.ID)
                pass
            elif token in [RegExParser.T__2]:
                localctx = RegExParser.EpsilonContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                self.match(RegExParser.T__2)
                pass
            elif token in [RegExParser.T__3]:
                localctx = RegExParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(RegExParser.T__3)
                self.state = 18
                self.regex(0)
                self.state = 19
                self.match(RegExParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 30
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = RegExParser.ConcatenationContext(self, RegExParser.RegexContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_regex)
                        self.state = 23
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 24
                        self.regex(6)
                        pass

                    elif la_ == 2:
                        localctx = RegExParser.AlternationContext(self, RegExParser.RegexContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_regex)
                        self.state = 25
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 26
                        self.match(RegExParser.T__1)
                        self.state = 27
                        self.regex(5)
                        pass

                    elif la_ == 3:
                        localctx = RegExParser.KlneeContext(self, RegExParser.RegexContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_regex)
                        self.state = 28
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 29
                        self.match(RegExParser.T__0)
                        pass

             
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class NewlineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegExParser.RULE_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline" ):
                return visitor.visitNewline(self)
            else:
                return visitor.visitChildren(self)

    def newline(self):

        localctx = RegExParser.NewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(RegExParser.T__5)
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
        self._predicates[1] = self.regex_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def regex_sempred(self, localctx:RegexContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)