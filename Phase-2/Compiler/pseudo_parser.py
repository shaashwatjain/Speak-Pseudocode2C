import sys
import pseudo_lexer
import pseudo_ast
from ply import yacc
from typing import Tuple
from colorama import Fore, Style
from pseudo_lexer import tokens, lex, find_column


class Pseudo_Parser:
    precedence = (
        ("left", "PLUS", "MINUS"),
        ("left", "TIMES", "DIVIDE", "PERCENT"),
        #  ("right", "UMINUS"),
    )

    def __init__(self):
        self.ast = []
        self.variable_types = {}
        self.var_lengths = {}
        self.scope = ""
        self.tokens = tokens
        self.L = []

        self.Parser = yacc.yacc(debug=True, module=self)

    def parse(self, input_code):
        self.Parser.parse(input=input_code, tracking=True, debug=False)
        return self.ast

    #  def p_Statement(self, p):
    #      """Statement : Stmt_List"""
    #
    #      self.ast.append(p[1])
    #
    #  def p_Stmt_List(self, p):
    #      """Stmt_List : Simple_Stmt
    #      | Stmt_List NEWLINE Simple_Stmt"""
    #
    #      if len(p) == 2:
    #          p[0] = [p[1]]
    #
    #      elif len(p) > 3:
    #          p[0] = p[1] + [p[3]]
    #
    #  def p_Start_Stmt(self, p):
    #      """
    #      Start_Stmt : KW_START Stmt_List
    #      """
    #      print("hello")
    #      self.L.append("#include<stdio.h>\n#include<stdlib.h>\n")
    #      self.L.append("int main(int argc, char** argv)\n{")
    #      for i in reversed(self.L):
    #          file.write(i)
    #
    #  def p_If_Stmt(self, p):
    #      """If_Stmt : KW_IF expression KW_THEN NEWLINE Stmt_List NEWLINE KW_ENDIF
    #      | KW_IF expression KW_THEN NEWLINE Stmt_List NEWLINE KW_ELSE NEWLINE Stmt_List NEWLINE KW_ENDIF
    #      | KW_IF expression KW_THEN NEWLINE Stmt_List NEWLINE KW_ELSE If_Stmt"""
    #
    #      if len(p) == 8:
    #          p[0] = pseudo_ast.If(p[2], p[5], None)
    #
    #      elif len(p) == 9:
    #          p[0] = pseudo_ast.If(p[2], p[5], [p[8]])
    #
    #      elif len(p) == 12:
    #          p[0] = pseudo_ast.If(p[2], p[5], p[9])
    #
    #  def p_While_Stmt(self, p):
    #      """While_Stmt : KW_WHILE expression KW_DO NEWLINE Stmt_List NEWLINE KW_ENDWHILE"""
    #
    #      p[0] = pseudo_ast.While(p[2], p[5])
    #
    #  def p_Simple_Stmt(self, p):
    #      """Simple_Stmt : expression
    #      | Expr_List
    #      | Start_Stmt
    #      | Assignment_Stmt
    #      | If_Stmt
    #      | While_Stmt
    #      | For_Stmt
    #      | Output_Stmt
    #      | Input_Stmt"""
    #
    #      p[0] = p[1]

    def p_Start_Stmt(self, p):
        """
        Start_Stmt : KW_START Program
        """
        self.L.append("int main(int argc, char** argv)\n{")
        self.L.append("#include<stdio.h>\n#include<stdlib.h>\n")
        for i in reversed(self.L):
            file.write(i)

    def p_Program(self, p):
        """
        Program : IDENTIFIER Program
        | NEWLINE Program
        | Print
        | Initialization
        """
        pass

    def p_Initialization(self, p):
        """
        Initialization : KW_INIT IDENTIFIER KW_TO Number
        """
        self.L.append("{} = ;\n".format(p[2][1]))

    def p_Number(self, p):
        """
        Number : INT_LIT NEWLINE End
        """
        self.L.append("{} ".format(p[1][0]))

    def p_IfStmt(self, p):
        """
        IfStmt : empty
        """

    def p_Print(self, p):
        """
        Print : KW_PRINT STRING_LIT NEWLINE End
        | End
        """
        self.L.append('\tprintf("%s\\n", {});\n'.format(p[2][1]))

    def p_End(self, p):
        """
        End : KW_END
        """
        self.L.append("\treturn 0;\n}")

    def p_empty(self, p):
        "empty :"
        pass

    def p_error(self, p: lex.LexToken):
        print(f"{Fore.RED}SYNTAX ERROR:{Style.RESET_ALL}")
        if p is not None:
            col = find_column(p)
            print(f"at line {p.lineno}, column {col}")
        else:
            print("Unexpected end of file")


if __name__ == "__main__":
    file = open("output.c", "w")

    with open(sys.argv[1], "rt") as f:
        input_code = f.read()
        if input_code[len(input_code) - 1] != "\n":
            input_code += "\n"

        pseudo_lexer.input_code = input_code
        lines = input_code.split("\n")
        pseudo_lexer.lines = lines
        obj = Pseudo_Parser()
        ast = obj.parse(input_code)
        print("Finished Parsing!")
        print(ast)
