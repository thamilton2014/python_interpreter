from src.Memory import Memory
from src.Parser import Parser

__author__ = 'thamilton'

if __name__ == "__main__":
    try:
        parser = Parser("/Users/thamilton/PycharmProjects/Project_2/test_data/test1.e")
        parser.feature().execute()

        memory = Memory()
        memory.display_memory()
    except (OSError, IOError, ValueError, Exception) as e:
        print(e)