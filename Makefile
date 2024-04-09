install:
	poetry install

gendiff:
	poetry run gendiff -h

lint:
	poetry run flake8 diff_calc