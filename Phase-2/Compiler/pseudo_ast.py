class Assignment:
    __slots__ = ("op", "dType", "lvalue", "rvalue")

    def __init__(self, op, dType, lvalue, rvalue):
        self.op = op
        self.lvalue = lvalue
        self.rvalue = rvalue
        self.dType = dType

    def children(self):
        nodelist = (self.lvalue, self.rvalue)
        return nodelist


class BinaryOp:
    __slots__ = ("op", "left", "right", "dType", "length")

    def __init__(self, op, left, right, dType, length):
        self.op = op
        self.left = left
        self.right = right
        self.dType = dType
        self.length = length

    def children(self):
        nodelist = (self.left, self.right)
        return nodelist


class Constant:
    __slots__ = ("dType", "value", "length")

    def __init__(self, dType, value, length):
        self.dType = dType
        self.value = value
        self.length = length

    def children(self):
        return None


class Variable:
    __slots__ = ("dType", "name", "length")

    def __init__(self, dType, name, length):
        self.name = name
        self.dType = dType
        self.length = length

    def children(self):
        return None


class Output:
    __slots__ = "data"

    def __init__(self, data):
        self.data = data

    def children(self):
        return self.data


class Input:
    __slots__ = ("variable", "dType")

    def __init__(self, variable, dType):
        self.variable = variable
        self.dType = dType

    def children(self):
        return None


class If:
    __slots__ = ("condition", "if_true", "if_false")

    def __init__(self, condition, if_true, if_false):
        self.condition = condition
        self.if_true = if_true
        self.if_false = if_false

    def children(self):
        return (self.condition, self.if_true, self.if_false)


class While:
    __slots__ = ("condition", "body")

    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def children(self):
        return (self.condition, self.body)


class For:
    __slots__ = ("assignment", "final", "body")

    def __init__(self, assignment, final, body):
        self.assignment = assignment
        self.final = final
        self.body = body

    def children(self):
        return (self.assignment, self.final, self.body)
