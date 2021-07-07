default:
  just --list

ci: fmt test

fmt:
  yapf --in-place --recursive **/*.py

test:
  python3 -m unittest test/*.py

compile: fmt
  ./bin/compile
