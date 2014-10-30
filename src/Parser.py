from src.ArithmeticOperator import ArithmeticOperator
from src.AssignmentStatement import AssignmentStatement
from src.BinaryExpression import BinaryExpression
from src.BooleanExpression import BooleanExpression
from src.Constant import Constant
from src.Id import Id
from src.IfStatement import IfStatement
from src.LexicalAnalyzer import LexicalAnalyzer
from src.LexicalException import LexicalException
from src.LoopStatement import LoopStatement
from src.RelationalOperator import RelationalOperator
from src.TokenType import TokenType
from src.ParserException import ParserException
from src.Feature import Feature
from src.Compound import Compound
from src.PrintStatement import PrintStatement


class Parser:
    # #
    # @param file_name - cannot be null have must have length >= 1
    # @throws ValueError if precondition is not satisfied
    # #
    def __init__(self, file_name):
        if file_name is None and file_name.__len__() == 0:
            raise ValueError("[Parser] invalid file name argument")
        self.lex = LexicalAnalyzer(file_name)

    def feature(self):
        token = self.get_next_token()
        self.match(token, TokenType.FEATURE_TOK)
        id_token = self.get_id()
        token = self.get_next_token()
        self.match(token, TokenType.IS_TOK)
        token = self.get_next_token()
        self.match(token, TokenType.DO_TOK)
        compound = self.get_compound()
        token = self.get_next_token()
        if token.get_token_type() != TokenType.END_TOK:
            raise ParserException("garbage at end of program")
        return Feature(compound)

    def get_compound(self):
        statement = self.get_statement()
        compound = Compound()
        compound.add(statement)
        token = self.get_look_ahead_token()
        while self.is_valid_start(token):
            statement = self.get_statement()
            compound.add(statement)
            token = self.get_look_ahead_token()
        return compound

    def is_valid_start(self, token):
        if token is None:
            raise ParserException("token is null")
        return token.get_token_type() == TokenType.ID_TOK or token.get_token_type() == TokenType.PRINT_TOK or \
               token.get_token_type() == TokenType.IF_TOK or token.get_token_type() == TokenType.FROM_TOK

    def get_statement(self):
        token = self.get_look_ahead_token()
        if token.get_token_type() == TokenType.ID_TOK:
            statement = self.get_assignment_statement()
        elif token.get_token_type() == TokenType.PRINT_TOK:
            statement = self.get_print_statement()
        elif token.get_token_type() == TokenType.IF_TOK:
            statement = self.get_if_statement()
        elif token.get_token_type() == TokenType.FROM_TOK:
            statement = self.get_loop_statement()
        else:
            raise ParserException("statement expected at row "
                                  + str(token.get_row_number()) + " and column " + str(token.get_column_number()))
        return statement

    def get_loop_statement(self):
        token = self.get_next_token()
        self.match(token, TokenType.FROM_TOK)
        statement = self.get_assignment_statement()
        token = self.get_next_token()
        self.match(token, TokenType.UNTIL_TOK)
        boolean_expression = self.get_boolean_expression()
        token = self.get_next_token()
        self.match(token, TokenType.LOOP_TOK)
        compound = self.get_compound()
        token = self.get_next_token()
        self.match(token, TokenType.END_TOK)
        return LoopStatement(statement, boolean_expression, compound)

    def get_print_statement(self):
        token = self.get_next_token()
        self.match(token, TokenType.PRINT_TOK)
        token = self.get_next_token()
        self.match(token, TokenType.LPARAN_TOK)
        expression = self.get_expression()
        token = self.get_next_token()
        self.match(token, TokenType.RPARAN_TOK)
        return PrintStatement(expression)

    def get_id(self):
        token = self.get_next_token()
        self.match(token, TokenType.ID_TOK)
        return Id(token.get_lexeme().lower())

    def match(self, token, token_type):
        if token.get_token_type() != token_type:
            raise ParserException(
                token_type + " expected at row " + token.get_row_number() + " and column " + token.get_column_number())

    def get_assignment_statement(self):
        input_val = self.get_id()
        token = self.get_next_token()
        self.match(token, TokenType.ASSIGN_TOK)
        expression = self.get_expression()
        return AssignmentStatement(input_val.get_char(), expression)

    def get_expression(self):
        token = self.get_look_ahead_token()
        if token.get_token_type() == TokenType.ID_TOK:
            expression = self.get_id()
        elif token.get_token_type() == TokenType.CONST_TOK:
            expression = self.get_literal_integer()
        else:
            operator = self.get_arithmetic_operator()
            expression_1 = self.get_expression()
            expression_2 = self.get_expression()
            expression = BinaryExpression(operator, expression_1, expression_2)
        return expression

    def get_literal_integer(self):
        token = self.get_next_token()
        self.match(token, TokenType.CONST_TOK)
        return Constant(int(token.get_lexeme()))

    def get_arithmetic_operator(self):
        token = self.get_next_token()
        if token.get_token_type() == TokenType.ADD_TOK:
            operator = ArithmeticOperator.ADD_OP
        elif token.get_token_type() == TokenType.SUB_TOK:
            operator = ArithmeticOperator.SUB_OP
        elif token.get_token_type() == TokenType.MUL_TOK:
            operator = ArithmeticOperator.MUL_OP
        elif token.get_token_type() == TokenType.DIV_TOK:
            operator = ArithmeticOperator.DIV_OP
        else:
            raise ParserException("arithmetic operator expected")
        return operator

    def get_if_statement(self):
        token = self.get_next_token()
        self.match(token, TokenType.IF_TOK)
        boolean_expression = self.get_boolean_expression()
        token = self.get_next_token()
        self.match(token, TokenType.THEN_TOK)
        compound_1 = self.get_compound()
        token = self.get_next_token()
        self.match(token, TokenType.ELSE_TOK)
        compound_2 = self.get_compound()
        token = self.get_next_token()
        self.match(token, TokenType.END_TOK)
        return IfStatement(boolean_expression, compound_1, compound_2)

    def get_boolean_expression(self):
        operator = self.get_relational_operator()
        expression_1 = self.get_expression()
        expression_2 = self.get_expression()
        return BooleanExpression(operator, expression_1, expression_2)

    def get_relational_operator(self):
        token = self.get_next_token()
        if token.get_token_type() == TokenType.EQ_TOK:
            operator = RelationalOperator.EQ_OP
        elif token.get_token_type() == TokenType.NE_TOK:
            operator = RelationalOperator.NE_OP
        elif token.get_token_type() == TokenType.GT_TOK:
            operator = RelationalOperator.GT_OP
        elif token.get_token_type() == TokenType.LT_TOK:
            operator = RelationalOperator.LT_OP
        elif token.get_token_type() == TokenType.GE_TOK:
            operator = RelationalOperator.GE_OP
        elif token.get_token_type() == TokenType.LE_TOK:
            operator = RelationalOperator.LE_OP
        else:
            raise ParserException("relational operator expected at row "
                                  + str(token.get_row_number()) + " and column " + token.get_column_number())
        return operator

    def get_next_token(self):
        token = ""
        try:
            token = self.lex.get_next_token()
        except LexicalException as e:
            print(e)
        return token

    def get_look_ahead_token(self):
        token = ""
        try:
            token = self.lex.get_look_ahead_token()
        except LexicalException as e:
            print(e)
        return token




