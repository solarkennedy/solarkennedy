.PHONY: README.md clean

README.md:
	python3 build_readme.py | tee README.md

clean:
	rm README.md
