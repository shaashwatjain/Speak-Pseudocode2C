from userDefinedTypes import VariableTypes, var_dict_key, VariableInfo
from typing import List
from exceptions import VariableNotDeclared, VariableAlreadyDeclared


class Variable:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Variable.__instance is None:
            Variable()
        return Variable.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Variable.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Variable.__instance = self

    __variable_map = dict()

    def insert_variable(self,
                        var_name: str,
                        var_scope: int,
                        var_type: VariableTypes = VariableTypes.int,
                        var_value=None):
        key = var_dict_key(var_name, var_scope)
        if key in self.__variable_map:
            raise VariableAlreadyDeclared
        else:
            mapped_variable_info_object = VariableInfo(var_name, var_type, var_value, var_type.value)
            self.__variable_map[key] = mapped_variable_info_object

    def get_variable(self,
                     var_name: str,
                     var_scope: int) -> VariableInfo:
        current_scope = var_scope
        while current_scope > 0:
            key = var_dict_key(var_name, current_scope)
            if key in self.__variable_map:
                return self.__variable_map[key]
            else:
                current_scope -= 1
        raise VariableNotDeclared

    def get_variable_list(self,
                          list_of_name_and_scopes: list) -> List[VariableInfo]:
        list_of_variable_info: List[VariableInfo] = []
        for name, scope in list_of_name_and_scopes:
            variable_info_obj = self.get_variable(name, scope)
            list_of_variable_info.append(variable_info_obj)
        return list_of_variable_info
