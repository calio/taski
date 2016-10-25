all:
	bumpversion  --current-version `git describe --abbrev=0 --tags` --tag --commit patch setup.py
	python setup.py register
	python setup.py sdist upload
