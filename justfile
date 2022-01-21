default:
  just --list

alias r := run
alias f := fmt

ci: test

run *args:
  python3 bp.py --verbose {{args}}

fmt:
  yapf --in-place --recursive .

test:
  python3 -m unittest test/*.py

compile: fmt
  ./bin/compile
