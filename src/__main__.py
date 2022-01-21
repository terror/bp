import argparse
import sys
import traceback
from arguments import Arguments

def main(args):
  try:
    args.run()
  except Exception as error:
    if args.verbose:
      traceback.print_exc()
    print(f'error: {str(error)}', file=sys.stderr)

if __name__ == '__main__':
  main(Arguments.from_args())
