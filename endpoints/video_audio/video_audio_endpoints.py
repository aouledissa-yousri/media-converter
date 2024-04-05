from fastapi import APIRouter, UploadFile
from controllers import VideoConversionController


app = APIRouter()

@app.post("/")
async def convertToAudio(video: UploadFile, outputFormat: str):
    result = await VideoConversionController.convertToAudio(video, outputFormat)
    return result

