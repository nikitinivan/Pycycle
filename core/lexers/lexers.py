from PyQt5.Qsci import *

__all__ = ['get_lexer_by_ext', 'set_lexer_by_menu']

LEXERS = {
    ('AVS', QsciLexerAVS): (),
    ('Bash', QsciLexerBash): ('sh', 'ksh', 'bash', 'ebuild', 'eclass', 'exheres-0', 'exlib'),
    ('Batch', QsciLexerBatch): ('cmd', 'btm'),
    ('Cmake', QsciLexerCMake): ('cmake'),
    ('CoffeeScript', QsciLexerCoffeeScript): ('coffee'),
    ('C++', QsciLexerCPP): ('cpp', 'hpp', 'c++', 'h++', 'cc', 'hh', 'cxx', 'hxx', 'C', 'H', 'cp', 'CPP'),
    ('C#', QsciLexerCSharp): ('cs'),
    ('CSS', QsciLexerCSS): ('css'),
    ('D', QsciLexerD): ('d', 'di'),
    ('Diff', QsciLexerDiff): ('diff', 'patch'),
    ('Fortran', QsciLexerFortran): ('f03', 'f90', 'F03', 'F90'),
    ('Fortran77', QsciLexerFortran77): ('f', 'for'),
    ('HTML', QsciLexerHTML): ('html', 'htm', 'xhtml', 'xslt'),
    ('IDL', QsciLexerIDL): ('pro'),
    ('Java', QsciLexerJava): ('java'),
    ('JavaScript', QsciLexerJavaScript): ('js', 'jsm'),
    ('Lua', QsciLexerLua): ('lua', 'wlua'),
    ('Makefile', QsciLexerMakefile): ('mak', 'mk'),
    ('Matlab', QsciLexerMatlab): ('m'),
    ('Octave', QsciLexerOctave): ('m'),
    ('Pascal', QsciLexerPascal): (),
    ('Perl', QsciLexerPerl): ('pl', 'pm', 't'),
    ('PO', QsciLexerPO): ('pas', 'inc'),
    ('PostScript', QsciLexerPostScript): ('ps', 'eps'),
    ('POV', QsciLexerPOV): ('pov', 'inc'),
    ('Properties', QsciLexerProperties): ('properties'),
    ('Python', QsciLexerPython): ('py', 'pyw', 'sc', 'tac', 'sage'),
    ('Ruby', QsciLexerRuby): ('rb', 'rbw', 'rake', 'gemspec', 'rbx', 'duby'),
    ('Spice', QsciLexerSpice): ('cir'),
    ('SQL', QsciLexerSQL): ('sql'),
    ('TCL', QsciLexerTCL): ('tcl', 'rvt'),
    ('TeX', QsciLexerTeX): ('tex', 'aux', 'toc'),
    ('Verilog', QsciLexerVerilog): ('verilog', 'v'),
    ('VHDL', QsciLexerVHDL): ('vhdl', 'vhd'),
    ('XML', QsciLexerXML): ('xml', 'xsl', 'rss', 'xslt', 'xsd', 'wsdl', 'wsf'),
    ('YAML', QsciLexerYAML): ('yaml', 'yml'),
}


def get_lexer_by_ext(file):
    """Function return lexer according file extension"""
    file_name, file_ext = file.split('.')
    for key, value in LEXERS.items():
        if file_ext in value:
            lexer = key[1]
            return lexer


def set_lexer_by_menu(item):
    """Function return lexer according menu item"""
    for key, value in LEXERS.items():
        if item in key[0]:
            lexer = key[1]
            return lexer

def testing():
    """Function for testing"""
    print(get_lexer_by_ext('file.py'))
    print(set_lexer_by_menu('Python'))


if __name__ == '__main__':
    testing()

