![Flake8](https://github.com/Q-Tify/inno-trackify/actions/workflows/lint.yml/flake8-badge.svg?branch=actions)
# inno-trackify

To install the dependencies:
```
poetry install
```

To run the backend:
```
poetry run uvicorn app.main:app --reload
```

To run the frontend:
```
poetry run streamlit run frontend/app.py
```
