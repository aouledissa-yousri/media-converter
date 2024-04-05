from fastapi import APIRouter, UploadFile
from controllers import ImageConversionController

app = APIRouter()


@app.post("/jpg/")
async def convertToJPG(image: UploadFile):
    result = await ImageConversionController.convertWEBPtoJPG(image)
    return result


@app.post("/png/")
async def convertToPNG(image: UploadFile):
    result = await ImageConversionController.convertWEBPtoPNG(image)
    return result

@app.post("/svg/")
async def convertToSVG(image: UploadFile):
    result = await ImageConversionController.convertWEBPtoSVG(image)
    return result