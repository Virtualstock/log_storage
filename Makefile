setup:
	pipenv install --dev
	pipenv run pip install -e .

test:
	pipenv run coverage run manage.py test --verbosity 2