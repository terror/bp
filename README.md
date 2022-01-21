`bp` is a simple, ~200 loc (excluding tests!) templating engine for commonly
used project files.

#### Installation

```bash
$ curl https://raw.githubusercontent.com/terror/bp/master/bp.py -o /usr/local/bin/bp
$ chmod +x /usr/local/bin/bp
```

#### Usage

```
usage: bp.py [-h] [--use [NAMES]] [--list] [--interactive] [--save [NAMES]]

optional arguments:
  --help, -h                   Show this help message and exit
  --use   -u        [NAMES]    Use a file template.
  --list, -l                   List all available templates.
  --interactive, -i            Be prompted for each variable in the files frontmatter.
  --save  -s        [NAMES]    Save a template in `store`.
```
