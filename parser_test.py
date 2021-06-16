import unittest
from tokens import Token, TokenType
from parser_ import Parser
from nodes import *

class TestParser(unittest.TestCase):

    def test_empty(self):
        tokens = []
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def test_numbers(self):
        tokens = [Token(TokenType.NUMBER, 12.34)]
        node = Parser(tokens).parse()
        self.assertEqual(node, NumberNode(12.34))

    def test_numbers(self):
        tokens = [Token(TokenType.NUMBER, 12.34)]
        node = Parser(tokens).parse()
        self.assertEqual(node, NumberNode(12.34))
    
    def test_plus(self):
        tokens = [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 34),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(NumberNode(12), NumberNode(34)))

    def test_subtract(self):
        tokens = [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 34),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, SubtractNode(NumberNode(12), NumberNode(34)))

    def test_multiply(self):
        tokens = [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 34),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, MultiplyNode(NumberNode(12), NumberNode(34)))

    def test_divide(self):
        tokens = [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 34),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, DivideNode(NumberNode(12), NumberNode(34)))

    def test_all(self):
        tokens =[
            Token(TokenType.NUMBER, 43),
            Token(TokenType.PLUS),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 26),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 75),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 98),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 10),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(
            NumberNode(43), 
            MultiplyNode(
                SubtractNode(
                    DivideNode(
                        NumberNode(26), 
                        NumberNode(75),
                    ), 
                    NumberNode(98),
                ), 
                NumberNode(10),
            ),
        ))
