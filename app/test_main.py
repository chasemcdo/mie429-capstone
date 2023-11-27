from fastapi.testclient import TestClient
from os import path

from .main import app

client = TestClient(app)

def test_label():
    base_path = path.dirname(__file__)
    tip_path = path.join(base_path, '__test__', 'tip.png')

    with open(tip_path, 'rb') as tip_file:
        files = {
            'file': (tip_path, tip_file, 'image/png')
        }
        response = client.post("/clip", files=files)
    
    assert response.status_code == 200
    assert "message" in response.json()

def test_generate_cache():
    base_path = path.dirname(__file__)
    tip_path = path.join(base_path, '__test__', 'tip.png')

    with open(tip_path, 'rb') as tip_file:
        files = {
            'files': (tip_path, tip_file, 'image/png')
        }
        response = client.post("/clip/cache", data={"labels": ["tip"]}, files=files)
    
    assert response.status_code == 200
    assert "message" in response.json()

def test_hello_world():
    response = client.post("/world")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
