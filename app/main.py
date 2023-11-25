from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

@app.post("/world")
async def generate_cache():
    return {"message": "Hello World!"}

@app.post("/clip/train")
async def generate_cache():
    return {"message": "Endpoint for Generating KV Cache"}

@app.get("/clip")
async def label():
    return {"message": "Endpoint for getting CLIP Labels"}

@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    file_names = []
    for file in files:
        # Here, save the file or process it
        file_names.append(file.filename)

    # Return the filenames as a JSON response
    return {"filenames": file_names}
