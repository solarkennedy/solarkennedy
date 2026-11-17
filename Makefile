.PHONY: README.md clean deploy

README.md:
	python3 build_readme.py | tee README.md

clean:
	rm README.md

# Regenerate the README, commit it if it changed, and push — the local
# stand-in for the old GitHub Actions "Build README" workflow.
deploy: README.md
	git diff --quiet README.md || git commit -am "Updated README"
	git push