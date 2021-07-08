`bp` is a simple, ~200 loc (excluding tests!) templating engine for commonly used project files.

#### Installation

```bash
$ curl https://raw.githubusercontent.com/terror/bp/master/bp.py -o /usr/local/bin/bp
$ chmod +x /usr/local/bin/bp
```

#### Usage

```
usage: bp.py [-h] [--use [NAMES] PATH] [--list] [--interactive] [--save NAME PATH]

optional arguments:
  -h, --help            show this help message and exit
  --use -u [NAMES] PATH Use a file template.
  --save -s NAME PATH   Save a template in `store`.
  --list, -l            List all available templates.
  --interactive, -i     Be prompted for each variable in the files frontmatter.
```
