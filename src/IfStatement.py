from src.Statement import Statement

__author__ = 'thamilton'


class IfStatement(Statement):
    # #
    # @param boolean_expression - cannot be null
    # @param compound_1 - cannot be null
    # @param compound_2 - cannot be null
    # @throws ValueError if any precondition is null
    # #
    def __init__(self, boolean_expression, compound_1, compound_2):
        super().__init__()
        if boolean_expression is None:
            raise ValueError("[If Statement] null boolean_expression argument")
        if compound_1 is None or compound_2 is None:
            raise ValueError("[If Statement] null compound argument")
        self.boolean_expression = boolean_expression
        self.compound_1 = compound_1
        self.compound_2 = compound_2

    def execute(self):
        if self.boolean_expression.evaluate():
            self.compound_1.execute()
        else:
            self.compound_2.execute()
