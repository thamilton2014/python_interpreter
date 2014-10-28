__author__ = 'thamilton'


class LoopStatement(object):
    # #
    # @param statement - cannot be null
    # @param boolean_expression - cannot be null
    # @param compound - cannot be null
    # @throws ValueError if any precondition is null
    # #
    def __init__(self, statement, boolean_expression, compound):
        if statement is None:
            raise ValueError("[Loop Statement] null statement argument")
        if boolean_expression is None:
            raise ValueError("[Loop Statement] null boolean_expression argument")
        if compound is None:
            raise ValueError("[Loop Statement] null compound argument")
        self.statement = statement
        self.boolean_expression = boolean_expression
        self.compound = compound

    def execute(self):
        self.statement.execute()
        while not self.boolean_expression.evaluate():
            self.compound.execute()
