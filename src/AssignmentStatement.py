from src.Memory import Memory
from src.Statement import Statement

__author__ = 'thamilton'


class AssignmentStatement(Statement):
    # #
    # @param input_val - cannot be null
    # @param expression - cannot be null
    # @throws ValueError if either argument is null
    # #
    def __init__(self, input_val, expression):
        super().__init__()
        if input_val is None:
            raise ValueError("[Assignment Statement] null input_val argument")
        if expression is None:
            raise ValueError("[Assignment Statement] null Expression argument")
        self.input_val = input_val
        self.expression = expression

    def execute(self):
        memory = Memory()
        memory.store(self.input_val, self.expression.evaluate())
