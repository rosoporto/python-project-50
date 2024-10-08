install:
	poetry install

gendiff:
	poetry run gendiff -h

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -s

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl