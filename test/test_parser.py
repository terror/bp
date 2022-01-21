import sys
import unittest
from parameterized import parameterized_class
from src.parser import Parser

@parameterized_class(
  ('line', 'expected_vars', 'expected_line'),
  [
    ('{%a%}{%b%}', ['a', 'b'], '12'),
    ('xx{%c%}+{%b%}wwwww{%a%}', ['c', 'b', 'a'], 'xx3+2wwwww1'),
    ('{%ax%}{%b%}', ['ax', 'b'], '{%ax%}2'),
    ('{%ax%}{%bx%}', ['ax', 'bx'], '{%ax%}{%bx%}'),
  ]
)
class TestParser(unittest.TestCase):
  def setUp(self):
    self.parser = Parser({'a': 1, 'b': 2, 'c': 3})

  def test_vars(self):
    self.assertEqual(self.parser.vars(self.line), self.expected_vars)

  def test_parse_line(self):
    self.assertEqual(self.parser.parse_line(self.line), self.expected_line)
