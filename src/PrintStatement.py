from src.Statement import Statement

__author__ = 'thamilton'


class PrintStatement(Statement):
    # #
    # @param expression - cannot be null
    # @throws ValueError if expression is null
    # #
    def __init__(self, expression):
        super().__init__()
        if expression is None:
            raise ValueError("[PrintStatement] null expression argument")
        self.expression = expression

    def execute(self):
        print("[Print Statement] " + str(self.expression.evaluate()))
