from fastapi import APIRouter, UploadFile
from controllers import AudioConversionController

app = APIRouter()


@app.post("/m4a/")
async def convertToM4A(audio: UploadFile):
    result = await AudioConversionController.convertMP3toM4A(audio)
    return result

@app.post("/ogg/")
async def convertToOGG(audio: UploadFile):
    result = await AudioConversionController.convertMP3toOGG(audio)
    return result

@app.post("/wav/")
async def convertToWAV(audio: UploadFile):
    result = await AudioConversionController.convertMP3toWAV(audio)
    return result