from fastapi import APIRouter, UploadFile
from controllers import VideoConversionController


app = APIRouter()


@app.post("/flv/")
async def convertToFLV(video: UploadFile):
    result = await VideoConversionController.convertWEBMtoFLV(video)
    return result


@app.post("/mov/")
async def convertToMOV(video: UploadFile):
    result = await VideoConversionController.convertWEBMtoMOV(video)
    return result

@app.post("/mp4/")
async def convertToMP4(video: UploadFile):
    result = await VideoConversionController.convertWEBMtoMP4(video)
    return result


@app.post("/avi/")
async def convertToAVI(video: UploadFile):
    result = await VideoConversionController.convertWEBMtoAVI(video)
    return result