from fastapi import APIRouter, UploadFile
from controllers import VideoConversionController


app = APIRouter()


@app.post("/avi/")
async def convertToFLV(video: UploadFile):
    result = await VideoConversionController.convertFLVtoAVI(video)
    return result


@app.post("/mov/")
async def convertToMOV(video: UploadFile):
    result = await VideoConversionController.convertFLVtoMOV(video)
    return result

@app.post("/mp4/")
async def convertToMP4(video: UploadFile):
    result = await VideoConversionController.convertFLVtoMP4(video)
    return result


@app.post("/webm/")
async def convertToWEBP(video: UploadFile):
    result = await VideoConversionController.convertFLVtoWEBM(video)
    return result