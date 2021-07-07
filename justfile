default:
  just --list

ci: test

fmt:
  yapf --in-place --recursive **/*.py

test:
  python3 -m unittest test/*.py

compile: fmt
  ./bin/compile
