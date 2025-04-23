from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os
from app.detection import detect_vehicles

app = FastAPI()


@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    input_dir = "inputs"
    os.makedirs(input_dir, exist_ok=True)
    image_path = os.path.join(input_dir, file.filename)

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    detections = detect_vehicles(image_path)
    return JSONResponse(content=detections)
