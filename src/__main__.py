import argparse
import sys
import traceback
from utils import Utils
from handler import Handler
from config import Config

@Utils.handle
def cli():
  parser = argparse.ArgumentParser()
  parser.add_argument('--use', '-u', nargs='+', help='Use a file template.')
  parser.add_argument('--list', '-l', action='store_true', help='List all available templates.')
  parser.add_argument('--interactive', '-i', action="store_true", help='Be prompted for variable in frontmatter.')
  parser.add_argument('--save', '-s', nargs='+', help='Save a template in `store`.')
  return (parser, parser.parse_args())

def main(args, config):
  Handler(Utils.convert(args), config).run()

if __name__ == '__main__':
  try:
    main(cli(), Config.load())
  except Utils.exceptions() as error:
    print(error)
    # traceback.print_exc()
    sys.exit(1)
