from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

@app.post("/world")
async def hello_world():
    return {"message": "Hello World!"}

@app.post("/clip")
async def label(file: UploadFile):
    return {"label": f"A cool png with path: {file.filename}"}

@app.post("/clip/cache")
async def generate_cache(files: List[UploadFile]):
    file_names = []
    for file in files:
        # Here, save the file or process it
        file_names.append(file.filename)

    # Return the filenames as a JSON response
    return {"filenames": file_names}
