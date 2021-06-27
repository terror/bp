`bp` is a simple, ~200 loc (excluding tests!) templating engine for commonly used project files.

#### Installation

```bash
$ curl https://raw.githubusercontent.com/terror/bp/master/bp.py -o /usr/local/bin/bp
$ chmod +x /usr/local/bin/bp
```

#### Usage

```
usage: bp.py [-h] [--use NAME [...]] [--interactive] [--save NAME PATH]

optional arguments:
  -h, --help            show this help message and exit
  --use -u NAME [...]   Use a file template.
  --interactive, -i     Be prompted for each variable that resides in the files frontmatter.
  --save -s NAME PATH   Save a template in the local storage location.
```
