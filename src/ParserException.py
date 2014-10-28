__author__ = 'thamilton'


class ParserException(Exception):
    def __init__(self, message):
        print("[Parser Exception] " + message)