from fastapi import APIRouter, UploadFile
from controllers import VideoConversionController


app = APIRouter()


@app.post("/flv/")
async def convertToMP4(video: UploadFile):
    result = await VideoConversionController.convertMP4toFLV(video)
    return result


@app.post("/mov/")
async def convertToMOV(video: UploadFile):
    result = await VideoConversionController.convertMP4toFLV(video)
    return result

@app.post("/avi/")
async def convertToAVI(video: UploadFile):
    result = await VideoConversionController.convertMP4toAVI(video)
    return result


@app.post("/webm/")
async def convertToWEBM(video: UploadFile):
    result = await VideoConversionController.convertMP4toWEBM(video)
    return result