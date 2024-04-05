from fastapi import APIRouter, UploadFile
from controllers import ImageConversionController

app = APIRouter()


@app.post("/png/")
async def convertToPNG(image: UploadFile):
    result = await ImageConversionController.convertJPGtoPNG(image)
    return result

@app.post("/svg/")
async def convertToSVG(image: UploadFile):
    result = await ImageConversionController.convertPNGtoSVG(image)
    return result

@app.post("/webp/")
async def convertToWEBP(image: UploadFile):
    result = await ImageConversionController.convertPNGtoWEBP(image)
    return result