from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

@app.post("/world")
async def hello_world():
    return {"message": "Hello World!"}

@app.get("/clip")
async def label():
    return {"message": "Endpoint for getting CLIP Labels"}

@app.post("/clip/cache")
async def generate_cache(files: List[UploadFile]):
    file_names = []
    for file in files:
        # Here, save the file or process it
        file_names.append(file.filename)

    # Return the filenames as a JSON response
    return {"filenames": file_names}
