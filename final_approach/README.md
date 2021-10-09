# Usage of Variable Class

### Example Instantiations
```
from variable_mapper import Variable

variable_obj = Variable()

variable_obj.insert_variable(
    var_name: str,
    var_scope: int,     # current_indent
    var_type: VariableTypes = VariableTypes.int,
    var_value=None
)
variable_obj.get_variable(
    var_name: str,
    var_scope: int      # current_indent
)
```

- Can be declared locally

## VariableInfo
- var_name: str,
- var_type: VariableTypes = VariableTypes.int,
- var_value=None,
- fmt_specifier: str = VariableTypes.int.value

## VariableTypes
- int
- char
- float

## Exceptions

- VariableNotDeclared - Only occurs in get_variable and get_variable_list
- VariableAlreadyDeclared - Only occurs in insert_variable