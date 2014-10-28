from src.LexicalException import LexicalException
from src.TokenType import TokenType
from src.Token import Token

__author__ = 'thamilton'


class LexicalAnalyzer(object):
    # #
    # @param file_name - cannot be null and must have positive length
    # @throws ValueError if precondition is not satisfied
    # #
    def __init__(self, file_name):
        if file_name is None and file_name.__len__() == 0:
            raise ValueError("invalid file name argument")
        data_file = open(file_name, "r")
        input_data = data_file.read()
        line_number = 1
        column_number = 1
        buffer_data = ""
        self.token_list = []
        for word in input_data.split():
            if word.isspace():
                buffer_data += ""
            else:
                token_type = self.get_token_type(line_number, column_number, word)
                self.token_list.append(Token(line_number + 1, column_number + 1, word, token_type))
            if word is '\n':
                line_number += 1
                column_number += 0
            column_number += 1
        data_file.close()
        self.token_list.append(Token(line_number, 1, "EOS", TokenType.EOS_TOK))

    # #
    # @param lexeme         = String value
    # @param line_number    = Integer value of line number
    # @param column_number  = Integer value of column number
    # #
    def get_token_type(self, line_number, column_number, lexeme):
        if lexeme.__eq__("feature"):
            tok_type = TokenType.FEATURE_TOK
        elif lexeme.isalpha() and lexeme.__len__() == 1:
            tok_type = TokenType.ID_TOK
        elif lexeme.__eq__("is"):
            tok_type = TokenType.IS_TOK
        elif lexeme.__eq__("do"):
            tok_type = TokenType.DO_TOK
        elif lexeme.__eq__(":="):
            tok_type = TokenType.ASSIGN_TOK
        elif lexeme.isdigit():
            tok_type = TokenType.CONST_TOK
        elif lexeme.__eq__("print"):
            tok_type = TokenType.PRINT_TOK
        elif lexeme.__eq__("("):
            tok_type = TokenType.LPARAN_TOK
        elif lexeme.__eq__(")"):
            tok_type = TokenType.RPARAN_TOK
        elif lexeme.__eq__("end"):
            tok_type = TokenType.END_TOK
        elif lexeme.__eq__("if"):
            tok_type = TokenType.IF_TOK
        elif lexeme.__eq__(">"):
            tok_type = TokenType.GT_TOK
        elif lexeme.__eq__(">="):
            tok_type = TokenType.GE_TOK
        elif lexeme.__eq__("<"):
            tok_type = TokenType.LT_TOK
        elif lexeme.__eq__("<="):
            tok_type = TokenType.LE_TOK
        elif lexeme.__eq__("="):
            tok_type = TokenType.EQ_TOK
        elif lexeme.__eq__("/="):
            tok_type = TokenType.NE_TOK
        elif lexeme.__eq__("then"):
            tok_type = TokenType.THEN_TOK
        elif lexeme.__eq__("else"):
            tok_type = TokenType.ELSE_TOK
        elif lexeme.__eq__("from"):
            tok_type = TokenType.FROM_TOK
        elif lexeme.__eq__("until"):
            tok_type = TokenType.UNTIL_TOK
        elif lexeme.__eq__("loop"):
            tok_type = TokenType.LOOP_TOK
        elif lexeme.__eq__("+"):
            tok_type = TokenType.ADD_TOK
        elif lexeme.__eq__("-"):
            tok_type = TokenType.SUB_TOK
        elif lexeme.__eq__("*"):
            tok_type = TokenType.MUL_TOK
        elif lexeme.__eq__("/"):
            tok_type = TokenType.DIV_TOK
        else:
            raise LexicalException("invalid lexeme at row "
                                   + str(line_number) + " and column " + str(column_number + 1))
        return tok_type

    def get_look_ahead_token(self):
        if not self.token_list:
            raise LexicalException("No more tokens")
        return self.token_list[0]

    def get_next_token(self):
        if self.token_list is None or len(self.token_list) == 0:
            raise LexicalException("No more tokens")
        return self.token_list.pop(0)

    def get_lexeme(self, word):
        return word

    def is_valid_identifier(self):
        pass