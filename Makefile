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
	flake8 backend/ frontend/ || true
	black -l 79 --check backend/ || true
	black -l 79 --check frontend/ || true
