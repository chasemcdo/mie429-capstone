# MIE429 Capstone Repository

The repository contains the code associated with our capstone project. The project is a web application which integrates [OpenAI's CLIP](https://openai.com/research/clip) to generate labels for images.

## Setup

Checkout the Tip Sub-Module for access to TIP Python classes:
```bash
git submodule update --recursive --remote
```

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

Interact with the application at http://localhost:8000/{path}

## Docker Images
Pre-build `linux/amd64` images for this repository are published to our [public docker hub repository](https://hub.docker.com/r/chasemcdougall/capstone-api).

## Documentation
FastAPI provides an interactive documentation page at http://localhost:8000/docs

## Testing

There is a test suite setup using [Pytest](https://docs.pytest.org). To run the tests, run the following command:

```bash
pytest
```

## Linting

[Ruff](https://docs.astral.sh/ruff/) is setup to lint the code. To run the linter and fix issues, run the following command:

```bash
ruff check app --fix
```
