install:
	poetry install

run-server: install
	cd ./backend && poetry run uvicorn app.main:app --reload

run-frontend: install
	poetry run streamlit run frontend/app.py

run: install
	cd ./backend && poetry run uvicorn app.main:app --reload & 
	poetry run streamlit run frontend/app.py
