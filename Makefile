setup:
	pipenv install --dev
	pipenv run pip install -e .

test:
	pipenv run coverage run manage.py test --verbosity 2

release:
	python setup.py sdist bdist_wheel
	twine upload dist/*
