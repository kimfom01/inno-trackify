help:             ## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep

install:          ## Install the project in dev mode.
	poetry install --no-root

create-db: install
	sqlite3 inno-trackify.db < ./migrations/init.sql

run-server: install create-db
	cd ./backend && poetry run uvicorn app.main:app --reload

run-frontend: install create-db
	poetry run streamlit run frontend/app.py

run: install create-db
	cd ./backend && poetry run uvicorn app.main:app --reload & 
	poetry run streamlit run frontend/app.py

lint: install ## Run pep8, black linters.
	flake8 backend/ frontend/ || true
	black -l 79 --check backend/ || true
	black -l 79 --check frontend/ || true
