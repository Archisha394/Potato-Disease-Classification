from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.get("/ping")
async def ping():
    return "hello world"


@app.post("/predict")
async def prediction():
    file: UploadFile = File(...)
