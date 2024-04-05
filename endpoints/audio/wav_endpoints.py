from fastapi import APIRouter, UploadFile
from controllers import AudioConversionController

app = APIRouter()


@app.post("/m4a/")
async def convertToM4A(audio: UploadFile):
    result = await AudioConversionController.convertWAVtoM4A(audio)
    return result

@app.post("/mp3/")
async def convertToMP3(audio: UploadFile):
    result = await AudioConversionController.convertWAVtoMP3(audio)
    return result

@app.post("/ogg/")
async def convertToOGG(audio: UploadFile):
    result = await AudioConversionController.convertWAVtoOGG(audio)
    return result