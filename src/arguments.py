import argparse
import dataclasses
import typing as t
from handler import Handler

@dataclasses.dataclass
class Arguments:
  use: t.List[str]
  list: bool
  interactive: bool
  save: t.List[str]
  verbose: bool

  @staticmethod
  def from_args():
    parser = argparse.ArgumentParser(prog="bp")

    parser.add_argument(
      '--use',
      '-u',
      nargs='+',
      required=False,
      help='Use a file template in `store`.'
    )

    parser.add_argument(
      '--list',
      '-l',
      required=False,
      action='store_true',
      help='List all available templates.'
    )

    parser.add_argument(
      '--interactive',
      '-i',
      required=False,
      action="store_true",
      help='Be prompted for variables in the files frontmatter.'
    )

    parser.add_argument(
      '--save',
      '-s',
      nargs='+',
      required=False,
      help='Save a template in `store`.'
    )

    parser.add_argument(
      '--verbose',
      '-v',
      required=False,
      action="store_true",
      help='Add tracebacks to error messages.'
    )

    return Arguments(**vars(parser.parse_args()))

  def run(self):
    Handler(self).run()
