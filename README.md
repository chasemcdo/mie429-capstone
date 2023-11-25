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
uvicorn main:app --reload
```

Interact with the application at http://localhost:8000
