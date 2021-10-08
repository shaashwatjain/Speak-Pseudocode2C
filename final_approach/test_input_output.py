import unittest
from mapper import Mapper
from variable_mapper import Singleton, Variable


class TestDeclare(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map_obj = Mapper()

    def tearDown(self) -> None:
        del self.test_map_obj

    def test_declare_integer(self):
        """
        Test declaring integer in case where it is mentioned explicitly.
        """
        test_input = "declare new_variable integer"
        test_content = test_input.split(" ")
        self.test_map_obj.declare_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["int new_variable;\n"])

    def test_declare_character(self):
        """
        Test declaring integer in case where it is mentioned explicitly.
        """
        test_input = "declare new_variable character"
        test_content = test_input.split(" ")
        self.test_map_obj.declare_variable(test_content)
        self.assertEqual(self.test_map_obj.get_program_list(), ["char new_variable;\n"])
