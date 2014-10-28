__author__ = 'thamilton'


class Compound(object):
    # #
    # @param
    # @description - create statement list
    # #
    def __init__(self):
        self.statements = []

    # #
    # @param statement - cannot be null
    # @throws ValueError - if statement is null
    # #
    def add(self, statement):
        if statement is None:
            raise ValueError("[Compound] null statement argument")
        self.statements.append(statement)

    def execute(self):
        for statement in self.statements:
            statement.execute()
