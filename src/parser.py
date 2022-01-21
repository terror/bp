import re

class Parser:
  def __init__(self, env):
    self.env = env

  def run(self, lines):
    return list(map(lambda line: self.parse_line(line), lines))

  def vars(self, line):
    return re.findall('{%(.*?)%}', line)

  def parse_line(self, line):
    vars = self.vars(line)
    if not vars:
      return line
    for var in vars:
      if var not in self.env:
        continue
      line = re.sub('{%' + var + '%}', str(self.env[var]), line)
    return line
