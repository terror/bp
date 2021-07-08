from .arg import Arg
import os

class InvalidFileFormat(Exception):
  pass

class InvalidOption(Exception):
  pass

class Utils:
  @staticmethod
  def split(l):
    if not l:
      return
    if os.path.exists(l[-1]):
      return (l[:-1], l[-1])
    return (l, None)

  # yapf: disable
  @staticmethod
  def convert(args):
    for pred, res in [
      (lambda args: args.use and args.interactive, (Arg.INT, args.use)),
      (lambda args: args.use, (Arg.USE, args.use)),
      (lambda args: args.save, (Arg.SAVE, args.save)),
      (lambda args: args.list, (Arg.LIST, [None]))
    ]:
      if pred(args):
        return res
    raise InvalidOption("You must pass in a valid option.")
  # yapf: enable
