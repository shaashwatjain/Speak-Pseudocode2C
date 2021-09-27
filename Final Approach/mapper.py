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

    def while_loop(self, content):
        """
        while loop construct
        """
        #  TODO: Check if i is inititalized or not
        rel_op = ["!=", "==", "<", "<=", ">", ">="]

        for i in range(len(content)):
            if content[i] in rel_op:
                break
        else:
            if any(x in content for x in ["true", "1"]):
                self.insert_line("while(1)")
            elif any(x in content for x in ["false", "0"]):
                self.insert_line("while(0)")
            self.insert_line("{")
            self.increase_indent()
            return

        self.insert_line(
            "while({0} {1} {2})".format(
                content[i - 1], content[i], content[i + 1]
            )
        )
        self.insert_line("{")
        self.increase_indent()

    def for_loop(self, content):
        """
        For loop construct
        """

        def check_oper_for(val, type_):
            op = ""
            flag = 1
            if abs(val) > 1:
                if type_ == "incr":
                    op = "+="
                else:
                    op = "-="
                flag = 0
            return val, op, flag

        #  Till keyword is compulsory
        #  Have to take care of iteration of char
        #  need to handle if user doesn't want to initalize the iterator
        #  decrement
        #  data type add before initialization
        #  Check the greater of the two number

        #####################################
        # Check for declaration of iterator #
        #####################################

        #  vobj = Variable()
        #  vobj.insert_variable("i", self.current_indent, VariableTypes.int, 5)
        #  temp = vobj.get_variable(content[0], self.current_indent)

        type_ = "int "
        update_val = 1
        pos = content.index("till")
        flag = 1
        if any(x in content for x in ["increment", "increase"]):
            #  if "increment" in content or "increase" in content:
            update_val, oper, flag = check_oper_for(int(content[-1]), "incr")

        if any(x in content for x in ["decrement", "decrease"]):
            update_val, oper, flag = check_oper_for(int(content[-1]), "decr")

        try:
            range_start = int(content[pos - 1])
        except:
            ###################################################
            # get the value of iterator from variable tracker #
            ###################################################
            if content[pos - 1] == "range":
                range_start = 1
            else:
                range_start = content[pos - 1]
            #  range_start = vobj.get_variable(
            #      content[0], self.current_indent
            #  )  # Replace by value from value tracker

        flag2 = 1
        try:
            range_end = int(content[pos + 1])
        except:
            range_end = content[pos + 1]
            flag2 = 0

        if flag:
            if range_end > range_start:
                oper = "++"
            else:
                oper = "--"

        # if no update is present in the statement
        if all(x in content for x in ["no", "update"]):
            self.insert_line(
                "for({type}{var}={start}; {var}<={end};)\n{ind}{open_par}".format(
                    var=content[0],
                    type=type_ if flag2 == 1 else 'char ',
                    start=range_start,
                    end=range_end,
                    ind=self.__current_indent*'\t',
                    open_par="{",
                )
            )

        else:
            self.insert_line(
                "for({type}{var}={start}; {var}<={end}; {var}{op} {update})\n{ind}{open_par}".format(
                    type=type_ if flag2 == 1 else 'char ',
                    var=content[0],
                    start=range_start,
                    end=range_end,
                    op=oper,
                    update=update_val if update_val != 1 else "",
                    ind=self.__current_indent*'\t',
                    open_par="{",
                )
            )
        self.increase_indent()

    def end_func(self):
        self.decrease_indent()
        self.insert_line("}")

    def get_output_program(self):
        for line in self.__program:
            print(line, end="")


def run():
    f = open("test_case.txt", "r")
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


if __name__ == "__main__":
    run()
