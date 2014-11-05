from src.LexicalException import LexicalException
from src.Memory import Memory
from src.Parser import Parser
from src.ParserException import ParserException

__author__ = 'thamilton'

if __name__ == "__main__":
    try:
        parser = Parser("/Users/thamilton/PycharmProjects/Project_2/test_data/test3.e")
        parser.feature().execute()
        memory = Memory()
        memory.display_memory()
    except (OSError, IOError, ValueError, Exception, LexicalException, ParserException) as e:
        print(e)