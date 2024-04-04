.ONESHELL:
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")

help:             ## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep

install:          ## Install the project in dev mode.
	poetry install --no-root

run-server: install
	cd ./backend && poetry run uvicorn app.main:app --reload

run-frontend: install
	poetry run streamlit run frontend/app.py

run: install
	cd ./backend && poetry run uvicorn app.main:app --reload & 
	poetry run streamlit run frontend/app.py

lint: install ## Run pep8, black linters.
	@$(ENV_PREFIX)flake8 backend/ frontend/ || true
	@$(ENV_PREFIX)black -l 79 --check backend/ || true
	@$(ENV_PREFIX)black -l 79 --check frontend/ || true
