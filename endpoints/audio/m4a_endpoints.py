from fastapi import APIRouter, UploadFile
from controllers import AudioConversionController

app = APIRouter()


@app.post("/mp3/")
async def convertToMP3(audio: UploadFile):
    result = await AudioConversionController.convertM4AtoMP3(audio)
    return result

@app.post("/ogg/")
async def convertToOGG(audio: UploadFile):
    result = await AudioConversionController.convertM4AtoOGG(audio)
    return result

@app.post("/wav/")
async def convertToWAV(audio: UploadFile):
    result = await AudioConversionController.convertM4AtoWAV(audio)
    return result