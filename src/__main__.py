import argparse
import sys
import traceback
from .utils import *
from .handler import Handler
from .config import Config

def cli():
  parser = argparse.ArgumentParser()
  parser.add_argument('--use', '-u', nargs='+', help='Use a file template.')
  parser.add_argument('--list', '-l', action='store_true', help='List all available templates.')
  parser.add_argument('--interactive', '-i', action="store_true", help='Be prompted for variable in frontmatter.')
  parser.add_argument('--save', '-s', nargs='+', help='Save a template in `store`.')
  return parser.parse_args()

def main(args, config):
  Handler(Utils.convert(args), config).run()

if __name__ == '__main__':
  try:
    main(cli(), Config.load())
  except (Exception, InvalidFileFormat, InvalidOption) as error:
    print(error)
    # traceback.print_exc()
    sys.exit(1)
