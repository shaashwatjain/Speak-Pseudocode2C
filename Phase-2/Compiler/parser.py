import sys
import lexer
from ply import yacc
from typing import Tuple
from colorama import Fore, Style
from lexer import tokens, lex, find_column

file = open("output.c", "w")
indent = 0


def p_Start(p):
    """
    Start : KW_START
    """
    file.write("#include<stdio.h>\n#include<stdlib.h>\n")
    file.write("int main(int argc, char** argv)\n{")

#  def p_Label(p):
#      """Label : IDENTIFIER"""
#      pass


def p_Print(p):
    """
    Print : KW_PRINT
    """
    file.write("\n\tprintf\n")


def p_End(p):
    """
    End : KW_END
    """
    file.write("return 0;\n}")


def p_empty(p):
    "empty :"
    pass


def p_error(p: lex.LexToken):
    print(f"{Fore.RED}SYNTAX ERROR:{Style.RESET_ALL}")
    if p is not None:
        col = find_column(p)
        print(f"at line {p.lineno}, column {col}")
        # print(" " * 10, " \t", " " * (col - 1), "^", sep="")
    else:
        print("Unexpected end of file")


parser = yacc.yacc(debug=True)

if __name__ == "__main__":
    with open(sys.argv[1], "rt") as f:
        input_code = f.read()
        if input_code[len(input_code) - 1] != "\n":
            input_code += "\n"

        lexer.input_code = input_code
        lines = input_code.split("\n")
        result = parser.parse(input_code, tracking=True, debug=False)
        # print(result)
        print("Finished Parsing!")
