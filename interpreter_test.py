import unittest
from nodes import *
from interpreter import Interpreter
from values import Number

class TestInterpreter(unittest.TestCase):

    def test_numbers(self):
        value = Interpreter().visit(NumberNode(12.34))
        self.assertEqual(value, Number(12.34))

    def test_add(self):
        value = Interpreter().visit(AddNode(NumberNode(27), NumberNode(14)))
        self.assertEqual(value, Number(41))

    def test_subtract(self):
        value = Interpreter().visit(SubtractNode(NumberNode(27), NumberNode(14)))
        self.assertEqual(value, Number(13))

    def test_multiply(self):
        value = Interpreter().visit(MultiplyNode(NumberNode(27), NumberNode(14)))
        self.assertEqual(value, Number(378))
    
    def test_divide(self):
        value = Interpreter().visit(DivideNode(NumberNode(27), NumberNode(14)))
        self.assertAlmostEqual(value.value, 1.92857, 5)

    def test_divide_zero(self):
        with self.assertRaises(Exception):
            Interpreter().visit(DivideNode(NumberNode(27), NumberNode(0)))
    
    def test_all(self):
        value = Interpreter().visit(
            AddNode(
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
            )
        )
        self.assertAlmostEqual(value.value, -933.53333, 5)

    
