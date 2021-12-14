import unittest
from mapper import Mapper
from exceptions import *


class TestDeclare(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj

    def test_integer(self):
        """
        1. Declaring integer by mentioning integer keyword explicitely.
        """
        test_input = "declare x integer"
        test_content = test_input.split(" ")
        self.test_map_obj.declare_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["int x;\n"])

    def test_float(self):
        """
        2. Declaring float by mentioning float keyword explicitely.
        """
        test_input = "declare x float"
        test_content = test_input.split(" ")
        self.test_map_obj.declare_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["float x;\n"])
    
    def test_character(self):
        """
        3. Declaring character by mentioning character keyword explicitely.
        """
        test_input = "declare var character"
        test_content = test_input.split(" ")
        self.test_map_obj.declare_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["char var;\n"])

    def test_no_type(self):
        """
        4. Declaring variable without mentioning type. 
        """
        test_input = "declare var"
        test_content = test_input.split(" ")
        self.test_map_obj.declare_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["int var;\n"])

    def test_redeclaring(self):
        """
        5. Redeclaring variable which is defined before. 
        """
        test_input = "declare new_variable int"
        test_content = test_input.split(" ")
        self.test_map_obj.declare_variable(test_content)
        self.assertRaises(VariableAlreadyDeclared, self.test_map_obj.declare_variable, test_content)
    
    def test_multi_vars(self):
        """
        6. Declaring multiple variables in a single line of pseudocode. 
        """
        test_input = "declare var1 var2 var3 integer"
        test_content = test_input.split(" ")
        self.test_map_obj.declare_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["int var1;\n", "int var2;\n", "int var3;\n"])
    

class TestInput(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj
    
    def test_no_type(self):
        """
        7. Taking input without mentioning type.
        """
        test_input = "input x"
        test_content = test_input.split(" ")
        self.test_map_obj.input_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ['int x;\n', 'scanf("%d", &x);\n'])
    
    def test_integer(self):
        """
        8. Taking input of integer.
        """
        test_input = "input x integer"
        test_content = test_input.split(" ")
        self.test_map_obj.input_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ['int x;\n', 'scanf("%d", &x);\n'])
    
    def test_character(self):
        """
        9. Taking input of character.
        """
        test_input = "input x character"
        test_content = test_input.split(" ")
        self.test_map_obj.input_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ['char x;\n', 'scanf("%c", &x);\n'])
    
    def test_float(self):
        """
        10. Taking input of float.
        """
        test_input = "input x float"
        test_content = test_input.split(" ")
        self.test_map_obj.input_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ['float x;\n', 'scanf("%f", &x);\n'])
    
    def test_multi_int(self):
        """
        11. Taking input of multiple integers.
        """
        test_input = "input x y z integer"
        test_content = test_input.split(" ")
        self.test_map_obj.input_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ['int x;\n', 'scanf("%d", &x);\n', 'int y;\n', 'scanf("%d", &y);\n', 'int z;\n', 'scanf("%d", &z);\n'])
    
    def test_multi_char(self):
        """
        12. Taking input of multiple characters.
        """
        test_input = "input x y z character"
        test_content = test_input.split(" ")
        self.test_map_obj.input_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ['char x;\n', 'scanf("%c", &x);\n', 'char y;\n', 'scanf("%c", &y);\n', 'char z;\n', 'scanf("%c", &z);\n'])
    
    def test_multi_float(self):
        """
        13. Taking input of multiple floats.
        """
        test_input = "input x y z float"
        test_content = test_input.split(" ")
        self.test_map_obj.input_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ['float x;\n', 'scanf("%f", &x);\n', 'float y;\n', 'scanf("%f", &y);\n', 'float z;\n', 'scanf("%f", &z);\n'])
    

class TestInitialize(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj
    
    def test_integer(self):
        """
        14. Initializing with integer type.
        """
        test_input = "initialize i = 21"
        test_content = test_input.split(" ")
        self.test_map_obj.assign_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ['int i = 21;\n'])
    
    def test_float(self):
        """
        15. Initializing with float type.
        """
        test_input = "initialize i = 3.14"
        test_content = test_input.split(" ")
        self.test_map_obj.assign_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ['float i = 3.14;\n'])
    
    def test_character(self):
        """
        16. Initializing with character type.
        """
        test_input = "initialize i = h"
        test_content = test_input.split(" ")
        self.test_map_obj.assign_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["char i = 'h';\n"])
    

class TestAssign(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj
    
    def test_variable(self):
        """
        17. Assigning variable.
        """
        test_input = "assign i = c"
        test_content = test_input.split(" ")
        self.test_map_obj.assign_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["char i = 'c';\n"])
    
    def test_relop(self):
        """
        18. Assigning relational operations.
        """
        test_input01 = "assign a = 2"
        test_input02 = "assign b = 2"
        test_input1 = "assign i1 = a + b"
        test_input2 = "assign i2 = a - b"
        test_input3 = "assign i3 = a * b"
        test_input4 = "assign i4 = a / b"
        test_content01 = test_input01.split(" ")
        test_content02 = test_input02.split(" ")
        test_content1 = test_input1.split(" ")
        test_content2 = test_input2.split(" ")
        test_content3 = test_input3.split(" ")
        test_content4 = test_input4.split(" ")
        self.test_map_obj.assign_variable(test_content01)
        self.test_map_obj.assign_variable(test_content02)
        self.test_map_obj.assign_variable(test_content1)
        self.test_map_obj.assign_variable(test_content2)
        self.test_map_obj.assign_variable(test_content3)
        self.test_map_obj.assign_variable(test_content4)
        self.assertEqual(self.test_map_obj.get_program_list(), ['int a = 2;\n', 'int b = 2;\n', 'int i1 = a + b;\n', 'int i2 = a - b;\n', 'int i3 = a * b;\n', 'float i4 = a / b;\n'])
    
    def test_increment_var(self):
        """
        19. Assigning relational operations on variable with some value.
        """
        test_input0 = "assign a = 3"
        test_input1 = "assign a = a + 2"
        test_input2 = "assign a = a - 2"
        test_input3 = "assign a = a * 2"
        test_input4 = "assign a = a / 2"
        test_content0 = test_input0.split(" ")
        test_content1 = test_input1.split(" ")
        test_content2 = test_input2.split(" ")
        test_content3 = test_input3.split(" ")
        test_content4 = test_input4.split(" ")
        self.test_map_obj.assign_variable(test_content0)
        self.test_map_obj.assign_variable(test_content1)
        self.test_map_obj.assign_variable(test_content2)
        self.test_map_obj.assign_variable(test_content3)
        self.test_map_obj.assign_variable(test_content4)
        self.assertEqual(self.test_map_obj.get_program_list(), ['int a = 3;\n', 'a = a + 2;\n', 'a = a - 2;\n', 'a = a * 2;\n', 'a = a / 2;\n'])


class TestPrint(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj
    
    def test_string(self):
        """
        20. Printing some string.
        """
        test_input = "print hello world"
        test_content = test_input.split(" ")
        self.test_map_obj.print_variables(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ['printf("hello world\\n");\n'])
        
    def test_variable(self):
        """
        21. Printing some variable.
        """
        test_input1 = "declare x integer"
        test_content1 = test_input1.split(" ")
        self.test_map_obj.declare_variable(test_content1)
        test_input2 = "print variable x"
        test_content2 = test_input2.split(" ")
        self.test_map_obj.print_variables(test_content2)
        self.assertEqual(self.test_map_obj.get_program_list(), ['int x;\n', 'printf("%d\\n", x);\n'])
        
    def test_string_variale_combination(self):
        """
        22. Printing some string with variable.
        """
        test_input1 = "declare x integer"
        test_content1 = test_input1.split(" ")
        self.test_map_obj.declare_variable(test_content1)
        test_input2 = "print the value of x is variable x metres in height"
        test_content2 = test_input2.split(" ")
        self.test_map_obj.print_variables(test_content2)
        self.assertEqual(self.test_map_obj.get_program_list(), ['int x;\n', 'printf("the value of x is %d metres in height\\n", x);\n'])
        
    def test_string_multiple_variale_combination(self):
        """
        23. Printing string and multiple variables.
        """
        test_input1 = "declare x y integer"
        test_content1 = test_input1.split(" ")
        self.test_map_obj.declare_variable(test_content1)
        test_input2 = "print the length and breadth of rectangle are variable x and variable y metres"
        test_content2 = test_input2.split(" ")
        self.test_map_obj.print_variables(test_content2)
        self.assertEqual(self.test_map_obj.get_program_list(), ['int x;\n', 'int y;\n', 'printf("the length and breadth of rectangle are %d and %d metres\\n", x, y);\n'])
    
    def test_undefined_variable(self):
        """
        24. Printing variable which is not declared.  
        """
        test_input = "print variable x"
        test_content = test_input.split(" ")
        self.assertRaises(VariableNotDeclared, self.test_map_obj.print_variables, test_content)
