install:
	poetry install

gendiff:
	poetry run gendiff -h

lint:
	poetry run flake8 diff_calc

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl