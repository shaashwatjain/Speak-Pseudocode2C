from enum import Enum, auto
from collections import namedtuple


var_dict_key = namedtuple('var_dict_key', ['var_name', 'var_scope'])


class VariableTypes(Enum):
    int = "%d"
    char = "%c"
    double = "%f"


class VariableInfo:

    def __init__(self,
                 var_name: str,
                 var_type: VariableTypes = VariableTypes.int,
                 var_value=None,
                 fmt_specifier: str = VariableTypes.int.value):
        self.var_name = var_name
        self.var_type = var_type
        self.var_value = var_value
        self.fmt_specifier = fmt_specifier
