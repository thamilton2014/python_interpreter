class Token:

    def __init__(self, row_number, lexeme, token_type):
        # if row_number is None or column_number is None:
        if row_number is None:
            raise TypeError("[Token] invalid column/row number argument")
        if lexeme is None:
            raise TypeError("[Token] invalid lexeme argument")
        if token_type is None:
            raise TypeError("[Token] null TokenType argument")
        self.row_number = row_number
        # self.column_number = column_number
        self.lexeme = lexeme
        self.token_type = token_type

    def get_row_number(self):
        return self.row_number

    # def get_column_number(self):
    #     return self.column_number

    def get_lexeme(self):
        return self.lexeme

    def get_token_type(self):
        return self.token_type