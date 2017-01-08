from PyQt5.QtWidgets import QMainWindow, QAction, QTabWidget, \
    QApplication, QFileDialog, QActionGroup, QMessageBox, QTabBar
from PyQt5.Qsci import *
from core.editor import Editor
import sys

from core.lexers import lexers


class Tab(QTabWidget):
    """Subclass for setting some additional stuff like tabs counting.
    Counting is convenient method for implementing tabCloseRequested connection"""
    count = 0

    def __init__(self):
        super(Tab, self).__init__()
        self.setTabsClosable(True)
        self.setMovable(True)
        self.tabCloseRequested.connect(self.removeTab)
        self.setDocumentMode(True) 
        self.setUsesScrollButtons(True)

        self.addTab(Editor(), 'Untitled')

    def addTab(self, QWidget, *__args):
        """Adding tab to TabWidget and increment tab count"""
        Tab.count += 1
        super(Tab, self).addTab(QWidget, *__args)

    def removeTab(self, p_int):
        """Removing tab from TabWidget and decrement tab count"""
        if Tab.count > 1:
            Tab.count -= 1
            super(Tab, self).removeTab(p_int)
        else:
            sys.exit()

    @classmethod
    def count_of_tabs(cls):
        """Return count of tabs in tab widget"""
        return cls.count


class Main(QMainWindow):
    """Class Main, contains following functions:
    UI Initialization, Menu Initialization"""

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.editor = Editor()
        self.tab = Tab()
        self.tab.setStyleSheet("""
        QTabWidget::pane {background: #272727;}
        QTabWidget::tab-bar:top {top: 1px;}
        QTabWidget::tab-bar:bottom {bottom: 1px;}
        QTabWidget::tab-bar:left {right: 1px;}
        QTabWidget::tab-bar:right {left: 1px;}
        QTabBar{background-color: #1b1b1b; qproperty-drawBase:0;  }

        QTabBar::tab {border: 1px #1b1b1b;}
        QTabBar::tab:selected {background: #2b2b2b;color: #bbbbbb;}
        QTabBar::tab:!selected {background: #3c3e3f;color: #bbbbbb;}
        QTabBar::tab:bottom:!selected {margin-bottom: 3px;}
        QTabBar::tab:top, QTabBar::tab:bottom {
            min-width: 8ex;
            margin-right: -1px;
            padding: 5px 10px 5px 10px;}
        """)

        self.set_window_ui()
        self.set_menu()
        self.setCentralWidget(self.tab)
        self.setUnifiedTitleAndToolBarOnMac(True)


    def set_window_ui(self):
        """UI Initialization"""
        self.setWindowTitle("Pycycle")
        self.resize(720, 580)

    def set_menu(self):
        """Menu Initialization"""
        menu = self.menuBar()

        # FILE MENU
        file_menu = menu.addMenu('&File')
        file_menu.addAction(QAction('&New File', self, shortcut='Ctrl+N', triggered=self._new_file))
        file_menu.addAction(QAction('&Open FIle', self, shortcut= 'Ctrl+O', triggered=self._open_file))
        file_menu.addAction(QAction('&Save', self, shortcut='Ctrl+S', triggered=self._save_file))
        file_menu.addAction(QAction('&Save As', self, shortcut='Ctrl+Shift+S', triggered=self._save_file_as))


        # EDIT MENU
        edit_menu = menu.addMenu('&Edit')
        edit_menu.addAction(QAction('&Undo', self, shortcut='Ctrl+Z', triggered=self._undo_edit))
        edit_menu.addAction(QAction('&Redo', self, shortcut='Ctrl+Y', triggered=self._redo_edit))
        edit_menu.addSeparator()
        edit_menu.addAction(QAction('&Copy', self, shortcut='Ctrl+C', triggered=self._copy_edit))
        edit_menu.addAction(QAction('&Cut', self, shortcut='Ctrl+X', triggered=self._cut_edit))
        edit_menu.addAction(QAction('&Paste', self, shortcut='Ctrl+V', triggered=self._paste_edit))

        # VIEW MENU
        view_menu = menu.addMenu('&View')
        # CHOOSING LANGUAGES
        languages = view_menu.addMenu('&Languages')
        group_of_lexers = QActionGroup(languages)
        group_of_lexers.setExclusive(True)
        list_of_lexers = sorted(lexers.LEXERS.keys())
        for element in list_of_lexers:
            action = languages.addAction(element[0])
            action.setCheckable(True)
            action.setActionGroup(group_of_lexers)
            action.setData(element[0])
        group_of_lexers.triggered.connect(self._set_lexer)

        # HELP MENU
        help_menu = menu.addMenu('&Help')
        help_menu.addAction(QAction('&Info', self, triggered=self._about))

    def _new_file(self):
        """Creating new file in new tab"""
        self.tab.addTab(Editor(), "Untitled")
        self.tab.setCurrentIndex(self.tab.currentIndex() + 1)

    def _open_file(self):
        """Open file and set it in a new tab or in current if tab is empty"""
        file = QFileDialog.getOpenFileName(self, 'Open file', ".")[0]
        if file:
            file_name = str(file).split('/')[-1] # Need to create version for Windows
            with open(file, 'rt') as text:
                if self.tab.currentWidget().text():  # If current Tab is not empty
                    self.tab.addTab(Editor(), file_name)
                    self.tab.setCurrentIndex(self.tab.currentIndex() + 1)
                    self.tab.currentWidget().setText(text.read())
                else:
                    self.tab.currentWidget().setText(text.read())
                    self.tab.setTabText(self.tab.currentIndex(), file_name)
                try:
                    lexer = lexers.get_lexer_by_ext(file_name)
                    self.tab.currentWidget().setLexer(lexer())
                except:
                    pass


    def _set_lexer(self, action):
        """Setting lexer to editor in current tab"""
        widget = self.tab.currentWidget()
        lexer = lexers.set_lexer_by_menu(action.data())
        widget.setLexer(lexer())


    def _save_file(self):
        """Saving changes if file exist, otherwise calling 'Save as' function"""
        try:
            file_name = self.tab.tabText(self.tab.currentIndex())
            print(file_name)
            with open(file_name, 'r+') as w_file:
                text = self.tab.currentWidget().text()
                w_file.write(text)
        except:
            self._save_file_as()

    def _save_file_as(self):
        """Saving file as..."""
        text = self.tab.currentWidget().text()
        file, _ = QFileDialog.getSaveFileName(self, 'Save file as')
        if file:
            file_name = str(file).split('/')[-1]
            with open(file, 'w') as w_file:
                w_file.write(text)
                try:
                    lexer = lexers.get_lexer_by_ext(file_name)
                    self.tab.currentWidget().setLexer(lexer())
                except:
                    pass
                finally:
                    self.tab.currentWidget().setText(text)
                    self.tab.setTabText(self.tab.currentIndex(), file_name)

    def _undo_edit(self):
        """Access to builtin Qscintilla function undo"""
        return self.tab.currentWidget().undo()

    def _redo_edit(self):
        """Access to builtin Qscintilla function redo"""
        return self.tab.currentWidget().redo()

    def _copy_edit(self):
        """Access to builtin Qscintilla function copy"""
        return self.tab.currentWidget().copy()

    def _cut_edit(self):
        """Access to builtin Qscintilla function cut"""
        return self.tab.currentWidget().cut()

    def _paste_edit(self):
        """Access to builtin Qscintilla function paste"""
        return self.tab.currentWidget().paste()

    def _about(self):
        QMessageBox.about(self, 'About', 'Hello')

def main():
    app = QApplication(sys.argv)
    window = Main()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
