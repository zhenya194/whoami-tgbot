# Install dependancies
install:
	pip install aiogram
	pip install pydantic-settings
	pip install python-dotenv

# Create .venv and install dependancies
create_and_install:
	python -m venv .venv
	pip install aiogram
	pip install pydantic-settings
	pip install python-dotenv
