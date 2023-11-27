from PIL import Image
import io
from fastapi import FastAPI, UploadFile
from typing import List
from tip_adapter.tip_adapter import TipAdapter
from torch import cuda, backends

app = FastAPI()

device = 'cuda' if cuda.is_available() else 'mps' if backends.mps.is_available() else 'cpu'
tip = TipAdapter(device=device)

@app.post("/world")
async def hello_world():
    return {"message": "Hello World!"}

@app.post("/clip")
async def label(file: UploadFile):
    request_object_content = await file.read()
    image = Image.open(io.BytesIO(request_object_content))

    tip.run([image])

    return {"label": f"A cool png with path: {file.filename}"}

@app.post("/clip/cache")
async def generate_cache(labels: List[str], files: List[UploadFile]):
    if len(labels) != len(files):
        return {"message": "The number of labels and files must be the same"}, 400
    
    data_dict = {}
    for label, file in zip(labels, files):
        # Here, save the file or process it
        request_object_content = await file.read()
        image = Image.open(io.BytesIO(request_object_content))
        data_dict[label] = [image]
        
    tip.create_cache(data_dict)

    # Return the filenames as a JSON response
    return {"filenames": len(labels)}
