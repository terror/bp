import unittest, sys
from parameterized import parameterized_class
from bp import Parser


# yapf: disable
@parameterized_class(('line', 'expected_vars', 'expected_parsed_line'), [
  ('{%a%}{%b%}', ['a', 'b'], '12'),
  ('xxx{%c%}+{%b%}wwwww{%a%}', ['c', 'b', 'a'], 'xxx3+2wwwww1'),
  ('{%ax%}{%b%}', ['ax', 'b'], '{%ax%}2'),
  ('{%ax%}{%bx%}', ['ax', 'bx'], '{%ax%}{%bx%}'),
  # TODO: this behaviour should work ('{%{%a%}{%b%}%}', ['{%a%}{%b%}', 'a', 'b'], '{%12%}')
])
# yapf: enable
class TestParser(unittest.TestCase):
  def setUp(self):
    self.parser = Parser({'a': 1, 'b': 2, 'c': 3})

  def test_get_vars(self):
    self.assertEqual(self.parser.get_vars(self.line), self.expected_vars)

  def test_parse_line(self):
    self.assertEqual(self.parser.parse_line(self.line), self.expected_parsed_line)
