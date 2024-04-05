from fastapi import APIRouter, UploadFile
from controllers import ImageConversionController

app = APIRouter()


@app.post("/jpg/")
async def convertToJPG(image: UploadFile):
    result = await ImageConversionController.convertSVGtoJPG(image)
    return result

@app.post("/png/")
async def convertToPNG(image: UploadFile):
    result = await ImageConversionController.convertSVGtoPNG(image)
    return result

@app.post("/webp/")
async def convertToWEBP(image: UploadFile):
    result = await ImageConversionController.convertSVGtoWEBP(image)
    return result