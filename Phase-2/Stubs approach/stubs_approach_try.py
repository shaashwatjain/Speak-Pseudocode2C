program = []
index = 0
current_indent = 0

def start_the_program():
    """
    Function to add starting arguments to the program.
    """
    add_headers()
    add_main()


def add_headers():
    """
    Function to add headers to file
    """
    insert_line(current_indent, "#include <stdio.h>")
    insert_line(current_indent, "#include <stdlib.h>")
    insert_line(current_indent)


def insert_line(indent, string_to_write = ""):
    global index
    program.insert(index, (indent*"\t") + string_to_write + "\n")
    index += 1


def increase_indent():
    global current_indent
    current_indent += 1


def decrease_indent():
    global current_indent
    if current_indent > 0:
        current_indent -= 1


def add_main():
    insert_line(current_indent, "int main(int argc, char* argv[])")
    insert_line(current_indent, "{")
    increase_indent()


def input_variable(type, content):
    """
    Only support for integer and character for now.
    """
    length_vars = len(content)
    type_conversion = "%d" if type == "int" else "%c"
    content_string = ""
    content_input_string = ""
    for arg in content[:length_vars - 1]:
        content_string += arg + ", "
        content_input_string += "&" + arg + ", "
    content_string += content[-1]
    content_input_string += "&" + content[-1]
    insert_line(current_indent, f"{type} {content_string};")
    insert_line(current_indent, "scanf(\"" + length_vars* (type_conversion) + f"\", {content_input_string});")


def print_variables(string: str, variable_list, variable_type_list):
    count = string.count("\z")
    string_list = string.split("\z")
    variable_list_converted = []
    for i in variable_type_list:
        if i == "int":
            variable_list_converted.append("%d")
        else:
            variable_list_converted.append("%c")
    print_string = ''
    index = 0
    length_vars = len(variable_list)
    for temp_string in string_list:
        print_string += temp_string
        if index < length_vars:
            print_string += variable_list_converted[index]
            index += 1
    content_string = ''
    for arg in variable_list[:length_vars - 1]:
        content_string += arg + ", "
    content_string += variable_list[-1]
    insert_line(current_indent, f"printf(\"{print_string}\\n\", {content_string});")

def end_func():
    decrease_indent()
    insert_line(current_indent, "}")

def run():
    f = open("Pseudocode.txt", "r")
    data = f.readlines()
    for line in data:
        if "start the program" in line:
            start_the_program()
        elif "input" in line:
            content = line.strip().split(" ")[1:]
            type = ""
            if "char" in content[-1]:
                type = "char"
            else:
                type = "int"
            input_variable(type, content)
        elif "print" in line:
            content = line.strip().split(" ")[1:]
            string_to_send = ''
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
            print_variables(string_to_send, variable_names, variable_types)
        elif "end" in line:
            end_func()
    global program
    for line in program:
        print(line, end = "")

run()