from PyQt5.Qsci import *
from PyQt5.QtGui import QFont, QFontMetrics, QColor

FONT_FAMILY = "Menlo"
BACKGROUND_COLOR = '#2b2b2b'
FOREGROUND_COLOR = 'white'
MARGIN_BACKGROUND = "#2b2b2b" # "#313335"
MARGIN_FOREGROUND = "#676a6d"
FOLD_MARGIN_BACKGROUND = "#2b2b2b" # "#313335"
EDGE_COLOR = "#BBB8B5"
SEL_BACKGROUND = "#606060" # "#606060"
SEL_FOREGROUND = "#FFFFFF"
IND_BACKGROUND = "#676a6d"
IND_FOREGROUND = "#676a6d"
MARKER_BACKGROUND = "#2b2b2b" # "#313335"
MARKER_FOREGROUND = "#676a6d"


class Editor(QsciScintilla):
    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)
        self.bgcolor = '#2b2b2b'

        # FONT
        self.font = QFont()
        self.font.setFamily(FONT_FAMILY)
        self.font.setFixedPitch(True)
        self.font.setPointSize(13)
        self.setFont(self.font)
        self.setMarginsFont(self.font)

        # DEFAULT BACKGROUND AND FOREGROUND
        self.setPaper(QColor(BACKGROUND_COLOR))
        self.setColor(QColor(FOREGROUND_COLOR))

        # MARGIN LINE NUMBERS
        fontmetrics = QFontMetrics(self.font)
        self.setMarginsFont(self.font)
        self.setMarginWidth(0, fontmetrics.width("00000") + 4)
        self.setMarginLineNumbers(0, True)

        # MARGIN BACKGROUND AND FOREGROUND
        self.setMarginsBackgroundColor(QColor(MARGIN_BACKGROUND))
        self.setMarginsForegroundColor(QColor(MARGIN_FOREGROUND))

        # EDGE LINE
        # self.setEdgeMode(QsciScintilla.EdgeLine)
        # self.setEdgeColumn(150)
        # self.setEdgeColor(QColor(EDGE_COLOR))

        # BRACE MATCHING
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # CURRENT LINE
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#2D2D2D"))
        self.setCaretForegroundColor(QColor("white"))
        # SELECTION BACKGROUND AND FOREGROUND
        self.setSelectionBackgroundColor(QColor(SEL_BACKGROUND))
        self.setSelectionForegroundColor(QColor(SEL_FOREGROUND))

        # TABS
        self.setIndentationsUseTabs(False)
        self.setIndentationWidth(4)
        self.setTabIndents(True)
        self.setAutoIndent(True)
        self.setBackspaceUnindents(True)
        self.setTabWidth(4)
        # indentation guides
        self.setIndentationGuides(True)
        # TABS BACKGROUND AND FOREGROUND
        self.setIndentationGuidesBackgroundColor(QColor(IND_BACKGROUND))
        self.setIndentationGuidesForegroundColor(QColor(IND_FOREGROUND))

        # FOLDING MARGIN
        self.setFolding(QsciScintilla.PlainFoldStyle)
        self.setMarginWidth(2, 8) # (2,14)
        # FOLDING MARKERS
        self.markerDefine("-", QsciScintilla.SC_MARKNUM_FOLDEROPEN)
        self.markerDefine("+", QsciScintilla.SC_MARKNUM_FOLDER)
        self.markerDefine("-", QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        self.markerDefine("+", QsciScintilla.SC_MARKNUM_FOLDEREND)
        # FOLDING MARKERS BACKGROUND AND FOREGROUND
        self.setMarkerBackgroundColor(QColor(MARKER_BACKGROUND))
        self.setMarkerForegroundColor(QColor(MARGIN_FOREGROUND))
        self.setFoldMarginColors(QColor(FOLD_MARGIN_BACKGROUND), QColor(FOLD_MARGIN_BACKGROUND))

        # FOLDING LINE DISABLE
        self.SendScintilla(QsciScintilla.SCI_SETFOLDFLAGS, 0)

        # AUTO COMPLETION
        self.setAutoCompletionSource(QsciScintilla.AcsDocument)
        self.setAutoCompletionThreshold(2)

        # WHITESPACE
        self.setWhitespaceVisibility(QsciScintilla.WsVisible)
        self.setWhitespaceSize(1)

        # DISABLE HORIZONTAL SCROLLBAR
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)

        self.setStyleSheet("""
        QsciScintilla
        {
             border: 0px solid black;
             padding: 0px;
             border-radius: 0px;
             opacity: 100;
        }


        """)

    def setLexer(self, lexer=None):
        super(Editor, self).setLexer(lexer)

        lexer.setFont(QFont(FONT_FAMILY))

        # lexer.setColor(QColor(FOREGROUND_COLOR))
        lexer.setPaper(QColor(BACKGROUND_COLOR))

        #TODO: Remove this temporary solution for highlighting
        try:
            lexer.setColor(QColor("#5BA5F7"), lexer.ClassName)
        except:
            pass
        try:
            lexer.setColor(QColor("#FF0B66"), lexer.Keyword)
        except:
            pass
        try:
            lexer.setColor(QColor("#00FF40"), lexer.Comment)
        except:
            pass
        try:
            lexer.setColor(QColor("#BD4FE8"), lexer.Number)
        except:
            pass
        try:
            lexer.setColor(QColor("#F1E607"), lexer.DoubleQuotedString)
        except:
            pass
        try:
            lexer.setColor(QColor("#F1E607"), lexer.TripleSingleQuotedString)
        except:
            pass
        try:
            lexer.setColor(QColor("#F1E607"), lexer.TripleDoubleQuotedString)
        except:
            pass
        try:
            lexer.setColor(QColor("#F1E607"), lexer.DoubleQuotedString)
        except:
            pass
        try:
            lexer.setColor(QColor("#04F452"), lexer.FunctionMethodName)
        except:
            pass
        try:
            lexer.setColor(QColor("#FFFFFF"), lexer.Operator)
        except:
            pass
        try:
            lexer.setColor(QColor("#FFFFFF"), lexer.Identifier)
        except:
            pass
        try:
            lexer.setColor(QColor("#F1E607"), lexer.CommentBlock)
        except:
            pass
        try:
            lexer.setColor(QColor("#F1E607"), lexer.UnclosedString)
        except:
            pass
        try:
            lexer.setColor(QColor("#F1E607"), lexer.HighlightedIdentifier)
        except:
            pass
        try:
            lexer.setColor(QColor("#F1E607"), lexer.Decorator)
        except:
            pass

def main():
    """For standalone starting Editor in Python mode"""
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    editor = Editor()
    editor.resize(640, 580)
    editor.setCaretLineBackgroundColor(QColor("#2D2D2D"))
    editor.setCaretForegroundColor(QColor("white"))
    font = QFont()
    font.setFamily(FONT_FAMILY)
    font.setFixedPitch(True)
    font.setPointSize(13)
    lexer = QsciLexerPython()
    lexer.setDefaultFont(font)
    lexer.setColor(QColor("#ffffff"))

    editor.setLexer(lexer)

    # high light code
    lexer.setColor(QColor("#ffffff"))
    lexer.setPaper(QColor("#333333"))
    lexer.setColor(QColor("#5BA5F7"), QsciLexerPython.ClassName)
    lexer.setColor(QColor("#FF0B66"), QsciLexerPython.Keyword)
    lexer.setColor(QColor("#00FF40"), QsciLexerPython.Comment)
    lexer.setColor(QColor("#BD4FE8"), QsciLexerPython.Number)
    lexer.setColor(QColor("#F1E607"), QsciLexerPython.DoubleQuotedString)
    lexer.setColor(QColor("#F1E607"), QsciLexerPython.TripleSingleQuotedString)
    lexer.setColor(QColor("#F1E607"), QsciLexerPython.TripleDoubleQuotedString)
    lexer.setColor(QColor("#F1E607"), QsciLexerPython.DoubleQuotedString)
    lexer.setColor(QColor("#04F452"), QsciLexerPython.FunctionMethodName)
    lexer.setColor(QColor("#FFFFFF"), QsciLexerPython.Operator)
    lexer.setColor(QColor("#FFFFFF"), QsciLexerPython.Identifier)
    lexer.setColor(QColor("#F1E607"), QsciLexerPython.CommentBlock)
    lexer.setColor(QColor("#F1E607"), QsciLexerPython.UnclosedString)
    lexer.setColor(QColor("#F1E607"), QsciLexerPython.HighlightedIdentifier)
    lexer.setColor(QColor("#F1E607"), QsciLexerPython.Decorator)


    editor.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
