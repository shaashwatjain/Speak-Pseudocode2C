import unittest
from mapper import Mapper
from exceptions import VariableAlreadyDeclared, VariableNotDeclared


class TestWhile(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj

    def test_both_int_1(self):
        """
        Testing when both the lhs and rhs is int and op -> <
        """
        test_input = "while 7 < 9"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(), ["while(7 < 9)\n", "{\n"]
        )

    def test_both_int_2(self):
        """
        Testing when both the lhs and rhs is int and op -> >
        """
        test_input = "while 1 > 0"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(), ["while(1 > 0)\n", "{\n"]
        )

    def test_both_int_3(self):
        """
        Testing when both the lhs and rhs is int and op -> ==
        """
        test_input = "while 1 == 1"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(), ["while(1 == 1)\n", "{\n"]
        )

    def test_mix_cond_1(self):
        """
        Testing when either lhs or rhs is a variable and not initialized less than
        """
        test_input = "while i < 100"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(),
            ["int i = 0;\n", "while(i < 100)\n", "{\n"],
        )

    def test_mix_cond_2(self):
        """
        Testing when either lhs or rhs is a variable and not initialized greater than
        """
        test_input = "while 10 >= count"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(),
            ["int count = 0;\n", "while(10 >= count)\n", "{\n"],
        )

    def test_mix_cond_3(self):
        """
        Testing when either lhs or rhs is a variable and not initialized greater than
        """
        test_input = "while count > 15"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(),
            ["int count = 0;\n", "while(count > 15)\n", "{\n"],
        )

    def test_mix_cond_4(self):
        """
        Testing when either lhs or rhs is a variable and initialized not equal
        """
        test_input = "initialize i = 0"
        test_content = test_input.split()
        self.test_map_obj.initialize_variable(test_content)

        test_input = "while i != 10"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(),
            ["int i = 0;\n", "while(i != 10)\n", "{\n"],
        )

    def test_mix_cond_5(self):
        """
        Testing when either lhs or rhs is a variable and initialized not equal
        """
        test_input = "initialize count = 0"
        test_content = test_input.split()
        self.test_map_obj.initialize_variable(test_content)

        test_input = "while 10 < count "
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(),
            ["int count = 0;\n", "while(10 < count)\n", "{\n"],
        )

    def test_both_var_1(self):
        """
        Testing when both lhs and rhs is a variable and lhs is initialized
        """
        test_input = "initialize num = 10"
        test_content = test_input.split()
        self.test_map_obj.initialize_variable(test_content)

        test_input = "while num > count"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(),
            ["int num = 10;\n", "int count = 0;\n", "while(num > count)\n", "{\n"],
        )

    def test_both_var_2(self):
        """
        Testing when both lhs and rhs is a variable and rhs is initialized
        """
        test_input = "initialize num = 5"
        test_content = test_input.split()
        self.test_map_obj.initialize_variable(test_content)

        test_input = "while count > num"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(),
            ["int num = 5;\n", "int count = 0;\n", "while(count > num)\n", "{\n"],
        )

    def test_both_var_3(self):
        """
        Testing when both lhs and rhs is a variable and rhs is uninitialized and exception is raised
        """
        test_input = "while i > j"
        test_content = test_input.split()
        with self.assertRaises(VariableNotDeclared):
            self.test_map_obj.while_loop(test_content)

    def test_unary_1(self):
        """
        Testing when only unary condition is present
        """
        test_input = "while 1"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["while(1)\n", "{\n"])

    def test_unary_2(self):
        """
        Testing when only unary condition is present
        """
        test_input = "while 0"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["while(0)\n", "{\n"])

    def test_unary_3(self):
        """
        Testing when only unary condition is present
        """
        test_input = "while 5"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["while(5)\n", "{\n"])

    def test_unary_4(self):
        """
        Testing when only unary condition is present
        """
        test_input = "while true"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["while(true)\n", "{\n"])

    def test_unary_5(self):
        """
        Testing when only unary condition is present
        """
        test_input = "while false"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(), ["while(false)\n", "{\n"]
        )

    def test_nested_loop_1(self):
        """
        Testing a nested while loop
        """
        test_input = "initialize j = 10"
        test_content = test_input.split()
        self.test_map_obj.initialize_variable(test_content)

        test_input = "initialize num = 5"
        test_content = test_input.split()
        self.test_map_obj.initialize_variable(test_content)

        test_input = "while i < num"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)

        test_input = "while j > i"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)

        self.assertEqual(
            self.test_map_obj.get_program_list(),
            [
                "int j = 10;\n",
                "int num = 5;\n",
                "int i = 0;\n",
                "while(i < num)\n",
                "{\n",
                "\twhile(j > i)\n",
                "\t{\n",
            ],
        )

    def test_nested_loop_2(self):
        """
        Testing a nested while loop with uninitialized var
        """
        test_input = "initialize j = 10"
        test_content = test_input.split()
        self.test_map_obj.initialize_variable(test_content)

        test_input = "while i < num"
        test_content = test_input.split()

        with self.assertRaises(VariableNotDeclared):
            self.test_map_obj.while_loop(test_content)

        test_input = "while j > i"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)

    def test_bin_one_1(self):
        """
        Testing when only 1 bin_op is present
        """

        test_input = "initialize j = 100"
        test_content = test_input.split()
        self.test_map_obj.initialize_variable(test_content)

        test_input = "while i < 100 and j > 50"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(),
            [
                "int j = 100;\n",
                "int i = 0;\n",
                "while(i < 100 && j > 50)\n",
                "{\n",
            ],
        )

    def test_bin_one_2(self):
        """
        Testing when only 1 bin_op is present
        """

        test_input = "initialize j = 100"
        test_content = test_input.split()
        self.test_map_obj.initialize_variable(test_content)

        test_input = "while i < 100 or j > 50"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(),
            [
                "int j = 100;\n",
                "int i = 0;\n",
                "while(i < 100 || j > 50)\n",
                "{\n",
            ],
        )

    def test_bin_one_3(self):
        """
        Testing when only 1 bin_op is present
        """
        test_input = "while i < 100 or 1"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(),
            [
                "int i = 0;\n",
                "while(i < 100 || 1)\n",
                "{\n",
            ],
        )

    def test_bin_two_1(self):
        """
        Testing when 2 bin_op are present
        """

        test_input = "while i < 100 or 1 and true"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(),
            [
                "int i = 0;\n",
                "while(i < 100 || 1 && true)\n",
                "{\n",
            ],
        )


    def test_bin_two_2(self):
        """
        Testing when 2 bin_op are present
        """
        test_input = "initialize j = 100"
        test_content = test_input.split()
        self.test_map_obj.initialize_variable(test_content)

        test_input = "while i < 100 and j > 50 or 0"
        test_content = test_input.split()
        self.test_map_obj.while_loop(test_content)
        self.assertEqual(
            self.test_map_obj.get_program_list(),
            [
                "int j = 100;\n",
                "int i = 0;\n",
                "while(i < 100 && j > 50 || 0)\n",
                "{\n",
            ],
        )


class TestFor(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj
