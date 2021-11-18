import unittest
from mapper import Mapper


class TestIf(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj

    def test_if(self):
        """
        Handle if
        """
        test_input = "if x"
        test_content = test_input.split(" ")
        self.test_map_obj.continued_if(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(x )\n", "{\n"])

class TestNestedIf(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj

    def test_NestedIf(self):
        """
        Handle if
        """
        test_input = "if x"
        test_input1 = "if x > 10"
        test_content = test_input.split(" ")
        test_content1 = test_input1.split(" ")
        self.test_map_obj.continued_if(test_content)
        self.test_map_obj.continued_if(test_content1)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(x )\n", "{\n", "\tif(x > 10 )\n", "\t{\n"])

class TestAndOr(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj

    def test_and_or(self):
        """
        Handle if
        """
        test_input = "if x and y and 10 or 12"
        test_content = test_input.split(" ")
        self.test_map_obj.continued_if(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(x && y && 10 || 12 )\n", "{\n"])

class TestNull(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj

    def test_null(self):
        """
        Handle if
        """
        test_input = " "
        self.test_map_obj.process_input(test_input)
        self.assertEqual(self.test_map_obj.get_program_list(), [])

class TestIfElseifElse(unittest.TestCase):

    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj

    def test_IfElseifElse(self):
        """
        Handle if
        """
        test_input1 = "if x"
        test_input2 = "else if y"
        test_input3 = "else"
        test_input4 = "end if"
        test_content1 = test_input1.split(" ")
        test_content2 = test_input2.split(" ")
        test_content3 = test_input3.split(" ")
        self.test_map_obj.continued_if(test_content1)
        self.test_map_obj.continued_if(test_content2)
        self.test_map_obj.continued_if(test_content3)
        self.test_map_obj.process_input(test_input4)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(x )\n", "{\n", "}\n", "else if(y )\n",
                                                                "{\n", "}\n", "else\n", "{\n", "}\n"])

class TestEnd(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj

    def test_end(self):
        """
        Handle if
        """
        test_input1 = "if x"
        test_input2 = "end if"
        test_content1 = test_input1.split(" ")
        self.test_map_obj.continued_if(test_content1)
        self.test_map_obj.process_input(test_input2)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(x )\n", "{\n", "}\n"])

class TestNestedLoop(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj

    def test_NestedLoop(self):
        """
        Handle if
        """
        test_input1 = "if 1"
        test_input2 = "if x"
        test_input3 = "else if y"
        test_input4 = "if z"
        test_input5 = "end if"
        test_input6 = "end if"
        test_input7 = "end if"

        self.test_map_obj.process_input(test_input1)
        self.test_map_obj.process_input(test_input2)
        self.test_map_obj.process_input(test_input3)
        self.test_map_obj.process_input(test_input4)
        self.test_map_obj.process_input(test_input5)
        self.test_map_obj.process_input(test_input6)
        self.test_map_obj.process_input(test_input7)

        self.assertEqual(self.test_map_obj.get_program_list(), ["if(1 )\n", "{\n", "\tif(x )\n", "\t{\n", "\t}\n",
                                                                "\telse if(y )\n", "\t{\n", "\t\tif(z )\n", "\t\t{\n",
                                                                "\t\t}\n", "\t}\n", "}\n"])

class TestOperator(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj

    def test_op1(self):
        """
        Handle if
        """
        test_input1 = "if x != y"
        test_input2 = "end if"
        test_content1 = test_input1.split(" ")
        self.test_map_obj.continued_if(test_content1)
        self.test_map_obj.process_input(test_input2)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(x != y )\n", "{\n", "}\n"])

    def test_op2(self):
        """
        Handle if
        """
        test_input3 = "if x > y"
        test_input4 = "end if"
        test_content3 = test_input3.split(" ")
        self.test_map_obj.continued_if(test_content3)
        self.test_map_obj.process_input(test_input4)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(x > y )\n", "{\n", "}\n"])

    def test_op3(self):

        test_input5 = "if x < y"
        test_input6 = "end if"
        test_content5 = test_input5.split(" ")
        self.test_map_obj.continued_if(test_content5)
        self.test_map_obj.process_input(test_input6)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(x < y )\n", "{\n", "}\n"])

    def test_op4(self):
        test_input5 = "if x >= y"
        test_input6 = "end if"
        test_content5 = test_input5.split(" ")
        self.test_map_obj.continued_if(test_content5)
        self.test_map_obj.process_input(test_input6)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(x >= y )\n", "{\n", "}\n"])

    def test_op5(self):
        test_input5 = "if x <= y"
        test_input6 = "end if"
        test_content5 = test_input5.split(" ")
        self.test_map_obj.continued_if(test_content5)
        self.test_map_obj.process_input(test_input6)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(x <= y )\n", "{\n", "}\n"])

    def test_op6(self):
        test_input5 = "if x == y"
        test_input6 = "end"
        test_content5 = test_input5.split(" ")
        self.test_map_obj.continued_if(test_content5)
        self.test_map_obj.process_input(test_input6)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(x == y )\n", "{\n", "}\n"])

    def test_op7(self):
        test_input5 = "if x % 2 == y"
        test_input6 = "end"
        test_content5 = test_input5.split(" ")
        self.test_map_obj.continued_if(test_content5)
        self.test_map_obj.process_input(test_input6)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(x % 2 == y )\n", "{\n", "}\n"])

    def test_op8(self):
        test_input5 = "if x / y == 2"
        test_input6 = "end"
        test_content5 = test_input5.split(" ")
        self.test_map_obj.continued_if(test_content5)
        self.test_map_obj.process_input(test_input6)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(x / y == 2 )\n", "{\n", "}\n"])

    def test_op9(self):
        test_input5 = "if not x == y"
        test_input6 = "end"
        test_content5 = test_input5.split(" ")
        self.test_map_obj.continued_if(test_content5)
        self.test_map_obj.process_input(test_input6)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(!x == y )\n", "{\n", "}\n"])

    def test_op10(self):
        test_input5 = "if not x and y"
        test_input6 = "end"
        test_content5 = test_input5.split(" ")
        self.test_map_obj.continued_if(test_content5)
        self.test_map_obj.process_input(test_input6)
        self.assertEqual(self.test_map_obj.get_program_list(), ["if(!x && y )\n", "{\n", "}\n"])

    def test_op11(self):
        test_input5 = "if year % 100 != 0 or year % 400 = 0"
        test_input6 = "end"
        test_content5 = test_input5.split(" ")
        self.test_map_obj.continued_if(test_content5)
        self.test_map_obj.process_input(test_input6)
        self.assertEqual(self.test_map_obj.get_program_list(), ['if(year % 100 != 0 || year % 400 == 0 )\n', '{\n', '}\n'])
