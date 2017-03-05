release:
	bumpversion  --current-version `git describe --abbrev=0 --tags` --tag --commit patch setup.py app/__init__.py
	python setup.py register
	python setup.py sdist upload

test:
	@pytest

.PHONY: release test
