from variable_mapper import Variable

var_obj = Variable()


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

        if comparison_list[:2] == ['else','if']:
            self.insert_line(f"else if({comparison_string})")
        elif comparison_list[:1] == ['if']:
            self.insert_line(f"if({comparison_string})")
        elif comparison_list[:1] == ['else']:
            self.insert_line("else")

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


def run():
    f = open("test.txt", "r")
    op = open("output.c", "w")
    data = f.readlines()
    map_obj = Mapper()
    for line in data:
        line = line.strip()
        if "start the program" in line:
            map_obj.start_the_program()
        elif "end" in line:
            map_obj.end_func()
        elif "else" in line and "if" in line:
            content = line.split(" ")
            map_obj.continued_if(content)
        elif "else" in line:
            content = line.split(" ")
            map_obj.continued_if(content)
        elif "if" in line:
            content = line.split(" ")
            map_obj.continued_if(content)
        for i in map_obj.program:
            op.write(i)
        map_obj.program = []


if __name__ == "__main__":
    run()
