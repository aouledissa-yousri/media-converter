from fastapi import APIRouter, UploadFile
from controllers import VideoConversionController

app = APIRouter()


@app.post("/flv/")
async def convertToFLV(video: UploadFile):
    result = await VideoConversionController.convertAVItoFLV(video)
    return result

@app.post("/mov/")
async def convertToMOV(video: UploadFile):
    result = await VideoConversionController.convertAVItoMOV(video)
    return result

@app.post("/mp4/")
async def convertToMP4(video: UploadFile):
    result = await VideoConversionController.convertAVItoMP4(video)
    return result


@app.post("/webm/")
async def convertToWEBM(video: UploadFile):
    result = await VideoConversionController.convertAVItoWEBM(video)
    return result