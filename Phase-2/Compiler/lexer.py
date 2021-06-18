import sys
from ply import lex

with open(sys.argv[1], "r") as f:
    input_code = f.read()

if input_code[len(input_code) - 1] != "\n":
    input_code += "\n"


# Find column number of token
def find_column(token):
    line_start = input_code.rfind("\n", 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

literals = ".=+-*/%!"

tokens = (
    # Relational Operators
    "EQ_EQ",
    "NOT_EQ",
    "LT",
    "LT_EQ",
    "GT",
    "GT_EQ",
    # Arithmetic Operator
    "ADD_EQ",
    "SUB_EQ",
    "MUL_EQ",
    "DIV_EQ",
    "MOD_EQ",
    # literals
    "INT_LIT",
    "FLOAT_LIT",
    "STRING_LIT",
    "IDENTIFIER",
)

keywords = {
    "start": "KW_START",
    "print": "KW_PRINT",
    "end": "KW_END",
    "if": "KW_IF",
    "else": "KW_ELSE",
    "for": "KW_FOR",
    "while": "KW_While",
    "add": "KW_ADD",
    "do": "KW_DO",
    "increment": "KW_INCR",
    "decrement": "KW_DECR",
    "initialize": "KW_INIT",
    "read": "KW_READ",
    "break": "KW_BREAK",
    #  "endif": "KW_ENDIF",
    #  "endfor": "KW_ENDFOR",
}

types = {"integer": "INT", "float": "FLOAT", "character": "CHAR"}

tokens = tokens + tuple(keywords.values()) + tuple(types.values())

# Relational Operators
t_EQ_EQ = r"=="
t_NOT_EQ = r"!="
t_LT = r"<"
t_LT_EQ = r"<="
t_GT = r">"
t_GT_EQ = r">="

# Arithmetic Operator
t_ADD_EQ = r"\+="
t_SUB_EQ = r"-="
t_MUL_EQ = r"\*="
t_DIV_EQ = r"/="
t_MOD_EQ = r"%="


def t_ANY_ignore_SPACES(t):
    r"\ +"


def t_ANY_ignore_TABS(t):
    r"\t+"


def t_NEWLINE(t):
    r"\n+"
    t.lexer.lineno += len(t.value)  # track line numbers


def t_ANY_ignore_SINGLE_COMMENT(t):
    r"//.*"


def t_ANY_ignore_MULTI_COMMENT(t):
    r"/\*(.|\n)*?\*/"

    t.lexer.lineno += t.value.count("\n")


def t_INT_LIT(t):
    r"\d+"

    t.value = ("int", int(t.value))
    return t


def t_FLOAT_LIT(t):
    r"[+-]?(\d+[.]\d*[eE][+-]?\d+)|[+-]?(\d+([.]\d*)|[+-]?\d+([eE][+-]?\d+)|[.]\d+([eE][+-]?\d+)?)"
    t.value = ("float", float(t.value))
    return t


def t_STRING_LIT(t):
    r"\"[^\"]*\" "

    if "\n" in t.value:
        lineno = t.lexer.lineno
        pos = find_column(t)
        splits = list(t.value.split("\n"))
        for i, line_ in enumerate(splits):
            line_actual = lines[lineno - 1]

            lineno += 1
        t.lexer.lineno += t.value.count("\n")
        return

    t.value = ("string", t.value)
    return t


def t_IDENTIFIER(t):
    r"([a-zA-Z]([a-zA-Z0-9_])*)|_"

    if t.value in keywords:
        t.type = keywords[t.value]
    else:
        t.type = "IDENTIFIER"
        t.value = ("identifier", t.value, find_column(t))

    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


#  def t_START_PSEUDOCODE(t):
#      r"startthepseudocode"
#      print("hi")
#
#
#  def t_IF_STATEMENT(t):
#      r"[iI]f"

lexer = lex.lex()
lexer.input(input_code)
lines = input_code.split("\n")

if __name__ == "__main__":
    for tok in lexer:
        print(tok)
