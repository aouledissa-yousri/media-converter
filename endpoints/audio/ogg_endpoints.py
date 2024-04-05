from fastapi import APIRouter, UploadFile
from controllers import AudioConversionController

app = APIRouter()


@app.post("/m4a/")
async def convertToM4a(audio: UploadFile):
    result = await AudioConversionController.convertOGGtoM4A(audio)
    return result

@app.post("/mp3/")
async def convertToMP3(audio: UploadFile):
    result = await AudioConversionController.convertOGGtoMP3(audio)
    return result

@app.post("/wav/")
async def convertToWAV(audio: UploadFile):
    result = await AudioConversionController.convertOGGtoWAV(audio)
    return result