from fastapi import APIRouter, UploadFile
from controllers import VideoConversionController


app = APIRouter()


@app.post("/flv/")
async def convertToMOV(video: UploadFile):
    result = await VideoConversionController.convertMOVtoFLV(video)
    return result


@app.post("/avi/")
async def convertToAVI(video: UploadFile):
    result = await VideoConversionController.convertMOVtoAVI(video)
    return result

@app.post("/mp4/")
async def convertToMP4(video: UploadFile):
    result = await VideoConversionController.convertMOVtoMP4(video)
    return result


@app.post("/webm/")
async def convertToWEBM(video: UploadFile):
    result = await VideoConversionController.convertMOVtoWEBM(video)
    return result