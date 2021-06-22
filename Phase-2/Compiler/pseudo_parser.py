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
    #      | Start_Stmt
    #      | If_Stmt
    #      | While_Stmt"""
    #
    #      p[0] = p[1]
    #
    #  def p_expression_arithmetic_binop(self, p):
    #      """expression : expression PLUS expression
    #      | expression MINUS expression
    #      | expression TIMES expression
    #      | expression DIVIDE expression
    #      | expression PERCENT expression"""
    #
    #      if p[1].dType == None or p[3].dType == None:
    #          print("Variable is undefined")
    #          sys.exit()
    #
    #      elif p[1].dType == str and p[3].dType == str:
    #
    #          if p[2] == "+":
    #
    #              # Check for -1 here, as the support for ignoring whitespace is
    #              # present
    #              if isinstance(p[1], pseudo_ast.Variable):
    #                  length1 = self.var_lengths[(p[1].name, self.scope)] - 1
    #              else:
    #                  length1 = p[1].length - 1
    #
    #              if isinstance(p[3], pseudo_ast.Variable):
    #                  length2 = self.var_lengths[(p[3].name, self.scope)]
    #              else:
    #                  length2 = p[3].length
    #
    #              total_length = length1 + length2
    #              p[0] = pseudo_ast.BinaryOp(p[2], p[1], p[3], str, total_length)
    #
    #          else:
    #              print("Invalid operation")
    #              sys.exit()
    #
    #      elif p[1].dType == str or p[3].dType == str:
    #          print("Invalid operation")
    #          sys.exit()
    #
    #      elif p[1].dType == float or p[3].dType == float:
    #          p[0] = pseudo_ast.BinaryOp(p[2], p[1], p[3], float, 0)
    #
    #      elif p[1].dType == int and p[3].dType == int:
    #          p[0] = pseudo_ast.BinaryOp(p[2], p[1], p[3], int, 0)
    #
    #      else:
    #          print("Invalid operation")
    #          sys.exit()
    #
    #  def p_expression_comp_binop(self, p):
    #      """expression : expression LT expression
    #      | expression GT expression
    #      | expression LT_EQ expression
    #      | expression GT_EQ expression
    #      | expression EQ_EQ expression
    #      | expression NOT_EQ expression"""
    #
    #      if p[1].dType == None or p[3].dType == None:
    #          print("Variable is undefined")
    #          sys.exit()
    #
    #      elif p[1].dType == str or p[3].dType == str:
    #          print("Strings cannot be compared")
    #          sys.exit()
    #
    #      else:
    #          if p[1].dType == float or p[3].dType == float:
    #              p[0] = pseudo_ast.BinaryOp(p[2], p[1], p[3], float, 0)
    #
    #          elif p[1].dType == int and p[3].dType == int:
    #              p[0] = pseudo_ast.BinaryOp(p[2], p[1], p[3], int, 0)
    #
    #  def p_expression_literal(self, p):
    #      """expression : literal"""
    #
    #      p[0] = p[1]
    #
    #  def p_literal_int_constant(self, p):
    #      """literal : INT_LIT"""
    #
    #      p[0] = pseudo_ast.Constant(int, p[1], 0)
    #
    #  def p_literal_float_constant(self, p):
    #      """literal : FLOAT_LIT"""
    #
    #      p[0] = pseudo_ast.Constant(float, p[1], 0)
    #
    #  def p_literal_string_constant(self, p):
    #      """literal : STRING_LIT"""
    #
    #      p[0] = pseudo_ast.Constant(str, str(p[1]), len(p[1]) + 1)
    #
    #  def p_expression_var(self, p):
    #      "expression : KW_VAR"
    #
    #      if (p[1], self.scope) in self.variable_types:
    #          length = self.var_lengths[(p[1], self.scope)]
    #          p[0] = pseudo_ast.Variable(
    #              self.variable_types[(p[1], self.scope)], p[1], length
    #          )
    #
    #      else:
    #          p[0] = pseudo_ast.Variable(None, p[1], 0)
    #
    #  def p_error(self, p):
    #      print(f"Syntax error at {p.value!r}")

    ###############
    # OLD GRAMMAR #
    ###############
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
