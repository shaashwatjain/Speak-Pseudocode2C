from variable_mapper import Variable 
from userDefinedTypes import VariableTypes
from exceptions import *

variable_obj = Variable()

class Mapper:
    program = []
    index = 0
    current_indent = 0
    variables = dict()

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
        self.program.insert(self.index, (self.current_indent * "\t") + string_to_write + "\n")
        self.index += 1

    def increase_indent(self):
        self.current_indent += 1
        if self.current_indent not in self.variables:
            self.variables[self.current_indent] = []

    def decrease_indent(self):
        if self.current_indent in self.variables:
            del self.variables[self.current_indent]
        if self.current_indent > 0:
           self.current_indent -= 1

    def add_main(self):
        self.insert_line("int main(int argc, char* argv[])")
        self.insert_line("{")
        self.increase_indent()

    def declare_variable(self, var_type, content):
        """
        pseudocode format: declare <variable name> <variable type>
        """
        for i in range(len(content)):
            if var_type == "int":
                var_type_final = VariableTypes.int 
            elif var_type == "char":
                var_type_final = VariableTypes.char
            elif var_type == "float":
                var_type_final = VariableTypes.float 
            variable_obj.insert_variable(content[i], self.current_indent, var_type_final)
            self.insert_line(f"{var_type} {content[i]};")
        
    def initialize_variable(self, var_name, var_value):
        """
        pseudocode format: initialize <variable name> = <variable value>
        """
        if var_value.isnumeric():
            var_type = VariableTypes.int 
            variable_obj.insert_variable(var_name, self.current_indent, VariableTypes.int, int(var_value))
            self.insert_line(f"int {var_name} = {int(var_value)};")
        else:
            try:
                is_float = float(var_value)
                variable_obj.insert_variable(var_name, self.current_indent, VariableTypes.float)
                self.insert_line(f"float {var_name} = {is_float};")
            except:
                self.insert_line(f"char {var_name} = \"{var_value}\";")
                variable_obj.insert_variable(var_name, self.current_indent, VariableTypes.char)


    def input_variable(self, var_type, content):
        """
        pseudocode format: input <variable name> <variable type>
        pseudocode format: input <space separated variable names> <type of variables>
        """
        for i in range(len(content)):
            if var_type == "int":
                var_type_final = VariableTypes.int 
            elif var_type == "char":
                var_type_final = VariableTypes.char
            elif var_type == "float":
                var_type_final = VariableTypes.float 
            variable_obj.insert_variable(content[i], self.current_indent, var_type_final)
            self.insert_line(f"{var_type} {content[i]};")
            self.insert_line(f"scanf(\"{var_type_final.value}\", &{content[i]});")

    def assign_variable(self, content):
        """
        pseudocode format: <variable result> = <variable 1> <operator> <variable 2>
        if variable already declared, just output the assignment statement 
        else, check the type of the <variable 1> and assign that type to the result variable 
        """
        type_dict = {"%d": "int", "%f": "float", "%c": "char"}
        try:
            # if variable already declared  
            result = variable_obj.get_variable(content[0], self.current_indent)
            assn_stmt = " ".join(content)
        except:
            # variable not declared earlier
            try:
                result_var_1 = variable_obj.get_variable(content[2], self.current_indent)
                type_var = type_dict[result_var_1.var_type.value]
                assn_stmt = type_var + " " + " ".join(content)
            except:
                assn_stmt = "int " + " ".join(content)
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
                result = variable_obj.get_variable(variable_list[variable_count], self.current_indent)
                variable_count += 1
                string_to_print += result.var_type.value + " "
        string_to_print = string_to_print.rstrip()
        string_to_print += "\\n\", "
        for j in variable_list:
            string_to_print += j + ", "
        string_to_print = string_to_print[:-2]
        string_to_print += ");"
        self.insert_line(string_to_print)

    def if_start(self, comparison_list):
        comparison_string = ''
        for word in comparison_list:
            if "or" == word:
                comparison_string += "||" + " "
            elif "and" == word:
                comparison_string += "&&" + " "
            else:
                try:
                    num = int(word)
                    comparison_string += num + " "
                except ValueError:
                    if len(word) == 1:
                        comparison_string += "'" + word + "' "
                    else:
                        comparison_string += word + " "
        self.insert_line(f"if({comparison_string})")
        self.insert_line("{")
        self.increase_indent()

    def continued_if(self, comparison_list):
        self.decrease_indent()
        self.insert_line("}")
        comparison_string = ''
        for word in comparison_list:
            if "or" == word:
                comparison_string += "||" + " "
            elif "and" == word:
                comparison_string += "&&" + " "
            else:
                try:
                    num = int(word)
                    comparison_string += num + " "
                except ValueError:
                    if len(word) == 1:
                        comparison_string += "'" + word + "' "
                    else:
                        comparison_string += word + " "
        self.insert_line(f"else if({comparison_string})")
        self.insert_line( "{")
        self.increase_indent()

    def else_end(self):
        self.decrease_indent()
        self.insert_line("}")
        self.insert_line(f"else")
        self.insert_line("{")
        self.increase_indent()

    def end_func(self):
        self.decrease_indent()
        self.insert_line("}")


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
            var_value =  content[-1]
            map_obj.initialize_variable(var_name, var_value)
        elif "=" in line or "assign" in line and "initialize" not in line:
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
                var_type = "char"
                content = content[:-1]
            elif "integer" in content:
                var_type = "int"
                content = content[:-1]
            elif "float" in content:
                var_type = "float"
                content = content[:-1]
            else:
                var_type = "int"
            map_obj.input_variable(var_type, content)
        elif "declare" in line:
            content = line.split(" ")[1:]
            var_type = ""
            if "character" in content:
                var_type = "char"
                content = content[:-1]
            elif "integer" in content:
                var_type = "int"
                content = content[:-1]
            elif "float" in content:
                var_type = "float"
                content = content[:-1]
            else:
                var_type = "int"
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
        elif "else" in line and "if" in line:
            content = line.split(" ")[2:]
            map_obj.continued_if(content)
        elif "else" in line:
            map_obj.else_end()
        elif "if" in line:
            content = line.split(" ")[1:]
            map_obj.if_start(content)
    for line in map_obj.program:
        print(line, end="")


if __name__ == "__main__":
    run()
