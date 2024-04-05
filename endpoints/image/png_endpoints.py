from fastapi import APIRouter, File, UploadFile
from controllers import ImageConversionController

app = APIRouter()


@app.post("/jpg/")
async def convertToJPG(image: UploadFile = File(...)):
    result = await ImageConversionController.convertPNGtoJPG(image)
    return result


@app.post("/svg/")
async def convertToSVG(image: UploadFile):
    result = await ImageConversionController.convertPNGtoSVG(image)
    return result

@app.post("/webp/")
async def convertToWEBP(image: UploadFile):
    result = await ImageConversionController.convertPNGtoWEBP(image)
    return result