# MIE429 Capstone Repository

The repository contains the code associated with our capstone project. The project is a web application which integrates OpenAI's CLIP model to generate labels for images.

## Installation

Boot your virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
Start the server:
```bash
uvicorn app.main:app --reload
```

Interact with the application at http://localhost:8000

## Testing

There is a test suite setup using Pytest. To run the tests, run the following command:

```bash
pytest
```

## Linting

[Ruff](https://docs.astral.sh/ruff/) is setup to lint the code. To run the linter and fix issues, run the following command:

```bash
ruff check . --fix
```
