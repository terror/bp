import os
import shutil
from arg import Arg
from path import File
from parser import Parser

class Handler:
  def __init__(self, args, config):
    self.args = args
    self.config = config

  def run(self):
    arg, data = self.args
    {Arg.USE: self.__use, Arg.INT: self.__use_interactive, Arg.SAVE: self.__save}[arg](*data)

  def __use(self, name, path=None):
    file = File(os.path.join(self.config.store, f'{name}.bp'))
    env = file.env
    path = path or os.getcwd()

    self.__write(env, file, path)

  def __use_interactive(self, name, path=None):
    file = File(os.path.join(self.config.store, f'{name}.bp'))
    env = file.env
    path = path or os.getcwd()

    for var in env:
      inp = input(f'{var}: ')
      env[var] = inp

    self.__write(env, file, path)

  def __save(self, name, path):
    path = os.path.abspath(path)
    shutil.move(path, os.path.join(self.config.store, f'{name}.bp'))

  def __write(self, env, file, path):
    p = f'{env["filename"]}.{env["extension"]}' if env['extension'] else f'{env["filename"]}'
    parser = Parser(env)
    with open(os.path.join(path, p), "w+") as out:
      lines = parser.run(file.content()[file.end:])
      for line in lines:
        out.write(line)
