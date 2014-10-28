from src.Expression import Expression

__author__ = 'thamilton'


class Constant(Expression):
    def __init__(self, value):
        super().__init__()
        if value is None:
            raise ValueError("[Constant] null value argument")
        self.value = value

    def evaluate(self):
        return self.value
