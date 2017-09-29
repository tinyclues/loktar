.PHONY: clean-pyc clean-build docs clean

help:
	@echo "all - check style with flake8, check code coverage and run the tests, generate the Sphinx documentation, and runs the server."
	@echo "ci - Command used by the CI"
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "dist - package"
	@echo "install - install the package to the active Python's site-packages"

all: lint coverage docs

ci: lint test

clean: clean-build clean-pyc clean-docker clean-test

clean-docker:
	docker-compose kill
	docker-compose rm --all -fv

clean-build:
	rm -rf ./src/build/
	rm -rf ./src/dist/
	rm -rf ./src/*egg*/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*.~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean-test:
	rm -f ./src/.coverage
	rm -fr ./src/htmlcov/
	rm -rf ./src/.cache
	rm -rf ./src/coverage.xml

lint:
	docker-compose run --no-deps loktar flake8 loktar

test: unit-test integration-test

unit-test:
	docker-compose run --no-deps loktar py.test -s tests/unit

integration-test:
	docker-compose run loktar py.test -s tests/integration


coverage:
	docker-compose run --no-deps loktar py.test -s --cov=loktar --cov-report html --cov-report xml --cov-config .coveragerc tests/unit

docs:
	# rm -f docs/loktar.rst
	# rm -f docs/modules.rst
	# sphinx-apidoc -o docs/ loktar -e
	# $(MAKE) -C docs clean
	# $(MAKE) -C docs html
	@echo 'to do gen doc'

register: clean build
	docker-compose -f docker-compose.yml -f docker-compose-release.yml run --no-deps loktar python setup.py register -r tinypypi

release: clean build
	docker-compose -f docker-compose.yml -f docker-compose-release.yml run --no-deps loktar python setup.py bdist_wheel upload -r tinypypi

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel

install: clean
	python setup.py install

shell:
	docker-compose run --no-deps loktar bash

shell-with-services:
	docker-compose run loktar bash

build:
	docker-compose build
