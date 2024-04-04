install:
	poetry install

run-server: install
	cd ./backend && poetry run uvicorn app.main:app --reload

run-frontend:
	poetry run streamlit run frontend/app.py

run:
	cd ./backend && poetry run uvicorn app.main:app --reload & 
	poetry run streamlit run frontend/app.py
