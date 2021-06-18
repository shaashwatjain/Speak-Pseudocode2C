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


def if_start(comparison_list):
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
    insert_line(current_indent, f"if({comparison_string})")
    insert_line(current_indent, "{")
    increase_indent()


def continued_if(comparison_list):
    decrease_indent()
    insert_line(current_indent, "}")
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
    insert_line(current_indent, f"else if({comparison_string})")
    insert_line(current_indent, "{")
    increase_indent()
    

def else_end():
    decrease_indent()
    insert_line(current_indent, "}")
    insert_line(current_indent, f"else")
    insert_line(current_indent, "{")
    increase_indent()


def end_func():
    decrease_indent()
    insert_line(current_indent, "}")

def run():
    f = open("Pseudocode.txt", "r")
    data = f.readlines()
    for line in data:
        line = line.strip()
        if "start the program" in line:
            start_the_program()
        elif "end" in line:
            end_func()
        elif "input" in line:
            content = line.split(" ")[1:]
            type = ""
            if "char" in content[-1]:
                type = "char"
                content = content[:-1]
            elif "int" in content[-1]:
                type = "int"
                content = content[:-1]
            else:
                type = "int"
            input_variable(type, content)
        # TODO: code for just declaring variable.
        # TODO: Implement logic for tracking variables first.
        elif "print" in line:
            content = line.split(" ")[1:]
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
        elif "else" in line and "if" in line:
            content = line.split(" ")[2:]
            continued_if(content)
        elif "else" in  line:
            else_end()
        elif "if" in line:
            content = line.split(" ")[1:]
            if_start(content)
    global program
    for line in program:
        print(line, end = "")

run()