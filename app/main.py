from redisai import Client
from uuid import uuid4

from PIL import Image
import io
from fastapi import FastAPI, UploadFile, HTTPException
from typing import List
from tip_adapter.tip_adapter import TipAdapter
from torch import cuda, backends, tensor

app = FastAPI()

device = 'cuda' if cuda.is_available() else 'mps' if backends.mps.is_available() else 'cpu'
if device != 'cuda':
    raise Exception("No GPU found, please check if CUDA is enabled")

redisai_client = Client(host='localhost', port=6379)

@app.post("/world")
async def hello_world():
    return {"message": "Hello World!"}

@app.post("/clip")
async def label(cache_id: str, file: UploadFile):
    request_object_content = await file.read()
    image = Image.open(io.BytesIO(request_object_content))

    tip = TipAdapter(device=device)
    tip.load_cache({
        "keys": tensor(redisai_client.tensorget(f"{cache_id}-keys")),
        "values": tensor(redisai_client.tensorget(f"{cache_id}-values"))
    })

    predictions = tip.run([image])

    return {
            "message": "Image Classified Successfully Completed",
            "predictions": predictions
        }

@app.post("/clip/cache")
async def generate_cache(labels: List[str], files: List[UploadFile]):
    if len(labels) != len(files):
        raise HTTPException(status_code=400, detail="The number of labels and files must be the same")

    data_dict = {}
    for label, file in zip(labels, files):
        request_object_content = await file.read()
        image = Image.open(io.BytesIO(request_object_content))
        data_dict[label] = [image]
    
    tip = TipAdapter(device=device)
    tip.create_cache(data_dict)
    
    if tip.cache['keys'] is None:
        raise HTTPException(status_code=500, detail="Cache generation failed")

    cache_id = str(uuid4())
    redisai_client.tensorset(f"{cache_id}-keys", tip.cache["keys"].cpu().numpy())
    redisai_client.tensorset(f"{cache_id}-values", tip.cache["values"].cpu().numpy())

    return {
            "message": "Cache Generated Successfully",
            "cache_id": cache_id
        }
