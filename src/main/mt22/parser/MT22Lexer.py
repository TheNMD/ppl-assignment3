# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *;
studentID = "2052932";
studentName = "Nguyen Manh Dan";



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u023e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\6\f\u0104\n\f\r\f\16\f\u0105\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\7\r\u010e\n\r\f\r\16\r\u0111\13\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\7\16\u011c\n\16\f\16\16\16")
        buf.write("\u011f\13\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3$\3$\7$\u01a0\n$\f$\16$\u01a3\13$\3%\3%\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3")
        buf.write("-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?")
        buf.write("\3?\7?\u01e3\n?\f?\16?\u01e6\13?\3?\3?\5?\u01ea\n?\3@")
        buf.write("\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\3@\3@\5@\u0203\n@\3A\3A\7A\u0207\nA\fA\16A\u020a")
        buf.write("\13A\3B\3B\5B\u020e\nB\3B\6B\u0211\nB\rB\16B\u0212\3C")
        buf.write("\3C\7C\u0217\nC\fC\16C\u021a\13C\3C\3C\3C\3D\3D\3D\5D")
        buf.write("\u0222\nD\3E\3E\7E\u0226\nE\fE\16E\u0229\13E\3E\3E\3E")
        buf.write("\3E\3E\3F\3F\7F\u0232\nF\fF\16F\u0235\13F\3F\5F\u0238")
        buf.write("\nF\3F\3F\3G\3G\3G\3\u010f\2H\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62")
        buf.write("c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081\2\u0083")
        buf.write("\2\u0085B\u0087\2\u0089C\u008bD\u008dE\3\2\r\5\2\n\f\16")
        buf.write("\17\"\"\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62")
        buf.write(";\3\2\63;\4\2\62;aa\4\2GGgg\4\2--//\n\2$$))^^ddhhpptt")
        buf.write("vv\6\2\f\f$$))^^\2\u024d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2")
        buf.write("\u008d\3\2\2\2\3\u008f\3\2\2\2\5\u009b\3\2\2\2\7\u00a5")
        buf.write("\3\2\2\2\t\u00b1\3\2\2\2\13\u00bc\3\2\2\2\r\u00cb\3\2")
        buf.write("\2\2\17\u00d8\3\2\2\2\21\u00e3\3\2\2\2\23\u00f0\3\2\2")
        buf.write("\2\25\u00fc\3\2\2\2\27\u0103\3\2\2\2\31\u0109\3\2\2\2")
        buf.write("\33\u0117\3\2\2\2\35\u0122\3\2\2\2\37\u0127\3\2\2\2!\u012c")
        buf.write("\3\2\2\2#\u0134\3\2\2\2%\u013a\3\2\2\2\'\u0142\3\2\2\2")
        buf.write(")\u0149\3\2\2\2+\u014f\3\2\2\2-\u0157\3\2\2\2/\u0160\3")
        buf.write("\2\2\2\61\u0165\3\2\2\2\63\u016b\3\2\2\2\65\u016f\3\2")
        buf.write("\2\2\67\u0175\3\2\2\29\u0178\3\2\2\2;\u017e\3\2\2\2=\u0187")
        buf.write("\3\2\2\2?\u018e\3\2\2\2A\u0191\3\2\2\2C\u0196\3\2\2\2")
        buf.write("E\u0199\3\2\2\2G\u019d\3\2\2\2I\u01a4\3\2\2\2K\u01a6\3")
        buf.write("\2\2\2M\u01a8\3\2\2\2O\u01aa\3\2\2\2Q\u01ac\3\2\2\2S\u01ae")
        buf.write("\3\2\2\2U\u01b0\3\2\2\2W\u01b3\3\2\2\2Y\u01b6\3\2\2\2")
        buf.write("[\u01b9\3\2\2\2]\u01bc\3\2\2\2_\u01be\3\2\2\2a\u01c1\3")
        buf.write("\2\2\2c\u01c3\3\2\2\2e\u01c6\3\2\2\2g\u01c9\3\2\2\2i\u01cb")
        buf.write("\3\2\2\2k\u01cd\3\2\2\2m\u01cf\3\2\2\2o\u01d1\3\2\2\2")
        buf.write("q\u01d3\3\2\2\2s\u01d5\3\2\2\2u\u01d7\3\2\2\2w\u01d9\3")
        buf.write("\2\2\2y\u01db\3\2\2\2{\u01dd\3\2\2\2}\u01e9\3\2\2\2\177")
        buf.write("\u0202\3\2\2\2\u0081\u0204\3\2\2\2\u0083\u020b\3\2\2\2")
        buf.write("\u0085\u0214\3\2\2\2\u0087\u0221\3\2\2\2\u0089\u0223\3")
        buf.write("\2\2\2\u008b\u022f\3\2\2\2\u008d\u023b\3\2\2\2\u008f\u0090")
        buf.write("\7t\2\2\u0090\u0091\7g\2\2\u0091\u0092\7c\2\2\u0092\u0093")
        buf.write("\7f\2\2\u0093\u0094\7K\2\2\u0094\u0095\7p\2\2\u0095\u0096")
        buf.write("\7v\2\2\u0096\u0097\7g\2\2\u0097\u0098\7i\2\2\u0098\u0099")
        buf.write("\7g\2\2\u0099\u009a\7t\2\2\u009a\4\3\2\2\2\u009b\u009c")
        buf.write("\7t\2\2\u009c\u009d\7g\2\2\u009d\u009e\7c\2\2\u009e\u009f")
        buf.write("\7f\2\2\u009f\u00a0\7H\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2")
        buf.write("\7q\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4\7v\2\2\u00a4\6")
        buf.write("\3\2\2\2\u00a5\u00a6\7t\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8")
        buf.write("\7c\2\2\u00a8\u00a9\7f\2\2\u00a9\u00aa\7D\2\2\u00aa\u00ab")
        buf.write("\7q\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae")
        buf.write("\7g\2\2\u00ae\u00af\7c\2\2\u00af\u00b0\7p\2\2\u00b0\b")
        buf.write("\3\2\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4")
        buf.write("\7c\2\2\u00b4\u00b5\7f\2\2\u00b5\u00b6\7U\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba")
        buf.write("\7p\2\2\u00ba\u00bb\7i\2\2\u00bb\n\3\2\2\2\u00bc\u00bd")
        buf.write("\7r\2\2\u00bd\u00be\7t\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0")
        buf.write("\7x\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3")
        buf.write("\7v\2\2\u00c3\u00c4\7F\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9")
        buf.write("\7n\2\2\u00c9\u00ca\7v\2\2\u00ca\f\3\2\2\2\u00cb\u00cc")
        buf.write("\7r\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf")
        buf.write("\7p\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7K\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5")
        buf.write("\7i\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7\7t\2\2\u00d7\16")
        buf.write("\3\2\2\2\u00d8\u00d9\7y\2\2\u00d9\u00da\7t\2\2\u00da\u00db")
        buf.write("\7k\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de")
        buf.write("\7H\2\2\u00de\u00df\7n\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1")
        buf.write("\7c\2\2\u00e1\u00e2\7v\2\2\u00e2\20\3\2\2\2\u00e3\u00e4")
        buf.write("\7r\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7")
        buf.write("\7p\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7D\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec\7n\2\2\u00ec\u00ed")
        buf.write("\7g\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7p\2\2\u00ef\22")
        buf.write("\3\2\2\2\u00f0\u00f1\7r\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3")
        buf.write("\7k\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6")
        buf.write("\7U\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9")
        buf.write("\7k\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb\7i\2\2\u00fb\24")
        buf.write("\3\2\2\2\u00fc\u00fd\7u\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff")
        buf.write("\7r\2\2\u00ff\u0100\7g\2\2\u0100\u0101\7t\2\2\u0101\26")
        buf.write("\3\2\2\2\u0102\u0104\t\2\2\2\u0103\u0102\3\2\2\2\u0104")
        buf.write("\u0105\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2")
        buf.write("\u0106\u0107\3\2\2\2\u0107\u0108\b\f\2\2\u0108\30\3\2")
        buf.write("\2\2\u0109\u010a\7\61\2\2\u010a\u010b\7,\2\2\u010b\u010f")
        buf.write("\3\2\2\2\u010c\u010e\13\2\2\2\u010d\u010c\3\2\2\2\u010e")
        buf.write("\u0111\3\2\2\2\u010f\u0110\3\2\2\2\u010f\u010d\3\2\2\2")
        buf.write("\u0110\u0112\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0113\7")
        buf.write(",\2\2\u0113\u0114\7\61\2\2\u0114\u0115\3\2\2\2\u0115\u0116")
        buf.write("\b\r\2\2\u0116\32\3\2\2\2\u0117\u0118\7\61\2\2\u0118\u0119")
        buf.write("\7\61\2\2\u0119\u011d\3\2\2\2\u011a\u011c\n\3\2\2\u011b")
        buf.write("\u011a\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2")
        buf.write("\u011d\u011e\3\2\2\2\u011e\u0120\3\2\2\2\u011f\u011d\3")
        buf.write("\2\2\2\u0120\u0121\b\16\2\2\u0121\34\3\2\2\2\u0122\u0123")
        buf.write("\7x\2\2\u0123\u0124\7q\2\2\u0124\u0125\7k\2\2\u0125\u0126")
        buf.write("\7f\2\2\u0126\36\3\2\2\2\u0127\u0128\7c\2\2\u0128\u0129")
        buf.write("\7w\2\2\u0129\u012a\7v\2\2\u012a\u012b\7q\2\2\u012b \3")
        buf.write("\2\2\2\u012c\u012d\7k\2\2\u012d\u012e\7p\2\2\u012e\u012f")
        buf.write("\7v\2\2\u012f\u0130\7g\2\2\u0130\u0131\7i\2\2\u0131\u0132")
        buf.write("\7g\2\2\u0132\u0133\7t\2\2\u0133\"\3\2\2\2\u0134\u0135")
        buf.write("\7h\2\2\u0135\u0136\7n\2\2\u0136\u0137\7q\2\2\u0137\u0138")
        buf.write("\7c\2\2\u0138\u0139\7v\2\2\u0139$\3\2\2\2\u013a\u013b")
        buf.write("\7d\2\2\u013b\u013c\7q\2\2\u013c\u013d\7q\2\2\u013d\u013e")
        buf.write("\7n\2\2\u013e\u013f\7g\2\2\u013f\u0140\7c\2\2\u0140\u0141")
        buf.write("\7p\2\2\u0141&\3\2\2\2\u0142\u0143\7u\2\2\u0143\u0144")
        buf.write("\7v\2\2\u0144\u0145\7t\2\2\u0145\u0146\7k\2\2\u0146\u0147")
        buf.write("\7p\2\2\u0147\u0148\7i\2\2\u0148(\3\2\2\2\u0149\u014a")
        buf.write("\7c\2\2\u014a\u014b\7t\2\2\u014b\u014c\7t\2\2\u014c\u014d")
        buf.write("\7c\2\2\u014d\u014e\7{\2\2\u014e*\3\2\2\2\u014f\u0150")
        buf.write("\7k\2\2\u0150\u0151\7p\2\2\u0151\u0152\7j\2\2\u0152\u0153")
        buf.write("\7g\2\2\u0153\u0154\7t\2\2\u0154\u0155\7k\2\2\u0155\u0156")
        buf.write("\7v\2\2\u0156,\3\2\2\2\u0157\u0158\7h\2\2\u0158\u0159")
        buf.write("\7w\2\2\u0159\u015a\7p\2\2\u015a\u015b\7e\2\2\u015b\u015c")
        buf.write("\7v\2\2\u015c\u015d\7k\2\2\u015d\u015e\7q\2\2\u015e\u015f")
        buf.write("\7p\2\2\u015f.\3\2\2\2\u0160\u0161\7v\2\2\u0161\u0162")
        buf.write("\7t\2\2\u0162\u0163\7w\2\2\u0163\u0164\7g\2\2\u0164\60")
        buf.write("\3\2\2\2\u0165\u0166\7h\2\2\u0166\u0167\7c\2\2\u0167\u0168")
        buf.write("\7n\2\2\u0168\u0169\7u\2\2\u0169\u016a\7g\2\2\u016a\62")
        buf.write("\3\2\2\2\u016b\u016c\7h\2\2\u016c\u016d\7q\2\2\u016d\u016e")
        buf.write("\7t\2\2\u016e\64\3\2\2\2\u016f\u0170\7y\2\2\u0170\u0171")
        buf.write("\7j\2\2\u0171\u0172\7k\2\2\u0172\u0173\7n\2\2\u0173\u0174")
        buf.write("\7g\2\2\u0174\66\3\2\2\2\u0175\u0176\7f\2\2\u0176\u0177")
        buf.write("\7q\2\2\u01778\3\2\2\2\u0178\u0179\7d\2\2\u0179\u017a")
        buf.write("\7t\2\2\u017a\u017b\7g\2\2\u017b\u017c\7c\2\2\u017c\u017d")
        buf.write("\7m\2\2\u017d:\3\2\2\2\u017e\u017f\7e\2\2\u017f\u0180")
        buf.write("\7q\2\2\u0180\u0181\7p\2\2\u0181\u0182\7v\2\2\u0182\u0183")
        buf.write("\7k\2\2\u0183\u0184\7p\2\2\u0184\u0185\7w\2\2\u0185\u0186")
        buf.write("\7g\2\2\u0186<\3\2\2\2\u0187\u0188\7t\2\2\u0188\u0189")
        buf.write("\7g\2\2\u0189\u018a\7v\2\2\u018a\u018b\7w\2\2\u018b\u018c")
        buf.write("\7t\2\2\u018c\u018d\7p\2\2\u018d>\3\2\2\2\u018e\u018f")
        buf.write("\7k\2\2\u018f\u0190\7h\2\2\u0190@\3\2\2\2\u0191\u0192")
        buf.write("\7g\2\2\u0192\u0193\7n\2\2\u0193\u0194\7u\2\2\u0194\u0195")
        buf.write("\7g\2\2\u0195B\3\2\2\2\u0196\u0197\7q\2\2\u0197\u0198")
        buf.write("\7h\2\2\u0198D\3\2\2\2\u0199\u019a\7q\2\2\u019a\u019b")
        buf.write("\7w\2\2\u019b\u019c\7v\2\2\u019cF\3\2\2\2\u019d\u01a1")
        buf.write("\t\4\2\2\u019e\u01a0\t\5\2\2\u019f\u019e\3\2\2\2\u01a0")
        buf.write("\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2H\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\7-\2\2")
        buf.write("\u01a5J\3\2\2\2\u01a6\u01a7\7/\2\2\u01a7L\3\2\2\2\u01a8")
        buf.write("\u01a9\7,\2\2\u01a9N\3\2\2\2\u01aa\u01ab\7\61\2\2\u01ab")
        buf.write("P\3\2\2\2\u01ac\u01ad\7\'\2\2\u01adR\3\2\2\2\u01ae\u01af")
        buf.write("\7#\2\2\u01afT\3\2\2\2\u01b0\u01b1\7(\2\2\u01b1\u01b2")
        buf.write("\7(\2\2\u01b2V\3\2\2\2\u01b3\u01b4\7~\2\2\u01b4\u01b5")
        buf.write("\7~\2\2\u01b5X\3\2\2\2\u01b6\u01b7\7?\2\2\u01b7\u01b8")
        buf.write("\7?\2\2\u01b8Z\3\2\2\2\u01b9\u01ba\7#\2\2\u01ba\u01bb")
        buf.write("\7?\2\2\u01bb\\\3\2\2\2\u01bc\u01bd\7@\2\2\u01bd^\3\2")
        buf.write("\2\2\u01be\u01bf\7@\2\2\u01bf\u01c0\7?\2\2\u01c0`\3\2")
        buf.write("\2\2\u01c1\u01c2\7>\2\2\u01c2b\3\2\2\2\u01c3\u01c4\7>")
        buf.write("\2\2\u01c4\u01c5\7?\2\2\u01c5d\3\2\2\2\u01c6\u01c7\7<")
        buf.write("\2\2\u01c7\u01c8\7<\2\2\u01c8f\3\2\2\2\u01c9\u01ca\7\60")
        buf.write("\2\2\u01cah\3\2\2\2\u01cb\u01cc\7.\2\2\u01ccj\3\2\2\2")
        buf.write("\u01cd\u01ce\7=\2\2\u01cel\3\2\2\2\u01cf\u01d0\7<\2\2")
        buf.write("\u01d0n\3\2\2\2\u01d1\u01d2\7*\2\2\u01d2p\3\2\2\2\u01d3")
        buf.write("\u01d4\7+\2\2\u01d4r\3\2\2\2\u01d5\u01d6\7]\2\2\u01d6")
        buf.write("t\3\2\2\2\u01d7\u01d8\7_\2\2\u01d8v\3\2\2\2\u01d9\u01da")
        buf.write("\7}\2\2\u01dax\3\2\2\2\u01db\u01dc\7\177\2\2\u01dcz\3")
        buf.write("\2\2\2\u01dd\u01de\7?\2\2\u01de|\3\2\2\2\u01df\u01ea\t")
        buf.write("\6\2\2\u01e0\u01e4\t\7\2\2\u01e1\u01e3\t\b\2\2\u01e2\u01e1")
        buf.write("\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4")
        buf.write("\u01e5\3\2\2\2\u01e5\u01e7\3\2\2\2\u01e6\u01e4\3\2\2\2")
        buf.write("\u01e7\u01e8\t\6\2\2\u01e8\u01ea\b?\3\2\u01e9\u01df\3")
        buf.write("\2\2\2\u01e9\u01e0\3\2\2\2\u01ea~\3\2\2\2\u01eb\u01ec")
        buf.write("\5}?\2\u01ec\u01ed\b@\4\2\u01ed\u0203\3\2\2\2\u01ee\u01ef")
        buf.write("\5}?\2\u01ef\u01f0\5\u0081A\2\u01f0\u01f1\b@\5\2\u01f1")
        buf.write("\u0203\3\2\2\2\u01f2\u01f3\5}?\2\u01f3\u01f4\5\u0083B")
        buf.write("\2\u01f4\u01f5\b@\6\2\u01f5\u0203\3\2\2\2\u01f6\u01f7")
        buf.write("\5}?\2\u01f7\u01f8\5\u0081A\2\u01f8\u01f9\5\u0083B\2\u01f9")
        buf.write("\u01fa\b@\7\2\u01fa\u0203\3\2\2\2\u01fb\u01fc\5\u0081")
        buf.write("A\2\u01fc\u01fd\b@\b\2\u01fd\u0203\3\2\2\2\u01fe\u01ff")
        buf.write("\5\u0081A\2\u01ff\u0200\5\u0083B\2\u0200\u0201\b@\t\2")
        buf.write("\u0201\u0203\3\2\2\2\u0202\u01eb\3\2\2\2\u0202\u01ee\3")
        buf.write("\2\2\2\u0202\u01f2\3\2\2\2\u0202\u01f6\3\2\2\2\u0202\u01fb")
        buf.write("\3\2\2\2\u0202\u01fe\3\2\2\2\u0203\u0080\3\2\2\2\u0204")
        buf.write("\u0208\5g\64\2\u0205\u0207\t\6\2\2\u0206\u0205\3\2\2\2")
        buf.write("\u0207\u020a\3\2\2\2\u0208\u0206\3\2\2\2\u0208\u0209\3")
        buf.write("\2\2\2\u0209\u0082\3\2\2\2\u020a\u0208\3\2\2\2\u020b\u020d")
        buf.write("\t\t\2\2\u020c\u020e\t\n\2\2\u020d\u020c\3\2\2\2\u020d")
        buf.write("\u020e\3\2\2\2\u020e\u0210\3\2\2\2\u020f\u0211\t\6\2\2")
        buf.write("\u0210\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0210\3")
        buf.write("\2\2\2\u0212\u0213\3\2\2\2\u0213\u0084\3\2\2\2\u0214\u0218")
        buf.write("\7$\2\2\u0215\u0217\5\u0087D\2\u0216\u0215\3\2\2\2\u0217")
        buf.write("\u021a\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2")
        buf.write("\u0219\u021b\3\2\2\2\u021a\u0218\3\2\2\2\u021b\u021c\7")
        buf.write("$\2\2\u021c\u021d\bC\n\2\u021d\u0086\3\2\2\2\u021e\u021f")
        buf.write("\7^\2\2\u021f\u0222\t\13\2\2\u0220\u0222\n\f\2\2\u0221")
        buf.write("\u021e\3\2\2\2\u0221\u0220\3\2\2\2\u0222\u0088\3\2\2\2")
        buf.write("\u0223\u0227\7$\2\2\u0224\u0226\5\u0087D\2\u0225\u0224")
        buf.write("\3\2\2\2\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227")
        buf.write("\u0228\3\2\2\2\u0228\u022a\3\2\2\2\u0229\u0227\3\2\2\2")
        buf.write("\u022a\u022b\7^\2\2\u022b\u022c\n\13\2\2\u022c\u022d\3")
        buf.write("\2\2\2\u022d\u022e\bE\13\2\u022e\u008a\3\2\2\2\u022f\u0233")
        buf.write("\7$\2\2\u0230\u0232\5\u0087D\2\u0231\u0230\3\2\2\2\u0232")
        buf.write("\u0235\3\2\2\2\u0233\u0231\3\2\2\2\u0233\u0234\3\2\2\2")
        buf.write("\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2\u0236\u0238\7")
        buf.write("\2\2\3\u0237\u0236\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u0239")
        buf.write("\3\2\2\2\u0239\u023a\bF\f\2\u023a\u008c\3\2\2\2\u023b")
        buf.write("\u023c\13\2\2\2\u023c\u023d\bG\r\2\u023d\u008e\3\2\2\2")
        buf.write("\22\2\u0105\u010f\u011d\u01a1\u01e4\u01e9\u0202\u0208")
        buf.write("\u020d\u0212\u0218\u0221\u0227\u0233\u0237\16\b\2\2\3")
        buf.write("?\2\3@\3\3@\4\3@\5\3@\6\3@\7\3@\b\3C\t\3E\n\3F\13\3G\f")
        return buf.getvalue()


class MT22Lexer(Lexer):

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
    WS = 11
    CCOMMENT = 12
    CPPCOMMENT = 13
    KWVOID = 14
    KWAUTO = 15
    KWINT = 16
    KWFLOAT = 17
    KWBOO = 18
    KWSTR = 19
    KWARR = 20
    KWINHERIT = 21
    KWFUNC = 22
    KWTRUE = 23
    KWFALSE = 24
    KWFOR = 25
    KWWHILE = 26
    KWDO = 27
    KWBRK = 28
    KWCONT = 29
    KWRTN = 30
    KWIF = 31
    KWELSE = 32
    KWOF = 33
    KWOUT = 34
    ID = 35
    ADDOP = 36
    SUBOP = 37
    MULOP = 38
    DIVOP = 39
    MODOP = 40
    EXCOP = 41
    ANDOP = 42
    OROP = 43
    EQLOP = 44
    DIFOP = 45
    LARGEOP = 46
    LEQLOP = 47
    SMALLOP = 48
    SEQLOP = 49
    CONCATOP = 50
    DOT = 51
    CM = 52
    SM = 53
    CL = 54
    LB = 55
    RB = 56
    LSB = 57
    RSB = 58
    LCB = 59
    RCB = 60
    EQL = 61
    LITINT = 62
    LITFLOAT = 63
    LITSTR = 64
    ILLEGAL_ESCAPE = 65
    UNCLOSED_STRING = 66
    ERROR_CHAR = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'readFloat'", "'readBoolean'", "'readString'", 
            "'preventDefault'", "'printInteger'", "'writeFloat'", "'printBoolean'", 
            "'printString'", "'super'", "'void'", "'auto'", "'integer'", 
            "'float'", "'boolean'", "'string'", "'array'", "'inherit'", 
            "'function'", "'true'", "'false'", "'for'", "'while'", "'do'", 
            "'break'", "'continue'", "'return'", "'if'", "'else'", "'of'", 
            "'out'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'::'", "'.'", 
            "','", "';'", "':'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "WS", "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", "KWINT", 
            "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", "KWFUNC", 
            "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", "KWBRK", "KWCONT", 
            "KWRTN", "KWIF", "KWELSE", "KWOF", "KWOUT", "ID", "ADDOP", "SUBOP", 
            "MULOP", "DIVOP", "MODOP", "EXCOP", "ANDOP", "OROP", "EQLOP", 
            "DIFOP", "LARGEOP", "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", 
            "DOT", "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
            "EQL", "LITINT", "LITFLOAT", "LITSTR", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "WS", "CCOMMENT", "CPPCOMMENT", 
                  "KWVOID", "KWAUTO", "KWINT", "KWFLOAT", "KWBOO", "KWSTR", 
                  "KWARR", "KWINHERIT", "KWFUNC", "KWTRUE", "KWFALSE", "KWFOR", 
                  "KWWHILE", "KWDO", "KWBRK", "KWCONT", "KWRTN", "KWIF", 
                  "KWELSE", "KWOF", "KWOUT", "ID", "ADDOP", "SUBOP", "MULOP", 
                  "DIVOP", "MODOP", "EXCOP", "ANDOP", "OROP", "EQLOP", "DIFOP", 
                  "LARGEOP", "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", 
                  "DOT", "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", 
                  "RCB", "EQL", "LITINT", "LITFLOAT", "Decimal", "Exponent", 
                  "LITSTR", "Char", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[61] = self.LITINT_action 
            actions[62] = self.LITFLOAT_action 
            actions[65] = self.LITSTR_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[68] = self.UNCLOSED_STRING_action 
            actions[69] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def LITINT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def LITFLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

        if actionIndex == 2:
            self.text = self.text.replace('_','')
     

        if actionIndex == 3:
            self.text = self.text.replace('_','')
     

        if actionIndex == 4:
            self.text = self.text.replace('_','')
     

        if actionIndex == 5:
            self.text = self.text.replace('_','')
     

        if actionIndex == 6:
            self.text = self.text.replace('_','')
     

    def LITSTR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     

    def UNCLOSED_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:
            self.text = self.text[1:]; raise UncloseString(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 10:
            raise ErrorToken(self.text)
     


