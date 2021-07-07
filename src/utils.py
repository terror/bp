from arg import Arg

# yapf: disable

class InvalidFileFormat(Exception):
  pass

class InvalidArgument(Exception):
  pass

class Utils:
  def handle(func):
    def wrap(*args, **kwargs):
      parser, args = func(*args, **kwargs)

      if not any([args.use, args.interactive, args.save, args.list]):
        parser.print_help()
        raise InvalidArgument('\nYou must specify an option.')

      if args.interactive and not args.use:
        raise InvalidArgument('Cannot use the `--interactive` flag without `--use`.')

      if args.use and args.save:
        raise InvalidArgument('Cannot use `--use` alongside `--save`.')

      return args
    return wrap

  def split(l):
    if not l:
      return
    if os.path.exists(l[-1]):
      return (l[:-1], l[-1])
    return (l, None)

  def exceptions():
    return (Exception, InvalidFileFormat, InvalidArgument)

  def convert(args):
    for pred, res in [
        (lambda args: args.use and args.interactive, (Arg.INT, args.use)),
        (lambda args: args.use, (Arg.USE, args.use)),
        (lambda args: args.save, (Arg.SAVE, args.save)),
        (lambda args: args.list, (Arg.LIST, [None]))
    ]:
      if pred(args):
        return res

# yapf: enable
