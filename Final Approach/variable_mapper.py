from userDefinedTypes import VariableTypes, var_dict_key, VariableInfo
from typing import List
from exceptions import VariableNotDeclared, VariableAlreadyDeclared


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Variable(object):
    __metaclass__ = Singleton
    __variable_map = dict()

    def insert_variable(self,
                        var_name: str,
                        var_scope: int,  # current_indent
                        var_type: VariableTypes = VariableTypes.int,
                        var_value=None):
        key = var_dict_key(var_name, var_scope)
        if key in self.__variable_map:
            raise VariableAlreadyDeclared
        else:
            mapped_variable_info_object = VariableInfo(var_name, var_type, var_value, var_type.value)
            self.__variable_map[key] = mapped_variable_info_object

    def exit_scope(self,
                   var_scope: int):
        for key in self.__variable_map.keys():
            if key[1] == var_scope:
                del self.__variable_map[key]

    def get_variable(self,
                     var_name: str,
                     var_scope: int) -> VariableInfo:
        current_scope = var_scope
        while current_scope >= 0:
            key = var_dict_key(var_name, current_scope)
            if key in self.__variable_map:
                return self.__variable_map[key]
            else:
                current_scope -= 1
        raise VariableNotDeclared

    def get_variable_list(self,
                          list_of_names: list,
                          scope: int) -> List[VariableInfo]:
        list_of_variable_info: List[VariableInfo] = []
        for name in list_of_names:
            variable_info_obj = self.get_variable(name, scope)
            list_of_variable_info.append(variable_info_obj)
        return list_of_variable_info
