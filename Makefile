setup:
	pipenv install -r requirements.txt --python=2.7
	pipenv run pip install -e .

test:
	pipenv run coverage run manage.py test --verbosity 2