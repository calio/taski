init:
	pip install -r requirements.txt

release:
	bumpversion  --current-version `git describe --abbrev=0 --tags` --tag --commit patch setup.py app/__init__.py
	python setup.py bdist_wheel
	twine upload dist/*
	-rm dist/*
	-rm build/*
	git push --tags

test:
	@pytest

clean:
	-rm -r build dist app/*.pyc

.PHONY: init release test
