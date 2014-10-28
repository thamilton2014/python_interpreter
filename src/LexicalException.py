__author__ = 'thamilton'


class LexicalException(Exception):
    def __init__(self, message):
        print("[Lexical Exception] " + message)