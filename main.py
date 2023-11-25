from fastapi import FastAPI

app = FastAPI()

@app.post("/clip/train")
async def generate_cache():
    return {"message": "Endpoint for Generating KV Cache"}

@app.get("/clip")
async def label():
    return {"message": "Endpoint for getting CLIP Labels"}
