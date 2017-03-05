release:
	bumpversion  --current-version `git describe --abbrev=0 --tags` --tag --commit patch setup.py app/__init__.py
	python setup.py register
	python setup.py sdist upload

test:
	@pytest tests/test_base.py

test_account:
	python create_test_account.py

.PHONY: release test test_account
