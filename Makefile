help:
	@echo '     init'
	@echo '         install pipenv and all project dependencies'
	@echo '     test'
	@echo '         run all tests'

init:
	@echo 'Install project dependencies'
	pip install pipenv
	pipenv install

test:
	@echo 'Running all tests'
	pipenv run pytest --cov=training_tracker
