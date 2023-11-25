from fastapi import FastAPI

app = FastAPI()

@app.post("/clip/train")
async def clip_train():
    return {"message": "Endpoint for Generating KV Cache"}

@app.get("/clip")
async def clip_train():
    return {"message": "Endpoint for getting CLIP Labels"}
