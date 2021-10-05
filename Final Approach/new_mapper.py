from variable_mapper import Variable
from userDefinedTypes import VariableTypes
from exceptions import *

variable_obj = Variable()


class Mapper:
    __program = []
    __index = 0
    __current_indent = 0

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
        self.__program.insert(self.__index, (self.__current_indent * "\t") + string_to_write + "\n")
        self.__index += 1

    def increase_indent(self):
        self.__current_indent += 1

    def decrease_indent(self):
        variable_obj.exit_scope(self.__current_indent)
        if self.__current_indent > 0:
            self.__current_indent -= 1

    def add_main(self):
        self.insert_line("int main(int argc, char* argv[])")
        self.insert_line("{")
        self.increase_indent()

    def declare_variable(self, var_type, content):
        """
        pseudocode format: declare <variable name> <variable type>
        """
        for i in range(len(content)):
            variable_obj.insert_variable(content[i], self.__current_indent, var_type)
            self.insert_line(f"{var_type.name} {content[i]};")

    def initialize_variable(self, var_name, var_value):
        """
        pseudocode format: initialize <variable name> = <variable value>
        """
        if var_value.isnumeric():
            variable_obj.insert_variable(var_name, self.__current_indent, VariableTypes.int, int(var_value))
            self.insert_line(f"int {var_name} = {int(var_value)};")
        else:
            try:
                is_float = float(var_value)
                variable_obj.insert_variable(var_name, self.__current_indent, VariableTypes.float)
                self.insert_line(f"float {var_name} = {is_float};")
            except ValueError:
                variable_obj.insert_variable(var_name, self.__current_indent, VariableTypes.char)
                self.insert_line(f"char {var_name} = \"{var_value}\";")

    def input_variable(self, var_type, content):
        """
        pseudocode format: input <variable name> <variable type>
        pseudocode format: input <space separated variable names> <type of variables>
        """
        for i in range(len(content)):
            if not variable_obj.check_variable_in_scope(content[i], self.__current_indent):
                variable_obj.insert_variable(content[i], self.__current_indent, var_type)
                self.insert_line(f"{var_type.name} {content[i]};")
            self.insert_line(f"scanf(\"{var_type.value}\", &{content[i]});")

    def assign_variable(self, content):
        """
        pseudocode format: <variable result> = <variable 1> <operator> <variable 2>
        if variable already declared, just output the assignment statement
        else, check the type of the <variable 1> and assign that type to the result variable
        """
        assn_stmt = ""
        try:
            # if variable already declared
            if variable_obj.check_variable_in_scope(content[0], self.__current_indent):
                assn_stmt = " ".join(content) + ";"
            else:
                raise VariableNotDeclared
        except VariableNotDeclared:
            # variable not declared earlier
            try:
                result_var_1 = variable_obj.get_variable(content[2], self.__current_indent)
                type_var = result_var_1.var_type.name
                assn_stmt = type_var + " " + " ".join(content) + ";"
            except VariableNotDeclared:
                assn_stmt = "int " + " ".join(content) + ";"
        self.insert_line(assn_stmt)

    def print_variables(self, string: str, variable_list):
        """
        pseudocode format: print variable <variable name>
        pseudocode format: print <string>
        """
        i = 0
        variable_count = 0
        string_to_print = "printf(\""
        content_list = string.split(" ")
        while i < len(content_list):
            if content_list[i] != "variable":
                string_to_print += content_list[i] + " "
                i += 1
            else:
                i += 1
                result = variable_obj.get_variable(variable_list[variable_count], self.__current_indent)
                variable_count += 1
                string_to_print += result.var_type.value + " "
        string_to_print = string_to_print.rstrip()
        string_to_print += "\\n\", "
        for j in variable_list:
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

    #  def variable_check(self, var, index):
    #      return variable_obj.check_variable_in_scope(var, index)

    def while_loop(self, content):
        """
        while loop construct
        content: string
        """

        rel_op = ["!=", "==", "<", "<=", ">", ">="]

        for i, word in enumerate(content):
            if word in rel_op:

                # if iterator is not initialized then initialize it
                if not variable_obj.check_variable_in_scope(
                    content[i - 1], self.__current_indent
                ):
                    self.initialize_variable(content[i - 1], "0")

                # If the rhs of condition is not initialized then print error
                if not (
                    content[i + 1].isdigit()
                    or variable_obj.check_variable_in_scope(
                        content[i + 1], self.__current_indent
                    )
                ):
                    self.insert_line(
                        "Error: Variable {0} is not initialized".format(content[i + 1])
                    )

                self.insert_line(
                    "while({0} {1} {2})".format(content[i - 1], word, content[i + 1])
                )
                break
        else:
            if any(x in content for x in ["true", "1"]):
                self.insert_line("while(1)")

            # XXX: Should be replaced with else?
            elif any(x in content for x in ["false", "0"]):
                self.insert_line("while(0)")

        self.insert_line("{")
        self.increase_indent()

    #################################
    # Helper fucntions for for loop #
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
        init = update = ""
        variable_exist = 0
        iterator = content[0]
        pos = content.index("till")

        # For range starting
        range_start = content[pos - 1]
        type_ = "int "

        # Required if value of pre initialized iterator is changed
        need_init = 1
        if not range_start.isdigit():
            if range_start in ["a", "z"]:
                type_ = "char "
            else:
                range_start = "1"
            need_init = 0

        # For range ending
        range_end = content[pos + 1]
        if not range_end.isdigit():
            if range_end in ["z", "a"]:
                type_ = "char "

            else:
                variable_exist = variable_obj.check_variable_in_scope(
                    content[pos + 1], self.__current_indent
                )
                if variable_exist:
                    type_ = (
                        str(
                            variable_obj.get_variable(
                                content[pos + 1], self.__current_indent
                            ).var_type.name
                        )
                        + " "
                    )
                    val = int(
                        variable_obj.get_variable(
                            content[pos + 1], self.__current_indent
                        ).var_value
                    )
                    #  print(val)
                else:
                    self.insert_line(
                        "Error: Variable {0} is not defined".format(content[pos + 1])
                    )
                    #  XXX: Check whether to raise exception or not
                    #  raise VariableNotDeclared

        # if iterator is not defined
        if (
            not variable_obj.check_variable_in_scope(iterator, self.__current_indent)
            or need_init
        ):
            init = "{0}{1} = {2}".format(type_, iterator, range_start)
        else:
            range_start = int(
                variable_obj.get_variable(content[0], self.__current_indent).var_value
            )

        # evaluate the condition of for loop
        condition = "{0} <= {1}".format(iterator, range_end)

        last = content[-1]
        if not all(x in content for x in ["no", "update"]):

            if any(x in content for x in ["increment", "increase"]):
                oper, last = self.helper_oper_(last, "+")

            elif any(x in content for x in ["decrement", "decrease"]):
                oper, last = self.helper_oper_(last, "-")

            else:
                last = ""
                if type_ == "char ":
                    range_start = ord(range_start)
                    range_end = ord(range_end)

                if variable_exist:
                    oper = self.helper_greater_(int(range_start), val)
                else:
                    oper = self.helper_greater_(int(range_start), int(range_end))

            update = "{0}{1}{2}".format(iterator, oper, last)

        self.insert_line("for({0}; {1}; {2})".format(init, condition, update))
        self.insert_line("{")
        self.increase_indent()


    def end_func(self):
        self.decrease_indent()
        self.insert_line("}")

    def get_output_program(self):
        for line in self.__program:
            print(line, end="")


def run():
    f = open("test_for.txt", "r")
    data = f.readlines()
    map_obj = Mapper()
    for line in data:
        line = line.strip()
        if "start the program" in line:
            map_obj.start_the_program()
        elif "end" in line:
            map_obj.end_func()
        elif "initialize" in line and "=" in line:
            content = line.split(" ")[1:]
            var_name = content[0]
            var_value = content[-1]
            map_obj.initialize_variable(var_name, var_value)
        elif "assign" in line and "initialize" not in line:
            content = line.split(" ")
            try:
                content.remove("assign")
            except:
                pass
            map_obj.assign_variable(content)
        elif "input" in line:
            content = line.split(" ")[1:]
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
            map_obj.input_variable(var_type, content)
        elif "declare" in line:
            content = line.split(" ")[1:]
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
            map_obj.declare_variable(var_type, content)
        elif "print" in line:
            variable_names = []
            string_to_send = ""
            content_list = line.split(" ")[1:]
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
            map_obj.print_variables(string_to_send, variable_names)
        elif "else" in line or "if" in line:
            content = line.split(" ")
            map_obj.continued_if(content)

        # While and For
        elif "end" in line and ("for" in line or "while" in line):
            map_obj.end_func()

        elif "for" in line:
            content = line.split()[1:]
            map_obj.for_loop(content)

        elif "while" in line:
            content = line.split()[1:]
            map_obj.while_loop(content)

    map_obj.get_output_program()

# TODO: add comments support, break support, increment operation support.


if __name__ == "__main__":
    run()
