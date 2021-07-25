help:
	@python3.7 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

env-create: ## (re)create a development environment using tox
	tox -e openaltrainer --recreate
	@echo -e "\r\nYou can activate the environment with:\r\n\r\n$$ source ./.tox/openaltrainer/bin/activate\r\n"

env-compile: ## compile requirements.txt / requirements-dev.txt using pip-tools
	pip-compile --no-header --no-emit-trusted-host --output-file requirements.txt requirements.in

clean: ## clean
	@rm -fr build/
	
clean-python:
	@rm -fr .eggs/
	@find . ! -path './.tox/*' -name '*.egg-info' -exec rm -fr {} +
	@find . ! -path './.tox/*' -name '*.egg' -exec rm -f {} +
	@find . ! -path './.tox/*' -name '*.pyc' -exec rm -f {} +
	@find . ! -path './.tox/*' -name '*.pyo' -exec rm -f {} +
	@find . ! -path './.tox/*' -name '*~' -exec rm -f {} +
	@find . ! -path './.tox/*' -name '__pycache__' -exec rm -fr {} +

clean-all: clean-python clean ## clean all including tox
	@rm requirements.txt
	@rm -fr .tox/