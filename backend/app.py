
from fastapi import FastAPI, UploadFile, File
import tempfile
import os

from predictor import predict_banana

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Banalyzer API running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        temp.write(await file.read())
        image_path = temp.name

    result = predict_banana(image_path)

    os.remove(image_path)

    return result
