from fastapi.testclient import TestClient
from fastapi import UploadFile
from os import path

from .main import app

client = TestClient(app)

def test_generate_cache():
    base_path = path.dirname(__file__)
    tip_path = path.join(base_path, '__test__', 'tip.png')
    vdt_path = path.join(base_path, '__test__', 'vdt.png')

    with open(tip_path, 'rb') as tip_file, open(vdt_path, 'rb') as vdt_file:
        files = {
            'files': (tip_path, tip_file, 'image/png')
        }
            # 'files': (vdt_path, vdt_file, 'image/png'),
        response = client.post("/uploadfiles/", files=files) # headers={"Content-Type": "multipart/form-data", "accept": "application/json"})
    
    print(response.content)

    assert response.status_code == 200
    assert "filenames" in response.json()
    assert len(response.json()["filenames"]) == 1
    assert "tip.png" in response.json()["filenames"][0]
    # assert "vdt.png" in response.json()["filenames"][1]

def test_hello_world():
    response = client.post("/world")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
