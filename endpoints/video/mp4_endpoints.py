from fastapi import APIRouter, UploadFile

app = APIRouter()


@app.post("/flv/")
async def convertToMP4(video: UploadFile):

    return "hello world"


@app.post("/mov/")
async def convertToMOV(video: UploadFile):

    return "hello world"

@app.post("/avi/")
async def convertToAVI(video: UploadFile):

    return "hello world"


@app.post("/webm/")
async def convertToWEBM(video: UploadFile):

    return "hello world"