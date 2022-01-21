import os
import shutil
import typing as t
from config import Config
from file import File
from parser import Parser

class Handler:
  def __init__(self, args):
    self.args = args
    self.config = Config.load()

  def run(self) -> None:
    for data, func in [
      (self.args.use, self.__use),
      (self.args.list, self.__list),
      (self.args.save, self.__save)
    ]:
      if data:
        func(data)

  def __use(self, filenames: t.List[str]) -> None:
    for filename in filenames:
      file = File(os.path.join(self.config.store, f'{filename}.bp'))

      if self.args.interactive:
        print(f'**** template {filename}.bp ****')
        for var in file.env:
          if not (inp := input(f'{var} ({file.env[var]}): ')):
            continue
          file.env[var] = inp

      self.__write(file, os.getcwd())

  def __list(self, *args) -> None:
    print(*os.listdir(os.path.expanduser(self.config.store)), sep="\n")

  def __save(self, args: t.List[str]) -> None:
    name, path = args
    shutil.move(
      os.path.abspath(path),
      os.path.join(os.path.expanduser(self.config.store), f'{name}.bp')
    )

  def __write(self, file, path) -> None:
    filename = f'{file.env["filename"]}.{file.env["extension"]}' if file.env[
      'extension'] else f'{file.env["filename"]}'
    with open(os.path.join(path, filename), "w+") as out:
      for line in Parser(file.env).run(file.content[file.end:]):
        out.write(line)
