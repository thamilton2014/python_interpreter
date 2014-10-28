from src.RelationalOperator import RelationalOperator

__author__ = 'thamilton'


class BooleanExpression(object):
    # #
    # @param operator - cannot be null
    # @param expression_1 - cannot be null
    # @param expression_2 - cannot be null
    # @throws ValueError if any precondition is null
    # #
    def __init__(self, operator, expression_1, expression_2):
        if operator is None:
            raise ValueError("[Boolean Expression] null operator argument")
        if expression_1 is None or expression_2 is None:
            raise ValueError("[Boolean Expression] null expression argument")
        self.operator = operator
        self.expression_1 = expression_1
        self.expression_2 = expression_2

    def evaluate(self):
        if self.operator == RelationalOperator.LE_OP:
            value = self.expression_1.evaluate() <= self.expression_2.evaluate()
        elif self.operator == RelationalOperator.LT_OP:
            value = self.expression_1.evaluate() < self.expression_2.evaluate()
        elif self.operator == RelationalOperator.GE_OP:
            value = self.expression_1.evaluate() >= self.expression_2.evaluate()
        elif self.operator == RelationalOperator.GT_OP:
            value = self.expression_1.evaluate() > self.expression_2.evaluate()
        elif self.operator == RelationalOperator.EQ_OP:
            value = self.expression_1.evaluate() == self.expression_2.evaluate()
        else:
            value = self.expression_1.evaluate() != self.expression_2.evaluate()
        return value
