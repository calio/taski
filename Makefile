init:
	pip install -r requirements.txt

release:
	bumpversion  --current-version `git describe --abbrev=0 --tags` --tag --commit patch setup.py app/__init__.py
	python setup.py bdist_wheel
	-rm dist/*
	twine upload dist/*
	git push --tags

test:
	@pytest

.PHONY: release test
