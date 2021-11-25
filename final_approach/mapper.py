from typing import final
from exceptions import *
from userDefinedTypes import VariableTypes
from variable_mapper import Variable
from nlp import NLP


class Mapper:
    def __init__(self):
        self._program = []
        self._index = 0
        self._current_indent = 0
        self.variable_obj = Variable()
        self.nlp_obj = NLP()

    def start_the_program(self):
        """
        Function to add starting arguments to the program.
        """
        self.add_headers()
        self.add_main()

    def add_headers(self):
        """
        Function to add headers to file
        """
        self.insert_line("#include <stdio.h>")
        self.insert_line()

    def insert_line(self, string_to_write=""):
        self._program.insert(self._index, (self._current_indent * "\t") + string_to_write + "\n")
        self._index += 1

    def increase_indent(self):
        self._current_indent += 1

    def decrease_indent(self):
        self.variable_obj.exit_scope(self._current_indent)
        if self._current_indent > 0:
            self._current_indent -= 1

    def add_main(self):
        self.insert_line("int main(int argc, char* argv[])")
        self.insert_line("{")
        self.increase_indent()

    def declare_variable(self, content):
        """
        pseudocode format: declare <variable name> <variable type>
        """
        content.pop(0)
        var_type = ""
        if "character" in content:
            var_type = VariableTypes.char
            content = content[:-1]
        elif "integer" in content:
            var_type = VariableTypes.int
            content = content[:-1]
        elif "float" in content:
            var_type = VariableTypes.float
            content = content[:-1]
        else:
            var_type = VariableTypes.int

        for i in range(len(content)):
            self.variable_obj.insert_variable(content[i], self._current_indent, var_type)
            self.insert_line(f"{var_type.name} {content[i]};")

    # def initialize_variable(self, content):
    #     """
    #     pseudocode format: initialize <variable name> = <variable value>
    #     """
    #     content.pop(0)
    #     var_name = content[0]
    #     var_value = content[-1]
    #     if var_value.isnumeric():
    #         self.variable_obj.insert_variable(var_name, self._current_indent, VariableTypes.int, int(var_value))
    #         self.insert_line(f"int {var_name} = {int(var_value)};")
    #     else:
    #         try:
    #             is_float = float(var_value)
    #             self.variable_obj.insert_variable(var_name, self._current_indent, VariableTypes.float)
    #             self.insert_line(f"float {var_name} = {is_float};")
    #         except ValueError:
    #             self.variable_obj.insert_variable(var_name, self._current_indent, VariableTypes.char)
    #             self.insert_line(f"char {var_name} = \"{var_value}\";")

    def input_variable(self, content):
        """
        pseudocode format: input <variable name> <variable type>
        pseudocode format: input <space separated variable names> <type of variables>
        """
        content.pop(0)
        var_type = ""
        if "character" in content:
            var_type = VariableTypes.char
            content = content[:-1]
        elif "integer" in content:
            var_type = VariableTypes.int
            content = content[:-1]
        elif "float" in content:
            var_type = VariableTypes.float
            content = content[:-1]
        else:
            var_type = VariableTypes.int

        for i in range(len(content)):
            if not self.variable_obj.check_variable_in_scope(content[i], self._current_indent):
                self.variable_obj.insert_variable(content[i], self._current_indent, var_type)
                self.insert_line(f"{var_type.name} {content[i]};")
                self.insert_line(f"scanf(\"{var_type.value}\", &{content[i]});")
            else:
                current_var = self.variable_obj.get_variable(content[i], self._current_indent)
                self.insert_line(f"scanf(\"{current_var.fmt_specifier}\", &{current_var.var_name});")

    def assign_variable(self, content):
        content.pop(0)
        assn_stmt = ""
        if len(content) == 3:   # if "assign a = 3"
            if content[-1].isnumeric():
                if not self.variable_obj.check_variable_in_scope(content[0], self._current_indent):
                    assn_stmt = "int "
                    self.variable_obj.insert_variable(content[0], self._current_indent, VariableTypes.int, int(content[-1]))
                assn_stmt += " ".join(content) + ";"

            elif "." in content[-1]:
                if not self.variable_obj.check_variable_in_scope(content[0], self._current_indent):
                    assn_stmt = "float "
                    self.variable_obj.insert_variable(content[0], self._current_indent, VariableTypes.float)
                assn_stmt += " ".join(content) + ";"

            elif self.variable_obj.check_variable_in_scope(content[-1], self._current_indent):
                result_var_1 = self.variable_obj.get_variable(content[-1], self._current_indent)
                type_var = result_var_1.var_type.name
                if not self.variable_obj.check_variable_in_scope(content[0], self._current_indent):
                    assn_stmt = result_var_1.var_type.name + " "
                    self.variable_obj.insert_variable(content[0], self._current_indent, result_var_1.var_type)
                assn_stmt += " ".join(content) + ";"

            else:
                if not self.variable_obj.check_variable_in_scope(content[0], self._current_indent):
                    assn_stmt = "char "
                    self.variable_obj.insert_variable(content[0], self._current_indent, VariableTypes.char, content[-1])
                assn_stmt += content[0] + " = '" + content[-1] + "';"

            self.insert_line(assn_stmt)

        elif len(content) == 5:     # if "assign a = b + c"
            if content[-1].isnumeric() and content[-3].isnumeric() and content[-2] != "/":      # b and c numeric
                if not self.variable_obj.check_variable_in_scope(content[0], self._current_indent):
                    assn_stmt = "int "
                    self.variable_obj.insert_variable(content[0], self._current_indent, VariableTypes.int)
                assn_stmt += " ".join(content) + ";"

            elif "." in content[-1] or "." in content[-3] or content[-2] == "/":    # decimal in b or c or division operation
                if not self.variable_obj.check_variable_in_scope(content[0], self._current_indent):
                    assn_stmt = "float "
                    self.variable_obj.insert_variable(content[0], self._current_indent, VariableTypes.float)
                assn_stmt += " ".join(content) + ";"

            else:
                if self.variable_obj.check_variable_in_scope(content[-3], self._current_indent) and self.variable_obj.check_variable_in_scope(content[-1], self._current_indent):   # b and c are variables
                    assn_stmt = ""
                    final_type = ""
                    result_var_1 = self.variable_obj.get_variable(content[-3], self._current_indent)
                    result_var_2 = self.variable_obj.get_variable(content[-1], self._current_indent)
                    if result_var_2.var_type.name == result_var_1.var_type.name:
                        final_type = result_var_1.var_type
                    else:
                        if "char" in [result_var_1.var_type.name, result_var_2.var_type.name]:
                            final_type = VariableTypes.char
                        elif "float" in [result_var_1.var_type.name, result_var_2.var_type.name]:
                            final_type = VariableTypes.float
                        else:
                            final_type = result_var_1.var_type
                    if not self.variable_obj.check_variable_in_scope(content[0], self._current_indent):
                        assn_stmt = final_type.name + " "
                        self.variable_obj.insert_variable(content[0], self._current_indent, final_type)
                    assn_stmt += " ".join(content) + ";"

                elif self.variable_obj.check_variable_in_scope(content[-3], self._current_indent) or self.variable_obj.check_variable_in_scope(content[-1], self._current_indent):    # b or c is variable but not both
                    final_type = []
                    result_var_1, result_var_2 = "", ""
                    # fetching variable details from variable mapper object
                    if self.variable_obj.check_variable_in_scope(content[-3], self._current_indent):
                        result_var_1 = self.variable_obj.get_variable(content[-3], self._current_indent)
                        type_var = result_var_1.var_type.name
                        final_type.append(result_var_1.var_type)
                        result_var_1 = content[-3]
                    else:
                        if content[-3].isnumeric():
                            final_type.append(VariableTypes.int)
                            result_var_1 = content[-3]
                        elif "." in content[-3]:
                            final_type.append(VariableTypes.float)
                            result_var_1 = content[-3]
                        else:
                            final_type.append(VariableTypes.char)
                            result_var_1 = "'" + content[-3] + "'"

                    if self.variable_obj.check_variable_in_scope(content[-1], self._current_indent):
                        result_var_2 = self.variable_obj.get_variable(content[-1], self._current_indent)
                        if final_type == "":
                            type_var = result_var_2.var_type.name
                            final_type.append(result_var_2.var_type)
                        result_var_2 = content[-1]
                    else:
                        if content[-1].isnumeric():
                            final_type.append(VariableTypes.int)
                            result_var_2 = content[-1]
                        elif "." in content[-1]:
                            final_type.append(VariableTypes.float)
                            result_var_2 = content[-1]
                        else:
                            final_type.append(VariableTypes.char)
                            result_var_2 = "'" + content[-1] + "'"

                    # checking variable types
                    if VariableTypes.char in final_type:
                        final_type = VariableTypes.char
                    elif VariableTypes.float in final_type:
                        final_type = VariableTypes.float
                    else:
                        final_type = final_type[0]

                    if not self.variable_obj.check_variable_in_scope(content[0], self._current_indent):
                        assn_stmt = final_type.name + " "
                        self.variable_obj.insert_variable(content[0], self._current_indent, VariableTypes.char)
                    assn_stmt += content[0] + " = " + result_var_1 + " " + content[-2] + " " + result_var_2 + ";"

                else:
                    if not self.variable_obj.check_variable_in_scope(content[0], self._current_indent):
                        assn_stmt = "char "
                        self.variable_obj.insert_variable(content[0], self._current_indent, VariableTypes.char)
                    assn_stmt += content[0] + " = '" + content[2] + "' "+ content[3] + " '" + content[4] + "';"
            self.insert_line(assn_stmt)

    def print_variables(self, content_list):
        """
        pseudocode format: print variable <variable name>
        pseudocode format: print <string>
        """
        variable_names = []
        string_to_send = ""
        content_list.pop(0)
        i = 0
        while i < len(content_list):
            if content_list[i] != "variable":
                string_to_send += content_list[i] + " "
                i += 1
            else:
                string_to_send += content_list[i] + " "
                i += 1
                variable_names.append(content_list[i])
                i += 1
        i = 0
        variable_count = 0
        string_to_print = "printf(\""
        content_list = string_to_send.split(" ")
        while i < len(content_list):
            if content_list[i] != "variable":
                string_to_print += content_list[i] + " "
                i += 1
            else:
                i += 1
                result = self.variable_obj.get_variable(variable_names[variable_count], self._current_indent)
                variable_count += 1
                string_to_print += result.var_type.value + " "
        string_to_print = string_to_print.rstrip()
        string_to_print += "\\n\", "
        for j in variable_names:
            string_to_print += j + ", "
        string_to_print = string_to_print[:-2]
        string_to_print += ");"
        self.insert_line(string_to_print)

    def continued_if(self, comparison_list):
        comparison_string = ''
        for word in comparison_list:
            if "or" == word:
                comparison_string += "||" + " "
            elif "and" == word:
                comparison_string += "&&" + " "
            elif word == "=":
                comparison_string += "==" + " "
            elif word == "not":
                comparison_string += "!"
            else:
                if word != 'if' and word != 'else':
                    comparison_string += word + " "

        if comparison_list[:2] == ['else', 'if']:
            self.end_func()
            self.insert_line(f"else if({comparison_string})")
        elif comparison_list[:1] == ['if']:
            self.insert_line(f"if({comparison_string})")
        elif comparison_list[:1] == ['else']:
            self.end_func()
            self.insert_line("else")

        self.insert_line("{")
        self.increase_indent()

    # Helper to check if a string is int or not
    # This method is valid for negative numbers also
    def is_digit(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    def while_loop(self, content):
        """
        while loop construct
        content: string
        """
        content.pop(0)
        rel_op = ["!=", "==", "<", "<=", ">", ">="]
        bin_op = {"and": "&&", "or": "||"}

        string = "while("
        # used to initialize only 1 uninitialized variable
        flag = 1
        for i, word in enumerate(content):
            if word in rel_op:
                string += " " + word + " "

            elif self.is_digit(word) or word in ["true", "false"]:
                string += word

            elif word in bin_op.keys():
                string += " " + bin_op[word] + " "

            else:
                if self.variable_obj.check_variable_in_scope(word, self._current_indent):
                    string += word
                else:
                    if flag:
                        self.assign_variable(["", word, "=", "0"])
                        string += word
                        flag = 0
                    else:
                        raise VariableNotDeclared

        self.insert_line(string + ")")
        self.insert_line("{")
        self.increase_indent()


    #################################
    # Helper functions for for loop #
    #################################
    def helper_oper_(self, val, sign):
        if int(val) > 1:
            oper = "{0}=".format(sign)
        else:
            oper = "{0}{0}".format(sign)
            val = ""
        return oper, val


    def helper_greater_(self, x, y):
        if x > y:
            oper = "--"
        else:
            oper = "++"
        return oper


    #######################
    # For loop constructs #
    #######################
    def for_loop(self, content):
        """
        For loop construct
        content: String
        """
        content.pop(0)
        init = update = ""
        variable_exist = 0
        iterator = content[0]
        pos = content.index("till")

        # For range starting
        range_start = content[pos - 1]
        raw_type_ = VariableTypes.int
        type_ = "int "

        # Required if value of pre initialized iterator is changed
        is_init = 1
        if not self.is_digit(range_start):
            if range_start in ["a", "z"]:
                raw_type_ = VariableTypes.char
                type_ = "char "
                range_start_val = ord(range_start)

            elif range_start != "range" and self.variable_obj.get_variable(
                range_start, self._current_indent
            ):
                obj = self.variable_obj.get_variable(range_start, self._current_indent)
                type_ = str(obj.var_type.name) + " "
                range_start_val = obj.var_value

            else:
                #  elif range_start == "range":
                # checking if range_start==range and iter is declared before
                if self.variable_obj.check_variable_in_scope(
                    iterator, self._current_indent
                ):
                    obj = self.variable_obj.get_variable(iterator, self._current_indent)
                    type_ = str(obj.var_type.name) + " "
                    range_start_val = obj.var_value

                else:
                    range_start = "1"
                    range_start_val = 1
            if range_start_val is None:
                range_start_val = 1

            is_init = 0

        else:
            range_start_val = int(range_start)

        # For range ending
        range_end = content[pos + 1]
        if not self.is_digit(range_end):
            if range_end in ["z", "a"]:
                raw_type_ = VariableTypes.char
                type_ = "char "
                range_end_val = ord(range_end)

            else:
                variable_exist = self.variable_obj.check_variable_in_scope(
                    content[pos + 1], self._current_indent
                )
                if variable_exist:
                    type_ = (
                        str(
                            self.variable_obj.get_variable(
                                content[pos + 1], self._current_indent
                            ).var_type.name
                        )
                        + " "
                    )
                    range_end_val = self.variable_obj.get_variable(
                        content[pos + 1], self._current_indent
                    ).var_value

                    if range_end_val is None:
                        range_end_val = range_start_val + 1
                else:
                    raise VariableNotDeclared
        else:
            range_end_val = int(range_end)

        # if iterator is not defined
        if not self.variable_obj.check_variable_in_scope(iterator, self._current_indent):
            init = "{0}{1} = {2}".format(type_, iterator, range_start)
            # Add declare stmt here type_ is not working here
            self.variable_obj.insert_variable(iterator, self._current_indent, raw_type_)

        else:
            if is_init:
                init = "{0} = {1}".format(iterator, range_start)

            range_start = self.variable_obj.get_variable(
                content[0], self._current_indent
            ).var_value
            if range_start is None:
                range_start = 1

        # evaluate the condition of for loop
        cond_oper = "<=" if range_start_val < range_end_val else ">="
        condition = "{0} {1} {2}".format(iterator, cond_oper, range_end)

        last = content[-1]
        if not all(x in content for x in ["no", "update"]):

            if any(x in content for x in ["increment", "increase"]):
                oper, last = self.helper_oper_(last, "+")

            elif any(x in content for x in ["decrement", "decrease"]):
                oper, last = self.helper_oper_(last, "-")

            else:
                last = ""
                oper = self.helper_greater_(range_start_val, range_end_val)

            update = "{0}{1}{2}".format(iterator, oper, last)

        self.insert_line("for({0}; {1}; {2})".format(init, condition, update))
        self.insert_line("{")
        self.increase_indent()

    def end_func(self):
        self.decrease_indent()
        self.insert_line("}")

    def get_output_program(self):
        for line in self._program:
            print(line, end="")

    def get_program_list(self) -> list:
        return self._program

    def comment(self, content: list):
        if "comment" in content[0]:
            content.pop(0)
        str_to_write = "// "
        for word in content:
            if word not in '':
                str_to_write += word + " "
        if len(str_to_write) > 3:
            self.insert_line(str_to_write)

    def return_statement(self, content: list):
        if len(content) == 2 and "return" in content[0]:
            if content[1].isnumeric():
                line_to_insert = "return " + content[1] + ";"
                self.insert_line(line_to_insert)
            else:
                fetched_variable = self.variable_obj.get_variable(content[1], self._current_indent)
                if fetched_variable.var_type.name == "int":
                    line_to_insert = "return " + content[1] + ";"
                    self.insert_line(line_to_insert)
                else:
                    raise ReturnTypeIncompatibleException
        else:
            raise ReturnTypeIncompatibleException

    def break_stmt(self):
        self.insert_line("break;")

    def continue_stmt(self):
        self.insert_line("continue;")

    def exit_func(self):
        while(self._current_indent > 1):
            self.end_func()

        if(self._current_indent == 1):
            self.end_func()


    __no_args_dict = {
        "start": start_the_program,
        "end": end_func,
        "exit": exit_func,
        "break": break_stmt,
        "continue": continue_stmt,
    }
    __content_args_dict = {
        # "initialize": initialize_variable,
        "assign": assign_variable,
        "input": input_variable,
        "declare": declare_variable,
        "print": print_variables,
        "if": continued_if,
        "else": continued_if,
        "for": for_loop,
        "while": while_loop,
        "comment": comment,
        "return": return_statement,
    }

    def process_input(self, line: str) -> list:
        start_len = len(self._program)
        line = line.strip().lower()
        line = self.nlp_obj.process_nlp(line)
        content = line.split(" ")
        if content[0] in self.__content_args_dict:
            self.__content_args_dict[content[0]](self, content)
        elif content[0] in self.__no_args_dict:
            self.__no_args_dict[content[0]](self)
        elif "end" in content[0]:
            self.__no_args_dict["end"](self)
        else:
            self.comment(content)
        return self._program[start_len:]


if __name__ == "__main__":
    f = open("test_new_assign.txt", "r")
    data = f.readlines()
    map_obj = Mapper()
    for text in data:
        map_obj.process_input(text)
    map_obj.get_output_program()
