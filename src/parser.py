import re

class Parser:
  def __init__(self, env):
    self.env = env

  def run(self, lines):
    for i in range(len(lines)):
      lines[i] = self.parse_line(lines[i])
    return lines

  def get_vars(self, line):
    return re.findall("{%(.*?)%}", line)

  def parse_line(self, line):
    # some cases:
    # a: 1; b: 2
    # {%a%} + {%b%} -> 1 + 2
    # ({%a%}{%b%})  -> (12)
    vars = self.get_vars(line)
    if not vars:
      return line
    for v in vars:
      if v not in self.env:
        continue
      line = re.sub("{%" + v + "%}", str(self.env[v]), line)
    return line
