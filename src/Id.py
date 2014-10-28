from src.Expression import Expression
from src.Memory import Memory

__author__ = 'thamilton'


class Id(Expression):
    def __init__(self, character):
        super().__init__()
        if character is None:
            raise ValueError("[Id] character is null")
        self.character = character

    def evaluate(self):
        memory = Memory()
        return memory.fetch(self.character)

    def get_char(self):
        return self.character
