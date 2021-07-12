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
        self.insert_line("#include <stdio.h>\n")
        #  self.insert_line()

    def insert_line(self, string_to_write=""):
        self.program.insert(
            self.index, (self.current_indent * "\t") + string_to_write + "\n"
        )
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

    def input_variable(self, var_type, content):
        """
        Only support for integer and character for now.
        """
        length_vars = len(content)
        type_conversion = "%d" if var_type == "int" else "%c"
        content_string = ""
        content_input_string = ""
        for arg in content[: length_vars - 1]:
            content_string += arg + ", "
            content_input_string += "&" + arg + ", "
            self.variables[self.current_indent].append(arg)
        content_string += content[-1]
        content_input_string += "&" + content[-1]
        self.variables[self.current_indent].append(content[-1])
        self.insert_line(f"{var_type} {content_string};")
        self.insert_line(
            'scanf("' + length_vars * (type_conversion) + f'", {content_input_string});'
        )

    def print_variables(self, string: str, variable_list, variable_type_list):
        count = string.count("\z")
        string_list = string.split("\z")
        variable_list_converted = []
        for i in variable_type_list:
            if i == "int":
                variable_list_converted.append("%d")
            else:
                variable_list_converted.append("%c")
        print_string = ""
        index = 0
        length_vars = len(variable_list)
        for temp_string in string_list:
            print_string += temp_string
            if index < length_vars:
                print_string += variable_list_converted[index]
                index += 1
        content_string = ""
        for arg in variable_list[: length_vars - 1]:
            content_string += arg + ", "
        content_string += variable_list[-1]
        self.insert_line(f'printf("{print_string}\\n", {content_string});')

    def if_start(self, comparison_list):
        comparison_string = ""
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
        comparison_string = ""
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
        self.insert_line("{")
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
            if "1" in content:
                self.insert_line("while(1)\n{0}".format("{"))

        self.insert_line(
            "while({0} {1} {2})\n{3}".format(
                content[i - 1], content[i], content[i + 1], '{'
            )
        )

    def for_loop(self, content):
        """
        For loop construct
        """
        #  Till keyword is compulsory
        #  Have to take care of iteration of char
        #  need to handle if user doesn't want to initalize the iterator
        #  decrement
        #  data type add before initialization
        #  Check the greater of the two number
        type_ = "int"
        incr = 1
        pos = content.index("till")
        if "increment" in content or "increase" in content:
            incr = content[-1]
        init, range_start, range_end = content[0], content[pos - 1], content[pos + 1]

        self.insert_line(
            "for({0} {1}={2}; {1}<={3}; {1}+={4})\n{5}\n".format(
                type_, init, range_start, range_end, incr, "{"
            )
        )
        self.increase_indent

    def end_for(self):
        self.decrease_indent()
        self.insert_line("}")


def run():
    f = open("test3.txt", "r")
    data = f.readlines()
    map_obj = Mapper()
    for line in data:
        line = line.lower().strip()
        if "start the program" in line:
            map_obj.start_the_program()
        elif "input" in line:
            content = line.split(" ")[1:]
            var_type = ""
            if "char" in content[-1]:
                var_type = "char"
                content = content[:-1]
            elif "int" in content[-1]:
                var_type = "int"
                content = content[:-1]
            else:
                var_type = "int"
            map_obj.input_variable(var_type, content)
        # TODO: code for just declaring variable.
        # TODO: Implement logic for tracking variables first.
        elif "print" in line:
            content = line.split(" ")[1:]
            string_to_send = ""
            length_content = len(content)
            index = 0
            variable_names = []
            variable_types = []
            while index != length_content:
                if "variable" != content[index]:
                    string_to_send += content[index] + " "
                else:
                    index += 1
                    variable_names.append(content[index])
                    index += 1
                    if index < length_content and "int" in content[index]:
                        variable_types.append("int")
                    elif index < length_content and "char" in content[index]:
                        variable_types.append("char")
                    else:
                        # default value
                        variable_types.append("int")
                    string_to_send += "\z "
                index += 1
            map_obj.print_variables(string_to_send, variable_names, variable_types)
        elif "else" in line and "if" in line:
            content = line.split(" ")[2:]
            map_obj.continued_if(content)
        elif "else" in line:
            map_obj.else_end()
        elif "if" in line:
            content = line.split(" ")[1:]
            map_obj.if_start(content)

        # My changes
        elif "end" in line and ("for" in line or "while" in line):
            map_obj.end_for()

        elif "for" in line:
            content = line.split()[1:]
            map_obj.for_loop(content)

        elif "while" in line:
            content = line.split()[1:]
            map_obj.while_loop(content)

        elif "end" in line:
            map_obj.end_func()

    for line in map_obj.program:
        print(line, end="")


if __name__ == "__main__":
    run()
