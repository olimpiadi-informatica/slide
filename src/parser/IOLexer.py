# Generated from /Users/harniver/Git/olimpiadi/slide/grammar/IOLexer.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\37")
        buf.write("\u00c2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\7\32\u0097\n\32\f\32\16")
        buf.write("\32\u009a\13\32\3\32\3\32\3\33\3\33\3\33\3\33\7\33\u00a2")
        buf.write("\n\33\f\33\16\33\u00a5\13\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\7\34\u00ae\n\34\f\34\16\34\u00b1\13\34\3\34")
        buf.write("\3\34\3\35\3\35\7\35\u00b7\n\35\f\35\16\35\u00ba\13\35")
        buf.write("\3\36\3\36\7\36\u00be\n\36\f\36\16\36\u00c1\13\36\3\u00a3")
        buf.write("\2\37\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37\3\2\7\5\2\13\13\17")
        buf.write("\17\"\"\4\2\f\f\17\17\3\2$$\4\2C\\c|\6\2\62;C\\aac|\2")
        buf.write("\u00c6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\3=\3\2\2\2\5A\3\2")
        buf.write("\2\2\7F\3\2\2\2\tM\3\2\2\2\13R\3\2\2\2\rY\3\2\2\2\17[")
        buf.write("\3\2\2\2\21]\3\2\2\2\23_\3\2\2\2\25a\3\2\2\2\27c\3\2\2")
        buf.write("\2\31e\3\2\2\2\33g\3\2\2\2\35i\3\2\2\2\37k\3\2\2\2!m\3")
        buf.write("\2\2\2#o\3\2\2\2%q\3\2\2\2\'s\3\2\2\2)u\3\2\2\2+|\3\2")
        buf.write("\2\2-\u0081\3\2\2\2/\u0087\3\2\2\2\61\u008e\3\2\2\2\63")
        buf.write("\u0092\3\2\2\2\65\u009d\3\2\2\2\67\u00ab\3\2\2\29\u00b4")
        buf.write("\3\2\2\2;\u00bb\3\2\2\2=>\7k\2\2>?\7p\2\2?@\7v\2\2@\4")
        buf.write("\3\2\2\2AB\7n\2\2BC\7q\2\2CD\7p\2\2DE\7i\2\2E\6\3\2\2")
        buf.write("\2FG\7f\2\2GH\7q\2\2HI\7w\2\2IJ\7d\2\2JK\7n\2\2KL\7g\2")
        buf.write("\2L\b\3\2\2\2MN\7e\2\2NO\7j\2\2OP\7c\2\2PQ\7t\2\2Q\n\3")
        buf.write("\2\2\2RS\7u\2\2ST\7v\2\2TU\7t\2\2UV\7k\2\2VW\7p\2\2WX")
        buf.write("\7i\2\2X\f\3\2\2\2YZ\7-\2\2Z\16\3\2\2\2[\\\7/\2\2\\\20")
        buf.write("\3\2\2\2]^\7,\2\2^\22\3\2\2\2_`\7\61\2\2`\24\3\2\2\2a")
        buf.write("b\7*\2\2b\26\3\2\2\2cd\7+\2\2d\30\3\2\2\2ef\7]\2\2f\32")
        buf.write("\3\2\2\2gh\7_\2\2h\34\3\2\2\2ij\7}\2\2j\36\3\2\2\2kl\7")
        buf.write("\177\2\2l \3\2\2\2mn\7.\2\2n\"\3\2\2\2op\7<\2\2p$\3\2")
        buf.write("\2\2qr\7=\2\2r&\3\2\2\2st\7\f\2\2t(\3\2\2\2uv\7t\2\2v")
        buf.write("w\7g\2\2wx\7r\2\2xy\7g\2\2yz\7c\2\2z{\7v\2\2{*\3\2\2\2")
        buf.write("|}\7w\2\2}~\7r\2\2~\177\7v\2\2\177\u0080\7q\2\2\u0080")
        buf.write(",\3\2\2\2\u0081\u0082\7k\2\2\u0082\u0083\7p\2\2\u0083")
        buf.write("\u0084\7r\2\2\u0084\u0085\7w\2\2\u0085\u0086\7v\2\2\u0086")
        buf.write(".\3\2\2\2\u0087\u0088\7q\2\2\u0088\u0089\7w\2\2\u0089")
        buf.write("\u008a\7v\2\2\u008a\u008b\7r\2\2\u008b\u008c\7w\2\2\u008c")
        buf.write("\u008d\7v\2\2\u008d\60\3\2\2\2\u008e\u008f\t\2\2\2\u008f")
        buf.write("\u0090\3\2\2\2\u0090\u0091\b\31\2\2\u0091\62\3\2\2\2\u0092")
        buf.write("\u0093\7\61\2\2\u0093\u0094\7\61\2\2\u0094\u0098\3\2\2")
        buf.write("\2\u0095\u0097\n\3\2\2\u0096\u0095\3\2\2\2\u0097\u009a")
        buf.write("\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write("\u009b\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u009c\b\32\2")
        buf.write("\2\u009c\64\3\2\2\2\u009d\u009e\7\61\2\2\u009e\u009f\7")
        buf.write(",\2\2\u009f\u00a3\3\2\2\2\u00a0\u00a2\13\2\2\2\u00a1\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a6\u00a7\7,\2\2\u00a7\u00a8\7\61\2\2\u00a8\u00a9\3")
        buf.write("\2\2\2\u00a9\u00aa\b\33\2\2\u00aa\66\3\2\2\2\u00ab\u00af")
        buf.write("\7$\2\2\u00ac\u00ae\n\4\2\2\u00ad\u00ac\3\2\2\2\u00ae")
        buf.write("\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2")
        buf.write("\u00b0\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b3\7")
        buf.write("$\2\2\u00b38\3\2\2\2\u00b4\u00b8\4\63;\2\u00b5\u00b7\4")
        buf.write("\62;\2\u00b6\u00b5\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6")
        buf.write("\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9:\3\2\2\2\u00ba\u00b8")
        buf.write("\3\2\2\2\u00bb\u00bf\t\5\2\2\u00bc\u00be\t\6\2\2\u00bd")
        buf.write("\u00bc\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2")
        buf.write("\u00bf\u00c0\3\2\2\2\u00c0<\3\2\2\2\u00c1\u00bf\3\2\2")
        buf.write("\2\b\2\u0098\u00a3\u00af\u00b8\u00bf\3\b\2\2")
        return buf.getvalue()


class IOLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    LONG = 2
    DOUBLE = 3
    CHAR = 4
    STRING = 5
    PLUS = 6
    MINUS = 7
    MULT = 8
    DIV = 9
    LPAREN = 10
    RPAREN = 11
    LBRACK = 12
    RBRACK = 13
    LBRACE = 14
    RBRACE = 15
    COMMA = 16
    COLON = 17
    SEMICOL = 18
    NL = 19
    REPEAT = 20
    UPTO = 21
    INPUT = 22
    OUTPUT = 23
    WS = 24
    INLINE_COMMENT = 25
    BLOCK_COMMENT = 26
    STR = 27
    NUM = 28
    IDENT = 29

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'long'", "'double'", "'char'", "'string'", "'+'", 
            "'-'", "'*'", "'/'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "','", "':'", "';'", "'\n'", "'repeat'", "'upto'", "'input'", 
            "'output'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "LONG", "DOUBLE", "CHAR", "STRING", "PLUS", "MINUS", 
            "MULT", "DIV", "LPAREN", "RPAREN", "LBRACK", "RBRACK", "LBRACE", 
            "RBRACE", "COMMA", "COLON", "SEMICOL", "NL", "REPEAT", "UPTO", 
            "INPUT", "OUTPUT", "WS", "INLINE_COMMENT", "BLOCK_COMMENT", 
            "STR", "NUM", "IDENT" ]

    ruleNames = [ "INT", "LONG", "DOUBLE", "CHAR", "STRING", "PLUS", "MINUS", 
                  "MULT", "DIV", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
                  "LBRACE", "RBRACE", "COMMA", "COLON", "SEMICOL", "NL", 
                  "REPEAT", "UPTO", "INPUT", "OUTPUT", "WS", "INLINE_COMMENT", 
                  "BLOCK_COMMENT", "STR", "NUM", "IDENT" ]

    grammarFileName = "IOLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


